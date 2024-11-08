from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang import Builder
from kivy.core.window import Window

# Load the KV file for this screen
Builder.load_file('login.kv')
Builder.load_file('logout.kv')
Builder.load_file('profil.kv')


class LogoutScreen(Screen):
    pass
class ProfilScreen(Screen):
    pass

class LoginScreen(Screen):
    
    def build(self):
        # Muat file KV
        Builder.load_file('logout.kv')
        Builder.load_file('login.kv')
        Builder.load_file('profil.kv')

        # Buat ScreenManager untuk mengelola layar
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(LogoutScreen(name='logout_screen'))  # Menambahkan screen ke ScreenManager
        sm.add_widget(LoginScreen(name='login_screen'))  # Menambahkan screen ke ScreenManager
        sm.add_widget(ProfilScreen(name='profil_screen'))  # Menambahkan screen ke ScreenManager
        return sm    
    
    def login(self):
        # Logic to navigate to another screen
        if self.ids.username.text == 'admin' and self.ids.password.text == 'admin':
            self.manager.current = 'beranda_screen'  # Ganti ke 'beranda_screen'
        else:
            print("Invalid credentials")
