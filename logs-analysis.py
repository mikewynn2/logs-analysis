#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def fetch_data(query):
    """ fetch data from database """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    data = c.fetchall()
    db.close()
    return data


def top_three_articles():
    # 1. What are the most popular three articles of all time ?
    query = """
        SELECT COUNT(*) AS views, title
        FROM log
            JOIN articles ON RIGHT(path, -9) = articles.slug
        WHERE path LIKE '/article%'
        GROUP BY title
        ORDER BY views DESC
        LIMIT 3;
    """
    result = fetch_data(query)
    print('The 3 most popular articles of all time:')
    print('')
    for views, title in result:
        print('- "{title}" -- {views} Views'.format(views=views, title=title))


def most_popular_authors():
    # 2. Who are the most popular article authors of all time?
    query = """
    SELECT COUNT(*) AS views, name
    FROM log
        JOIN articles ON RIGHT(path, -9) = articles.slug
        JOIN authors ON authors.id = articles.author
    WHERE path LIKE '/article%'
    GROUP BY name
    ORDER BY views DESC;
    """
    result = fetch_data(query)
    print('The most popular article authors of all time:')
    print('')
    for views, name in result:
        print('- {name} -- {views} Views'.format(name=name, views=views))


def error_days():
    # 3. On which days did more than 1% of requests lead to errors?
    query = """
    SELECT err_percent, day
    FROM (
        SELECT (err_count / CAST (total AS DOUBLE PRECISION))
            AS err_percent, err_log.day
        FROM (
                SELECT COUNT(*) AS total, date(time) AS day
                FROM log
                GROUP BY day
            ) AS total_log
            JOIN (
                SELECT COUNT(*) AS err_count, date(time) AS day
                FROM log
                WHERE status LIKE '404%'
                GROUP BY day
            ) AS err_log ON err_log.day = total_log.day
    ) AS percent_log
    WHERE err_percent > 0.01;
    """
    result = fetch_data(query)
    print('Dates where more than 1% of requests lead to errors:')
    print('')
    for percent, day in result:
        print('-  {:%B %d, %Y} -- {:.1%} errors'.format(day, percent))


if __name__ == '__main__':
    top_three_articles()
    print('')
    most_popular_authors()
    print('')
    error_days()
