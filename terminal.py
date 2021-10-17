import subprocess
import platform
import socket
import os
import time


login_pass = open('password.txt')
login_name = open('username.txt')
lp = login_pass.read()
ln = login_name.read()
cpucount = os.cpu_count()
print("FishOS Terminal [Version 0.1]")
print("System>>> Make sure you've already done psh -i")
def listShow():
    subprocess.run(["dir"], shell=True)

def openWindowsCmd():
        return subprocess.run(["cmd"])

def showLista(x): # defining showList function whit parameter X
        subprocess.run(["dir", x], shell=True) # code

def pingCmd(x):
    subprocess.run(["ping",x])

def pingT(x):
    subprocess.run(["ping","-t",x])

while True:
    code = input("")
    if code == 'ping':
        host = input(">>> Enter the website/IP to ping: ")
        pingCmd(host)


    if code == 'ping -i':
        print("""
---------------------FISHOS PING COMMANDS---------------------
ping: ping a webstie or an ip
ping -i: get ping info
ping -w: continue pinging a website or an ip
""")
    if code == 'ping -w':
        try:
            host2 = input(">>> Enter the website/IP to ping: ")
            pingT(host2)
        except KeyboardInterrupt:
            code
    
    if code == 'psh -i':
        print("""
This is the FishOS Terminal
try to type ping -i or powershell or date to see what happends
--ATTENTION--
PLEASE MAKE SURE THAT YOU'RE THE ONLY ONE USING THIS TERMINAL
IF YOU TYPE IN SOME COMMANDS YOU MAY DESTROY YOU COMPUTER
WE WON'T GIVE A REFOUND OF THE DAMAGE
EVERYTHING IS AT YOUR OWN RISK
OTHERWISE DO NOT USE THE TERMINAL
        """)

    if code == 'lcl -ho':
        print(">>> Your local IP is " + hostip)
        print(">>> Your hostname is " + hostname)

    if code == 'date':
        print(">>> Local date: " + time.strftime("%m/%d/%y"))

    if code == 'list':
        listShow()
    
    if code == 'list -a':
        dirlist2 = input("Path>>> ")
        showLista(dirlist2)

    if code == 'shw -m -p':
        echo = input(">>> Input what do you want to print: ")
        print(echo)

    if code == 'exit':
        os.startfile('home.py')
        os.close('terminal.py')

    if code == 'sys -i':
        print("This os is maked by a person")

    if code == 'powershell':
        openWindowsCmd()

    if code == 'lcl -us':
        print("Name: " + ln)
        print("Password: " + lp)
    
    if code == 'lcl -us -c':
        try:
            print("""
[1] Change username
[2] Change password
            """)
            choose = input("[?]: ")
            if choose == '1':
                choose2 = input("Insert new username: ")
                namechange = open('user/username.txt', 'w')
                namechange.write(choose2)
                namechange.close()
            
            if choose == '2':
                choose3 = input("Insert new password: ")
                passchange = open('password.txt', 'w')
                passchange.write(choose3)
                passchange.close()
        except KeyboardInterrupt:
            pass

    else:
        # print("Command not found")
        pass
