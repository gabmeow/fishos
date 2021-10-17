import time
import os

print("""

███████╗██╗░██████╗██╗░░██╗░█████╗░░██████╗  ░██████╗███████╗████████╗██╗░░░██╗██████╗░
██╔════╝██║██╔════╝██║░░██║██╔══██╗██╔════╝  ██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗
█████╗░░██║╚█████╗░███████║██║░░██║╚█████╗░  ╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝
██╔══╝░░██║░╚═══██╗██╔══██║██║░░██║░╚═══██╗  ░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░
██║░░░░░██║██████╔╝██║░░██║╚█████╔╝██████╔╝  ██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░
╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░  ╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░
""")

print("""
[1] Continue Whit Setup
[2] Setup Already Done
""")

setup = input("[?]: ")
if setup == "1":
    name = input(str("Please Enter Your Username: "))
    pas = input(str("Please Enter Your Password: "))

    with open('user/username.txt', 'w') as f:
        f.writelines(name)

    with open('user/password.txt', 'w') as f:
        f.writelines(pas)
    print("Setup Finished!")
    print("Please Press Enter To Restart The OS")

if setup == '2':
    login_pass = open('user/password.txt')
    login_name = open('user/username.txt')
    lp = login_pass.read()
    ln = login_name.read()

while True:
    login = input(str("Please Enter The Password " + ln + ': '))
    if login == lp:
        os.startfile("home.py")
        break
    else:
        print("Wrong Password!")
