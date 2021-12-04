__author__ = "AlexZiroYT"

import os

settings_answ = ["1", "settings", "sett", "set"]
add_answ = ["2", "add", "new"]
del_answ = ["3", "del", "delete", "remove"]

def delete():
    print('''CAUTION!
This function can delete important system files!
If you are afraid of making a mistake, it is better to delete the alias file YOURSELF!
Path: C:\Windows (the alias file is named the same as it was called when it was created)
''')
    alias = input("Alias name >>> ")
    os.remove("c:/windows/" + alias + ".bat")
    start()

def add():
    original = input("Original command >>> ")
    new = input("Alias (New command) >>> ")
    alias = open("C:/Windows/" + new +".bat", "a")
    alias.write(original)
    start()
    
def settings():
    print('''
Welcome Interface:
[1] Turn everything on. (greeting text and list of actions)
[2] Only a list of actions
[3] Turn off everything
''')
    hiA = input(">>> ")
    if(hiA == "1"):
        hiSet = open("settings/hi.txt", "w")
        hiSet.write("1")
        hiSet.close()
    elif(hiA == "2"):
        hiSet = open("settings/hi.txt", "w")
        hiSet.write("2")
        hiSet.close()
    elif(hiA == "3"):
        hiSet = open("settings/hi.txt", "w")
        hiSet.write("3")
        hiSet.close()
    start()
    
def start():
    with open("settings/hi.txt") as file:
        hiSettings = file.read()
        
        if (hiSettings == "1"):
            with open("settings/hi/hiAll.txt") as file:
                hi = file.read()
        elif(hiSettings == "2"):
            with open("settings/hi/hiOnlyActions.txt") as file:
                hi = file.read()
        elif(hiSettings == "3"):
            with open("settings/hi/hiOff.txt") as file:
                hi = file.read()          
    print(hi)
    answer = input(">>> ")
    if(answer in settings_answ):
        settings()
    if(answer in add_answ):
        add()
    if(answer in del_answ):
        delete()  
start()