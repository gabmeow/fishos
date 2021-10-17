import os
import time

print("""

████████╗███████╗██╗░░██╗████████╗░░░░░░███████╗██████╗░██╗████████╗░█████╗░██████╗░
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝░░░░░░██╔════╝██╔══██╗██║╚══██╔══╝██╔══██╗██╔══██╗
░░░██║░░░█████╗░░░╚███╔╝░░░░██║░░░█████╗█████╗░░██║░░██║██║░░░██║░░░██║░░██║██████╔╝
░░░██║░░░██╔══╝░░░██╔██╗░░░░██║░░░╚════╝██╔══╝░░██║░░██║██║░░░██║░░░██║░░██║██╔══██╗
░░░██║░░░███████╗██╔╝╚██╗░░░██║░░░░░░░░░███████╗██████╔╝██║░░░██║░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░░░░░░╚══════╝╚═════╝░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
""")

fileopener = open('disk/D/Text Editor/new.txt')
filereader = fileopener.read()

print("Your recent files: " + filereader)

print("""
[1] Make a new file
[2] Delete a file
[3] Exit
""")

choose = input("[?]: ")

if choose == '1':
    print("Type something to put in the file")
    typein = input("")
    with open('disk/D/Text Editor/new.txt', 'w') as f:
        f.writelines(typein)
        os.open('home.py')
        os.open('edit.py')

if choose == '3':
    os.startfile('home.py')
    os.close('edit.py')
