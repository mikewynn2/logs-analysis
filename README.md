# Log Analysis Project
This is a project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
## Project Description:
This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

    1. What are the most popular three articles of all time?
    2. Who are the most popular article authors of all time? 
    3. On which days did more than 1% of requests lead to errors?

## This Project Requires a Bit of Setup:
This project is run in a virutal machine created using Vagrant so there are a few steps
to get set up:
#### Installing the dependencies and setting up the files:
1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. Download the vagrantfile(https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile)
    These files configure the virtual machine and install all the tools needed to run this project.
1. Download the database setup: [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
1. Unzip the data to get the newsdata.sql file.
1. Put the newsdata.sql file into the vagrant directory
1. Download this project: [log analysis](https://github.com/mikewynn2/log-analysis)
1. Upzip as needed and copy all files into the vagrant directory into a folder called log-analysis
#### Start the Virtual Machine:
1. Open Terminal and navigate to the project folders we setup above.
1. cd into the vagrant directory
1. Run ``` vagrant up ``` to build the VM for the first time.
1. Once it is built, run ``` vagrant ssh ``` to connect.
1. cd into the correct project directory: ``` cd /vagrant/log-analysis ```
#### Load the data into the database:
1. Load the data using the following command: ``` psql -d news -f newsdata.sql ```


## Run The Project
1. You should already have vagrant up and be connected to it. 
1. If you aren't already, cd into the correct project directory: ``` cd /vagrant/log-analysis ```
1. Run ``` python3 logs-analysis.py ```

Generating this information will take several seconds, but will now start loading. 

## EXPECTED OUTPUT:

The 3 most popular articles of all time:

- "Candidate is jerk, alleges rival" -- 338647 Views
- "Bears love berries, alleges bear" -- 253801 Views
- "Bad things gone, say good people" -- 170098 Views

The most popular article authors of all time:

- Ursula La Multa -- 507594 Views
- Rudolf von Treppenwitz -- 423457 Views
- Anonymous Contributor -- 170098 Views
- Markoff Chaney -- 84557 Views

Dates where more than 1% of requests lead to errors:

-  July 17, 2016 -- 2.3% errors

