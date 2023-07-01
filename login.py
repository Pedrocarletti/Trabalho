from pymongo import MongoClient

def check_login(username, password):
    client = MongoClient()
    db = client['pedro']
    users = db.users

    user = users.find_one({'username': username, 'password': password})
    if user is None:
        return False
    else:
        return True

if __name__ == '__main__':
    print(check_login('example_user', 'example_password'))
