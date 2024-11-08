from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

# Memuat file .kv
Builder.load_file('balita.kv')
Builder.load_file('menu.kv')

class BalitaScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class LogoutScreen(Screen):
    pass

class TambahScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        # Membuat ScreenManager
        sm = ScreenManager()
        sm.add_widget(BalitaScreen(name='balita_screen'))
        sm.add_widget(MenuScreen(name='menu_screen'))
        sm.add_widget(LogoutScreen(name='logout_screen'))
        sm.add_widget(TambahScreen(name='tambah_screen'))
        return sm

if __name__ == "__main__":  # Perbaikan pada kondisi ini
    Window.size = (360, 640)  # Menetapkan ukuran jendela
    MyApp().run()  # Menjalankan aplikasi
