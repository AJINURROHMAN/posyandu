from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window



# Load the KV file for this screen
Builder.load_file('profil.kv')
Builder.load_file('logout.kv')
Builder.load_file('login.kv')


class ProfilScreen(Screen):
    def go_to_logout(self):
        self.manager.current = 'logout_screen'  # Ganti ke screen beranda

class BerandaScreen(Screen):
    pass

class LogoutScreen(Screen):
    pass
class LoginScreen(Screen):
    pass

class TestApp(App):
    def build(self):
        sm = ScreenManager()

        # Tambahkan screen ke dalam ScreenManager
        sm.add_widget(ProfilScreen(name='profil_screen'))
        sm.add_widget(BerandaScreen(name='beranda_screen'))
        sm.add_widget(LogoutScreen(name='logout_screen'))  # Menambahkan screen ke ScreenManager
        sm.add_widget(LoginScreen(name='login_screen'))  # Menambahkan screen ke ScreenManager

        # Set screen default
        sm.current = 'profil_screen'
        
        return sm

if __name__ == '__main__':
    Window.size = (360, 640)
    TestApp().run()
