import requests
import datetime


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
        }
        return repo


class CommitHandler(DataHandler):
    def __init__(self, url):
        DataHandler.__init__(self, url)

    def get_commit(self):
        data = self.fetch_text_data()
        commit = {
            'commit_text': data,
            'commit_hash': data.encode().hex()[0:40],
            'commit_time': datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        }
        return commit

# uh = UserHandler("https://random-data-api.com/api/v2/users")
# print(uh.get_user())
# rh = RepoHandler("https://random-word-api.herokuapp.com/word")
# print(rh.get_repo())
# ch = CommitHandler("https://whatthecommit.com/index.txt")
# print(len(ch.get_commit()['commit_hash']))
