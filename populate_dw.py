from data_handler import UserHandler, RepoHandler
from dw_handler import DataWarehouseHandler

dwh = DataWarehouseHandler()


def insert_users():
    uh = UserHandler("https://random-data-api.com/api/v2/users")
    for i in range(10):
        user = uh.get_user()
        dwh.insert_user(user)


def insert_repos():
    rh = RepoHandler("https://random-word-api.herokuapp.com/word")
    for i in range(10):
        repo = rh.get_repo()
        dwh.insert_repo(repo)


# insert_users()
# insert_repos()
