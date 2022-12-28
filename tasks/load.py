from airflow.decorators import task
from couchdb_handle import CouchHandler
from dw_handler import DataWarehouseHandler
from datetime import datetime
import uuid


@task(task_id="load")
def LoadToDW():
    ch = CouchHandler()
    dwh = DataWarehouseHandler()
    for idx in ch.db:
        doc = ch.db[idx]
        try:
            commit_doc = doc.get('item')

            user_key = str(uuid.uuid4().int & (1 << 64) - 1)
            repo_key = str(uuid.uuid4().int & (1 << 64) - 1)
            branch_key = str(uuid.uuid4().int & (1 << 64) - 1)
            date_key = str(uuid.uuid4().int & (1 << 64) - 1)

            # user
            user_data = commit_doc.get('user')
            user = {
                'user_key': user_key,
                'user_email': user_data.get('user_email'),
                'user_alias': user_data.get('user_alias'),
            }

            # repo
            repo_data = commit_doc.get('repo')
            repo = {
                'repo_key': repo_key,
                'repo_name': repo_data.get('repo_name'),
                'repo_owner': repo_data.get('repo_owner'),
                'repo_org': repo_data.get('repo_org'),
            }

            # branch
            branch_data = commit_doc.get('branch')
            branch = {
                'branch_key': branch_key,
                'branch_name': branch_data.get('branch_name')
            }

            # date
            date = {
                "date_key": date_key,
                "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }

            # commit
            commit_data = commit_doc.get('commit')
            commit = {
                'commit_message': commit_data.get('commit_message'),
                'commit_hash': commit_data.get('commit_hash'),
                'commit_line_diff': commit_data.get('commit_line_diff'),
                'commit_file_diff': commit_data.get('commit_file_diff'),
                'user_key': user_key,
                'repo_key': repo_key,
                'branch_key': branch_key,
                "date_key": date_key
            }

        except BaseException as e:
            print("ERROR: ", e)
            print("COMMIT_DATA", commit_doc)
