from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen , FadeTransition
from kivy.lang import Builder
from kivy.core.window import Window 
from kivy.animation import Animation 
from kivy.clock import Clock

# Mengatur ukuran window menjadi 360x640
Window.size = (360, 640)

# Load file login.kv dan file-file lainnya (jika ada)
Builder.load_file('login.kv')
Builder.load_file('beranda.kv')
Builder.load_file('profil.kv')
Builder.load_file('menu.kv')
Builder.load_file('berhasil.kv')
Builder.load_file('dashboard.kv')
Builder.load_file('logout.kv')
Builder.load_file('tambah.kv')
Builder.load_file('balita.kv')


class LoginScreen(Screen):
    def login(self):
        # Logic to navigate to another screen
        if self.ids.username.text == 'admin' and self.ids.password.text == 'admin':
            self.manager.current = 'login_screen'  # Ganti ke 'beranda_screen'
        else:
            print("Invalid credentials")

class ProfilScreen(Screen):
    pass
class BerandaScreen(Screen):
    def on_enter(self):
        # Animasi pertama untuk memunculkan top_box dengan fade-in dan geser dari atas
        anim_appear = Animation(opacity=1, pos_hint={'': 3}, d=1)
        
        # Animasi kedua untuk menunggu selama 0.5 detik lalu menghilangkan top_box
        anim_disappear = Animation(opacity=0, d=1)

        # Jalankan animasi pertama
        anim_appear.start(self.ids.top_box)
        
        # Setelah animasi pertama selesai, tunggu 0.5 detik lalu jalankan animasi menghilang
        anim_appear.bind(on_complete=lambda *x: anim_disappear.start(self.ids.top_box))
class DashboardScreen(Screen):
    def on_enter(self):
        # Menampilkan popup saat layar terbuka
        self.show_popup()

    def show_popup(self):
        # Mengatur popup agar mulai dengan opacity 0 (transparan)
        self.ids.popup_box.opacity = 1

        # Animasi untuk fade-in (muncul) selama 1 detik
        anim_appear = Animation(opacity=1, d=1.0)
        anim_appear.start(self.ids.popup_box)

        # Setelah animasi fade-in selesai, tunggu 1 detik, lalu jalankan fade-out
        Clock.schedule_once(self.hide_popup, 1.5)  # Total 1 detik muncul + 0.5 detik untuk fade-in

    def hide_popup(self, dt):
        # Animasi untuk fade-out (menghilang) selama 1 detik
        anim_disappear = Animation(opacity=0, d=1.0)
        anim_disappear.start(self.ids.popup_box)
class BerhasilScreen(Screen):
    pass
class BerhasilScreen(Screen):
    def on_enter(self):
        # Animasi pertama untuk memunculkan top_box dengan fade-in dan geser dari atas
        anim_appear = Animation(opacity=1, pos_hint={'top': 1}, d=1)
        
        # Animasi kedua untuk menunggu selama 0.5 detik lalu menghilangkan top_box
        anim_disappear = Animation(opacity=0, d=1)

        # Jalankan animasi pertama
        anim_appear.start(self.ids.top_box)
        
        # Setelah animasi pertama selesai, tunggu 0.5 detik lalu jalankan animasi menghilang
        anim_appear.bind(on_complete=lambda *x: anim_disappear.start(self.ids.top_box))
class MenuScreen(Screen):
    pass
class LogoutScreen(Screen):
    pass
        
class TambahScreen(Screen):
    pass
class BalitaScreen(Screen):
    pass


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login_screen'))   # Nama screen untuk login
        sm.add_widget(ProfilScreen(name='profil_screen'))  # Nama screen untuk profil
        sm.add_widget(BerandaScreen(name='beranda_screen'))  # Nama screen untuk beranda
        sm.add_widget(MenuScreen(name='menu_screen'))  # Nama screen untuk beranda
        sm.add_widget(BerhasilScreen(name='berhasil_screen'))  # Nama screen untuk beranda
        sm.add_widget(DashboardScreen(name='dashboard_screen'))  # Nama screen untuk beranda
        sm.add_widget(TambahScreen(name='tambah_screen'))
        sm.add_widget(BalitaScreen(name='balita_screen'))
        sm.add_widget(LogoutScreen(name='logout_screen'))
        return sm


if __name__ == '__main__':
    MainApp().run()
