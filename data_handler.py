import requests
from random import randrange


class DataHandler:
    def __init__(self, url):
        self.url = url

    def fetch_json_data(self):
        response = requests.request("GET", self.url)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        return response.json()

    def fetch_text_data(self):
        response = requests.request("GET", self.url)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        return response.text


class UserHandler(DataHandler):
    def __init__(self, url):
        DataHandler.__init__(self, url)

    def get_user(self):
        data = self.fetch_json_data()
        user = {
            'user_email': data['email'],
            'user_alias': data['username']
        }

        return user


class RepoHandler(DataHandler):
    def __init__(self, url):
        DataHandler.__init__(self, url)

    def get_repo(self):
        data = self.fetch_json_data()
        repo = {
            'repo_name': data[0],
            'repo_owner': 'AleX77NP',
            'repo_org': 'JoyoDev'
        }

        return repo


class CommitHandler(DataHandler):
    def __init__(self, url):
        DataHandler.__init__(self, url)

    def get_commit(self):
        data = self.fetch_text_data()
        return data


class FakeCommitApi:
    def __init__(self):
        self.uh = UserHandler("https://random-data-api.com/api/v2/users")
        self.rh = RepoHandler("https://random-word-api.herokuapp.com/word")
        self.ch = CommitHandler("https://whatthecommit.com/index.txt")
        self.branches = ["master", "dev", "release", "staging"]
        for i in range(10):
            ticket_num = randrange(1, 200)  # generate ticket number
            self.branches.append(f'feature/ticket-{ticket_num}')

    def get_data(self):
        user = self.uh.get_user()
        repo = self.rh.get_repo()
        branch = self.branches[randrange(0, 13)]
        commit_message = self.ch.get_commit()
        commit = {
            'commit_message': commit_message,
            'commit_hash': commit_message.encode().hex()[0:40],
            'commit_line_diff': randrange(1, 1000),
            'commit_file_diff': randrange(1, 15)
        }

        # return document in JSON format
        return {
            'user': user,
            'repo': repo,
            'branch': branch,
            'commit': commit
        }


# api = FakeCommitApi()
# print(api.get_data())
