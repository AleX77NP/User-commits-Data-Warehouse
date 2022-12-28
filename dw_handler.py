import sqlite3


class DataWarehouseHandler:
    def __init__(self):
        self.db = sqlite3.connect('git_activity.db')
        self.cursor = self.db.cursor()

    def save(self):
        self.db.commit()

    def insert_user(self, user):
        user_data = (user['user_key'], user['user_email'], user['user_alias'])
        sql = ''' INSERT INTO USER_DIM (User_Key, User_Email, User_Alias) VALUES (?, ?, ?) '''
        self.cursor.execute(sql, user_data)
        self.save()

    def insert_repo(self, repo):
        repo_data = (repo['repo_key'], repo['repo_name'], repo['repo_owner'], repo['repo_org'])
        sql = ''' INSERT INTO REPO_DIM (Repo_Key, Repo_Name, Repo_Owner, RepoOrg) VALUES (?, ?, ?, ?) '''
        self.cursor.execute(sql, repo_data)
        self.save()

    def insert_branch(self, branch):
        repo_data = (branch['branch_key'], branch['branch_name'])
        sql = ''' INSERT INTO BRANCH_DIM (Branch_Key, Branch_Name) VALUES (?, ?) '''
        self.cursor.execute(sql, repo_data)
        self.save()

    def insert_commit(self, commit):
        commit_data = (commit['commit_key'], commit['commit_message'], commit['commit_hash'], commit['commit_time'],
                       commit['commit_line_diff'], commit['commit_file_diff'], commit['user_key'], commit['repo_key'],
                       commit['branch_key'])
        sql = '''INSERT INTO COMMIT_FACT (Commit_Key, Commit_Message, Commit_Hash, Commit_Time, Commit_Line_Diff, 
        Commit_File_Diff, User_Key, Repo_Key, Branch_Key) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) '''
        self.cursor.execute(sql, commit_data)
        self.save()
