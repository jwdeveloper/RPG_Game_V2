import json
import os
from datetime import datetime


class User(object):

    def __init__(self):
        self.login = ""
        self.password = ""
        self.character = ""

class UserManager:
    users = []
    fileName = "usersData.json"

    def addUser(self, login, password):
        user = User()
        user.login = login
        user.password = password
        self.users.append(user)
        self.save()
        return user

    def findUser(self, login):

        for user in self.users:
            if user.login == login:
                return user
        return None

    def load(self):
        mode = 'r+' if os.path.exists(self.fileName) else 'a+'
        with open(self.fileName, mode) as file:
            try:
                if mode == "a+":
                    self.users = []
                    return

                dictioanry = json.loads(file.read())

                for obj in dictioanry:
                    user = User()
                    for key in obj:
                        setattr(user, key, obj[key])
                    self.users.append(user)
            except Exception as error:
                print(error)
                self.users = []

    def save(self):
        usersJson = json.dumps(self.users, indent=5,default=lambda o: o.__dict__)
        with open(self.fileName, "a+") as outfile:
            outfile.seek(0)
            outfile.truncate()
            outfile.write(usersJson)
    def login(self):
        print("Witaj w grze, wpisz swoje dane logowania lub załóż nowe konto")
        l = input("Login: ")
        p = input("Password: ")
        u = self.findUser(l)
        if u == None:
            user=self.addUser(l,p)
            print("Założono nowego użytkownika")
            self.pickcharacter(user)
            return user
        else:
            if u.password==p:
                print("Zalogowano pomyślnie")
                return u
            else:
                print("Niepoprawne hasło lub nazwa użytkownika")
                self.login()
    def pickcharacter(self,u):
        print("Wybierz postać:")
        print("0. Barbarzyńca")
        print("1. Bard")
        print("2. Druid")
        print("3. Mag")
        print("4. Nekromanta")
        print("5. Paladyn")
        print("6. Lucznik")
        print("7. Złodziej")
        postacie=[]
        postacie.append("Barbarian")
        postacie.append("Bard")
        postacie.append("Druid")
        postacie.append("Mage")
        postacie.append("Necromancer")
        postacie.append("Paladyn")
        postacie.append("Ranger")
        postacie.append("Rogue")
        postac = int(input())
        postac = postacie[postac]
        if postac!=None:
            u.character=postac
            print("Wybrano postać: ",postac)
            self.save()
        else:
            print("Wybierz dostępną postać")