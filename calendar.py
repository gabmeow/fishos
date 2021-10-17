import os
import time

print("""

░█████╗░░█████╗░██╗░░░░░███████╗███╗░░██╗██████╗░░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░█████╗░░██╔██╗██║██║░░██║███████║██████╔╝
██║░░██╗██╔══██║██║░░░░░██╔══╝░░██║╚████║██║░░██║██╔══██║██╔══██╗
╚█████╔╝██║░░██║███████╗███████╗██║░╚███║██████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
""")

print("Today is: " + time.strftime("%m/%d/%y"))

ncommdo = open('fishos/commitments.txt')
ncommco = open('fishos/commitments.txt')
ncview = ncommdo.read()

print("Your recent commitments: " + ncview)

choice = input("""
[1] Make or delete commitments
[2] Go back to the home
""")

if choice == '1':

    print("""
[1] Make a new commitment
[2] Delete a commitment
[3] Exit
    """)

    choose = input("[?]: ")

    if choose == '1':

        n_comm_d = input(str("Please enter the date and the message of your commitment: "))

        with open('user/commitments.txt', 'w') as f:
            f.writelines(n_comm_d)
            print("Succesfully created a commitment!")
            print("[1] Exit")
            back = input("[?]: ")

            if back == '1':
                os.startfile('calendar.py')
                os.close('calendar.py')

    if choose == '2':
        print("Press 1 to delete your commitments")
        clear = input()
        if clear == '1':
            with open('user/commitments.txt', 'w') as f:
                ciao = str()
                f.writelines(ciao)
            print("Succesfully deleted your commitments!")
            print("""
[1] Exit
            """)

        choose2 = input("[?]: ")

        if choose2 == '1':
            os.startfile('calendar.py')
            os.close('calendar.py')

if choice == '2':
    os.startfile('home.py')
    os.close('calendar.py')
