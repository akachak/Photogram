from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from libs.screens.tabs import DownPanel
# from libs.components.database import db

class InForm(Screen):
    def check(self):
        return True

class RegForm(Screen):
    pass

class WTFForm(Screen):
    pass

class WindowManager(ScreenManager):
    pass