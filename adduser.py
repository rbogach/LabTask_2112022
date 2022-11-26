import os


def new_user():
    confirm = "N"

    while confirm != "Y":
        userName = input("Enter user name: ")

        print("Use user name: '" + userName + "' ?(Y/N)")

        confirm = input().upper()

    os.system("sudo adduser " + userName)


new_user()