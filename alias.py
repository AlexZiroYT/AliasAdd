__author__ = "AlexZiroYT"

import os

add_answ = ["1", "add", "new"]
del_answ = ["2", "del", "delete", "remove"]

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
    
def start():        
    print('''Hi!
This script will help you create an alternative to the command for windows!
You can replace the command with another text!
For example, instead of "dir", make "ls" as on Linux.

[1] Add Alias
[2] Delete Alias
To close: ctrl+c
''')
    answer = input(">>> ")
    if(answer in settings_answ):
        settings()
    if(answer in add_answ):
        add()
    if(answer in del_answ):
        delete()  
start()
