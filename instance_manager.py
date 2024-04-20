# instance manager

import pickle
import ui_functions as user_in
import ui_output as show_user

userlist="usernames.dat"

def get_usernames()
    try:
        with open(userlist,'r') as users:
            usernames = users.readlines()
        return usernames


def new_user():
    forbidden = get_usernames()
    while True:
        username = user_in.get_string("username")
        if username in forbidden:
            print("Username already in use! Try another.")
            continue
    if not username: return False
    with open(userlist, 'a+') as users:
        users.write(username+"\n")

