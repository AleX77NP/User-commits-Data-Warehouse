from airflow.decorators import task
from couchdb_handle import CouchHandler


def transform(message):
    commit_message = message.capitalize().rstrip('\r\n')
    return commit_message


@task(task_id='transform')
def TransformData():
    ch = CouchHandler()
    for idx in ch.db:
        doc = ch.db[idx]
        commit_message = transform(doc.get('item').get('commit').get('commit_message'))
        doc['item']['commit']['commit_message'] = commit_message
        ch.db.save(doc)
