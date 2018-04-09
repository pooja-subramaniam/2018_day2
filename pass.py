def get_credentials():
    username = input('Please type your user name: ')
    password = input('Please type your password')
    return username, password

def authenticate(username, password, pwdb):
    if username in pwdb:
        if pwdb[username] == password:
            return True
    return False

def add_user(username, password, pwdb):
    pwdb.update({username:password})



pwdb = {}
username, password = get_credentials()
add_user(username, password, pwdb)
if authenticate(username, password, pwdb):
    print('Match!')
else:
    print('Not a match!')
