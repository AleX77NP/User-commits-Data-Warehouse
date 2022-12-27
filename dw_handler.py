import sqlite3


class DataWarehouseHandler:
    def __init__(self):
        self.db = sqlite3.connect('git_activity.db')
        self.cursor = self.db.cursor()

    def save(self):
        self.db.commit()

    def insert_user(self, user):
        user_data = (user['user_email'], user['user_alias'])
        sql = ''' INSERT INTO USER (User_Email, User_Alias) VALUES (?, ?) '''
        self.cursor.execute(sql, user_data)
        self.save()

    def insert_repo(self, repo):
        repo_data = (repo['repo_name'], repo['repo_owner'])
        sql = ''' INSERT INTO REPO (Repo_Name, Repo_Owner) VALUES (?, ?) '''
        self.cursor.execute(sql, repo_data)
        self.save()

    def insert_commit(self, commit):
        commit_data = (commit['commit_text'], commit['commit_hash'], commit['commit_time'])
        sql = ''' INSERT INTO USER_COMMIT (Commit_Text, Commit_Hash, Commit_Time) VALUES (?, ?, ?) '''
        self.cursor.execute(sql, commit_data)
        self.save()

