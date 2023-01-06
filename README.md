# DESCRIPTION:
Example of ETL pipeline implemented using Python and Airflow. FakeCommitApi generates
fake data for users, repos, branches and user commits. Check Data Warehouse design - `images/DW_Schema.png`

Pipeline consists of following tasks:

1. extract (CouchDB used for staging)
2. transform
3. load into Data Warehouse

Technologies used: Python, Sqlite, Apache CouchDB, Apache Airflow
# STEPS:
- create virtual environment 
- download dependencies
- create Data Warehouse tables by running `python3 dw_setup.py`
- run `CouchDB` locally (Docker or installation)
- export `COUCH_USER` and `COUCH_PASSWORD` env variables in all shells 
- set path variable `AIRFLOW_HOME` to this directory `export AIRFLOW_HOME=$(pwd)`
- set environment variables for twitter credentials and DB details
- run `airflow db init`
- you probably don't hav any airflow user yet, so create one, run `airflow users create` and follow instructions
- open current directory in two terminal windows run `airflow scheduler` in one and `airflow webserver` in other
- go to `localhost:8080` and login with the user credentials you just created
- you should be able to see `commits_dag` there

## Notes:
Since data is randomly generated, there are no checks if user/repo/branch already exists.
This is just a simple example to show how to schedule pipeline with Airflow and implement basic 
extract, transform and load operations, as well as data modeling.