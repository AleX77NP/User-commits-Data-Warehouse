import sqlite3

db_connection = sqlite3.connect('git_activity.db')

cursor_obj = db_connection.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS USER_DIM")
cursor_obj.execute("DROP TABLE IF EXISTS REPO_DIM")
cursor_obj.execute("DROP TABLE IF EXISTS BRANCH_DIM")
cursor_obj.execute("DROP TABLE IF EXISTS COMMIT_FACT")

user_dim_table = """ CREATE TABLE USER_DIM (
                 User_Key CHAR(36) PRIMARY KEY NOT NULL,
                 User_Email VARCHAR(50) UNIQUE NOT NULL,
                 User_Alias VARCHAR(20) UNIQUE NOT NULL,
                 Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
            ); """

repo_dim_table = """ CREATE TABLE REPO_DIM (
                 Repo_Key CHAR(36) PRIMARY KEY NOT NULL,
                 Repo_Name VARCHAR(50) UNIQUE NOT NULL,
                 Repo_Org VARCHAR(30) NOT NULL,
                 Repo_Owner VARCHAR(20) NOT NULL,
                 Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
            ); """

branch_dim_table = """ CREATE TABLE BRANCH_DIM (
                   Branch_Key CHAR(36) PRIMARY KEY NOT NULL,
                   Branch_Name VARCHAR(20) UNIQUE NOT NULL,
                   Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
            ); """


commit_fact_table = """ CREATE TABLE COMMIT_FACT (
                        Commit_Key CHAR(36) PRIMARY KEY NOT NULL,
                        Commit_Message VARCHAR(100) NOT NULL,
                        Commit_Hash CHAR(40) NOT NULL,
                        Commit_Time TEXT NOT NULL,
                        Commit_Line_Diff SMALLINT NOT NULL,
                        Commit_File_Diff SMALLINT NOT NULL,
                        Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                        User_Key CHAR(36) NOT NULL,
                        Repo_Key CHAR(36)NOT NULL,
                        Branch_Key CHAR(36) NOT NULL,
                        FOREIGN KEY(User_key) REFERENCES USER_DIM(User_Key),
                        FOREIGN KEY(Repo_key) REFERENCES REPO_DIM(Repo_Key),
                        FOREIGN KEY(Branch_key) REFERENCES BRANCH_DIM(Branch_Key)
                    ); """

cursor_obj.execute(user_dim_table)
cursor_obj.execute(repo_dim_table)
cursor_obj.execute(branch_dim_table)
cursor_obj.execute(commit_fact_table)

db_connection.close()
