from kivy.uix.tabbedpanel import TabbedPanel
from libs.components.database import *
from libs.components.swiper import SwiperOne
from kivymd.uix import *

class DownPanel(TabbedPanel):
    def exit(self):
        return True
    def search(self):
        name = self.search_input.text
        file = open('user.txt')
        # flag=False
        try:

            with db:
                us = User.get(User.login==name)
            self.user_name.text="Зарегистрирован в приложении"

        except Exception as e:
            self.user_name.text="Пока никого не нашли"
            print('ppp')

    def dei(self):
        pass
    