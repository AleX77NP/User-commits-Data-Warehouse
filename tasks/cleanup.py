from airflow.decorators import task
from couchdb_handle import CouchHandler


@task(task_id="cleanup")
def CleanUp():
    ch = CouchHandler()
    rows = ch.db.view('_all_docs', include_docs=True)
    docs = []
    for row in rows:
        if row['id'].startswith('_'):
            continue
        doc = row['doc']
        doc['_deleted'] = True
        docs.append(doc)
    ch.db.update(docs)
