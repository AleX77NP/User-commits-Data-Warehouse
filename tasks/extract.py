from airflow.decorators import task
from data_handler import FakeCommitApi
from couchdb_handle import CouchHandler
import os

os.environ["no_proxy"] = "*"


@task(task_id="extract")
def LoadToStaging():
    api = FakeCommitApi()
    ch = CouchHandler()

    iterations = 10
    commit_list = []

    try:
        for i in range(iterations):
            data = api.get_data()
            commit_list.append(data)

        for commit_data in commit_list:
            ch.insert({
                "item": commit_data
            })
    except BaseException as e:
        print("ERRORS: ", e)


