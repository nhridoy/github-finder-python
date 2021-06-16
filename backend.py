import requests

def userInfo(userName = ""):
    data = requests.get(f'https://api.github.com/users/{userName}')
    repo = requests.get(f'https://api.github.com/users/{userName}/repos')
    userDatas = data.json()
    userRepos = data.json()
    # print(userDatas)
    return userDatas, userRepos

# print(userInfo("nhridoy"))