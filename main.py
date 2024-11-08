from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.core.window import Window
from database import Database

# Mengatur ukuran window menjadi 360x640
Window.size = (360, 640)

# Load file login.kv dan file-file lainnya (jika ada)
Builder.load_file('login.kv')
Builder.load_file('profil.kv')
Builder.load_file('dashboard.kv')
Builder.load_file('logout.kv')
Builder.load_file('tambah.kv')
Builder.load_file('balita.kv')
Builder.load_file('dashlog.kv')
Builder.load_file('bumil.kv')

from login import LoginScreen
from logout import LogoutScreen
from dashlog import DashlogScreen
from dashboard import DashboardScreen
from balita import BalitaScreen
from tambah import TambahScreen
from profil import ProfilScreen
from bumil import BumilScreen
from tambah_bumil import TambahBumilScreen

class MainApp(App):
    def __init__(self,):
        super().__init__()
        self.user = None  # Menyimpan username yang sedang login
        self.database = Database()  # Inisialisasi objek database di sini

    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login_screen'))   # Nama screen untuk login
        sm.add_widget(ProfilScreen(name='profil_screen'))  # Nama screen untuk profil
        sm.add_widget(DashboardScreen(name='dashboard_screen'))  # Nama screen untuk beranda
        sm.add_widget(TambahScreen(name='tambah_screen'))
        sm.add_widget(BalitaScreen(name='balita_screen'))
        sm.add_widget(LogoutScreen(name='logout_screen'))
        sm.add_widget(DashlogScreen(name='dashlog_screen'))
        sm.add_widget(BumilScreen(name='bumil_screen'))
        sm.add_widget(TambahBumilScreen(name='tambah_bumil_screen'))
        return sm

if __name__ == '__main__':
    MainApp().run()
