
from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from libs.screens.homePage import HomePage

 
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

class MainApp(MDApp):
    def build(self):
        Window.size=[300,600]
        self.load_all_kv_files()
        return HomePage()
    
    def load_all_kv_files(self):
        Builder.load_file('libs/screens/homePage.kv')
        Builder.load_file('libs/screens/formsManager.kv')
        Builder.load_file('libs/screens/tabs.kv')
        
if __name__ == '__main__':
    MainApp().run()
    
