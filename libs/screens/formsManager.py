from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from libs.screens.tabs import DownPanel
from libs.components.database import db, sql

class InForm(Screen):
    def check(self):
        log = self.inLogin.text
        pas = self.inPassword.text
        for value in sql.execute("SELECT * FROM users"):
            if((value[0]==log) and (value[1]==pas)):
                return True
            else:
                return False

class RegForm(Screen):
    def reg(self):
        log= self.regLogin.text
        pas= self.regPassword.text
        sql.execute("SELECT login FROM users")
        if sql.fetchone() is None:
            if(pas==self.regRetPassword.text):
                sql.execute(f"INSERT INTO users VALUES(?,?)",(log, pas))
                db.commit()
                return True
            else:
                return False
        else:
            return False


class WTFForm(Screen):
    pass

class WindowManager(ScreenManager):
    pass