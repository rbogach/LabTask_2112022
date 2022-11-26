import subprocess
import os


def add_user_to_group():
    username = input("Enter the name of the user that you want to add to a group: ")
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]
    print("Enter a list of groups to add the user to")
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3")
    print("The available groups are:\r\n " + output)
    chosen_groups = str(input("Groups: "))
    output = output.split(" ")
    chosen_groups = chosen_groups.split(" ")
    print("Add To:")
    found = True
    group_string = ""
    for grp in chosen_groups:
        for existingGrp in output:
            if grp == existingGrp:
                found = True
                print("-Existing Group : " + grp)
                group_string = group_string + grp + ","
            if not found:
                print("-New Group : " + grp)
                group_string = group_string + grp + ","
            else:
                found = False
                groupString = group_string[:-1] + " "
                confirm = ""
                while confirm != "Y" and confirm != "N":
                    print("Add user '" + username + "' to these groups? (Y/N)")
                    confirm = input().upper()
                    if confirm == "N":
                        print("User '" + username + "' not added")
                    elif confirm == "Y":
                        os.system("sudo usermod -aG " + groupString + username)
                        print("User ‘" + username + " added")


add_user_to_group()
