from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import QueryDict
from kivymd.toast import toast
from kivy.utils import QueryDict, rgba
from kivy.metrics import dp, sp


class LoginApplication(MDApp):

    fonts = QueryDict()
    fonts.size = QueryDict()
    fonts.size.h1 = dp(24)
    fonts.size.h2 = dp(22)
    fonts.size.h3 = dp(18)
    fonts.size.h4 = dp(16)
    fonts.size.h5 = dp(14)
    fonts.size.h6 = dp(12)

    fonts.heading = 'assets/fonts/feather/feather.ttf'
    fonts.subheading = 'assets/fonts/Lobster/Lobster-Regular.ttf'
    fonts.body = 'assets/fonts/Roboto/Roboto-Black.ttf'
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.manager = ScreenManager()
        self.manager.add_widget(Builder.load_file("login.kv"))
        self.manager.add_widget(Builder.load_file("dashboard.kv"))
        self.manager.get_screen('login').ids.lg_btn.on_release = self.on_login
        #self.manager.get_screen('home').ids.dash_home_btn.on_release = self.go_dash

        return self.manager

    def on_start(self):
        self.manager.current = 'login'

    def on_login(self):
        user = self.manager.get_screen('login').ids.user.text
        password = self.manager.get_screen('login').ids.password.text
        self.manager.current = 'home'

    def go_dash(self):
        self.manager.current = 'home'

class ScaleBox(MDBoxLayout):
    scale = NumericProperty(1)

LoginApplication().run()
