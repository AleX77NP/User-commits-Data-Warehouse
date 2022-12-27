import sqlite3

db_connection = sqlite3.connect('git_activity.db')

cursor_obj = db_connection.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS USER")
cursor_obj.execute("DROP TABLE IF EXISTS REPO")
cursor_obj.execute("DROP TABLE IF EXISTS USER_COMMIT")

user_table = """ CREATE TABLE USER (
                 User_Key INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 User_Email VARCHAR(50) UNIQUE NOT NULL,
                 User_Alias VARCHAR(20) UNIQUE NOT NULL,
                 Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
            ); """

repo_table = """ CREATE TABLE REPO (
                 Repo_Key INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 Repo_Name VARCHAR(50) UNIQUE NOT NULL,
                 Repo_Owner VARCHAR(20) NOT NULL,
                 Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
            ); """


user_commit_table = """ CREATE TABLE USER_COMMIT (
                        Commit_Key INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        Commit_Text VARCHAR(100) NOT NULL,
                        Commit_Hash CHAR(40) NOT NULL,
                        Commit_Time TEXT NOT NULL,
                        Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                        User_Key INTEGER NOT NULL,
                        Repo_Key INTEGER NOT NULL,
                        FOREIGN KEY(User_key) REFERENCES USER(User_Key),
                        FOREIGN KEY(Repo_key) REFERENCES REPO(Repo_Key)
                    ); """

cursor_obj.execute(user_table)
cursor_obj.execute(repo_table)
cursor_obj.execute(user_commit_table)

db_connection.close()
