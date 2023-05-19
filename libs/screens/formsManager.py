from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from libs.screens.tabs import DownPanel

class InForm(Screen):
    def check(self):
        return True

class RegForm(Screen):
    pass

class WTFForm(Screen):
    pass

class WindowManager(ScreenManager):
    pass