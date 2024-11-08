from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation

# Definisikan layar LogoutScreen
class LogoutScreen(Screen):
    class LogoutScreen(Screen):
    def on_enter(self):
        # Mengatur opacity gambar menjadi 0 sebelum animasi dimulai
        self.ids.logout_image.opacity = 0
        # Jalankan animasi fade-in
        anim = Animation(opacity=1, duration=1)  # Durasi 1 detik
        anim.start(self.ids.logout_image)
        
        # Bind animasi fade-out setelah fade-in selesai
        anim.bind(on_complete=lambda *args: self.fade_out())

    def fade_out(self):
        # Animasi fade out
        anim = Animation(opacity=0, duration=1)  # Durasi 1 detik
        anim.start(self.ids.logout_image)


class LoginScreen(Screen):
    pass

class LogoutApp(App):
    def build(self):
        # Muat file KV
        Builder.load_file('logout.kv')
        Builder.load_file('login.kv')

        # Buat ScreenManager untuk mengelola layar
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(LogoutScreen(name='logout_screen'))  # Menambahkan screen ke ScreenManager
        sm.add_widget(LoginScreen(name='login_screen'))  # Menambahkan screen ke ScreenManager
        
        # Tampilkan layar logout_screen sebagai layar awal
        sm.current = 'logout_screen'
        return sm

    def go_to_login(self):
        # Fungsi untuk memindahkan ke layar login (bisa disesuaikan dengan aplikasi login Anda)
        print("Kembali ke layar login...")
        # Misalnya, kembalikan ke layar login di ScreenManager
        # self.root.current = 'login_screen'

if __name__ == '__main__':
    Window.size = (360, 640)
    LogoutApp().run()
