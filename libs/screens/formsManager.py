from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from libs.screens.tabs import DownPanel
from libs.components.database import *

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
        with db:
            try:
                ge = User.get(User.login==log)
                if (ge.password==pas):
                    flagUser=True
            except Exception as e:
                    flagUser = False
                    print('AAAAA')
        

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
        with db:
            try:
                User.get(User.login==log)
                flagLogin=True
                print("MAYBE")
            except Exception as e:
                flagLogin=False
                print('piska')
            
        if(log == '' or pas == ''):
            flagLogin=True

        if(not(flagLogin)):
            if(pas==self.regRetPassword.text):
                with db:
                    newUser = User.create(login=log, password = pas)
                    
                fileUser = open('user.txt', 'w+')
                fileUser.seek(0)
                fileUser.write(newUser.login)
                fileUser.close()
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