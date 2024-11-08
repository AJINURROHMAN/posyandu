from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

# Memuat file .kv untuk tampilan
Builder.load_file('tambah.kv')  # Memuat file .kv untuk layar tambahan
Builder.load_file('balita.kv')  # Memuat file .kv untuk layar tambahan

# Kelas untuk tampilan TambahScreen
class TambahScreen(Screen):
    pass
class BalitaScreen(Screen):
    pass

# Kelas utama aplikasi
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TambahScreen(name='tambah_screen'))  # Menambahkan TambahScreen ke ScreenManager
        sm.add_widget(BalitaScreen(name='balita_screen'))  # Menambahkan TambahScreen ke ScreenManager
        
        return sm

# Menjalankan aplikasi
if __name__ == '_main_':
    Window.size = (360, 640)  # Mengatur ukuran jendela
    MyApp().run()       