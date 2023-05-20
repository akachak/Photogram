from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from libs.screens.tabs import DownPanel
from libs.components.database import db, sql

class InForm(Screen):
    def biba(self):
        fileSave = open('save.txt')
        try:
            s = fileSave.readlines()
            p = s[0]
            p = p[:-1]
            self.inLogin.text = p
            self.inPassword.text = s[1]
        except Exception as e:
            print('piska')
        
        fileSave.close()
    def check(self, value):
        log = self.inLogin.text
        pas = self.inPassword.text
        save = value
        
        
        flagUser=False
        for value in sql.execute("SELECT * FROM users"):
            if(value[0]==log and value[1]==pas):
                flagUser=True
        

        if(flagUser):
            fileUser = open('user.txt', 'w+')
            fileUser.seek(0)
            fileUser.write(log)
            fileUser.close()
            if(save):
                fileSave = open('save.txt', 'w+')
                fileSave.seek(0)
                fileSave.write(log)
                fileSave.write('\n')
                fileSave.write(pas)
                fileSave.close()
            else:
                fileSave = open('save.txt', 'w+')
                fileSave.seek(0)
                fileSave.close()
                self.inLogin.text=''
                self.inPassword.text=''
            return True
        else:
            return False


class RegForm(Screen):
    def reg(self):
        log= self.regLogin.text
        pas= self.regPassword.text
        flagLogin = False
        for value in sql.execute("SELECT * FROM users"):
            if (value[0]==log):
                flagLogin=True

        if(log == '' or pas == ''):
            flagLogin=True

        if(not(flagLogin)):
            if(pas==self.regRetPassword.text):
                sql.execute(f"INSERT INTO users VALUES(?, ?)", (log,pas))
                db.commit()
                return True
            else:
                self.regRetPassword.text=''
                return False
        else:
            self.regLogin.text=''
            return False


class WTFForm(Screen):
    pass

class WindowManager(ScreenManager):
    pass