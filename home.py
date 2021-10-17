import time
import os
import socket

login_pass = open('user/password.txt')
login_name = open('user/username.txt')
lp = login_pass.read()
ln = login_name.read()

print("""

███████╗██╗░██████╗██╗░░██╗░█████╗░░██████╗
██╔════╝██║██╔════╝██║░░██║██╔══██╗██╔════╝
█████╗░░██║╚█████╗░███████║██║░░██║╚█████╗░
██╔══╝░░██║░╚═══██╗██╔══██║██║░░██║░╚═══██╗
██║░░░░░██║██████╔╝██║░░██║╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░ 
""")

print("WELCOME " + ln)
print("Today is: " + time.strftime("%m/%d/%y"))
print("""
[1] Google
[2] Text Editor
[3] File Explorer
[4] Calendar
[5] Terminal
[6] Activity Gestor (NOT AVALIBLE ON THIS VERSION)
[7] Safe Shutdown
""")
select = input("[?]: ")
if select == '1':
    os.startfile('browser.py')
    os.startfile('browsop.py')

if select == '2':
    os.startfile('edit.py')
    os.startfile('txtedop.py')

if select == '3':
    os.startfile('explorer.py')

if select == '4':
    os.startfile('calendar.py')    
    
if select == '5':
    os.startfile('terminal.py')
    
if select == '6':
    os.startfile('act.py')

if select == '7':
    os.close('home.py')
