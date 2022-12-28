import os

os.sys.path.insert(0, os.getcwd().split('/dags')[0])

from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.decorators import dag
from airflow import DAG
from tasks import extract
from tasks import transform
from tasks import load
from tasks import cleanup

import pendulum


@dag(
    default_args={
        'depends_on_past': False,
        'retries': 0,
        'retry_delay': timedelta(minutes=5),
    },
    tags=["git_commits"],
    description="DAG to extract, transform and load data from user's commits to Data Warehouse",
    schedule_interval=timedelta(days=7),
    start_date=pendulum.datetime(pendulum.today().year, pendulum.today().month, pendulum.today().day, tz='UTC'),
    catchup=False,
    dag_id='commits_dag'
)
def CommitsDAG():
    extract_task = extract.LoadToStaging()
    transform_task = transform.TransformData()
    load_task = load.LoadToDW()
    cleanup_task = cleanup.CleanUp()

    extract_task >> transform_task >> load_task >> cleanup_task


d = CommitsDAG()
