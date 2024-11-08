from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation

from bumil import BumilScreen

# Memuat file .kv untuk tampilan
Builder.load_file('tambah_bumil.kv')  # Memuat file .kv untuk layar tambahan
Builder.load_file('bumil.kv')  # Memuat file .kv untuk layar balita

# Kelas untuk tampilan TambahScreen
class TambahScreen(Screen):
    pass

class BalitaScreen(Screen):
    pass

class TambahBumilScreen(Screen):
    pass

# Kelas utama aplikasi
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TambahBumilScreen(name='tambah_bumil_screen'))  # Menambahkan TambahScreen ke ScreenManager
        sm.add_widget(BumilScreen(name='bumil_screen'))  # Menambahkan BalitaScreen ke ScreenManager
        
        return sm

# Menjalankan aplikasi
if __name__ == '__main__':
    Window.size = (360, 640)  # Mengatur ukuran jendela
    MyApp().run()
