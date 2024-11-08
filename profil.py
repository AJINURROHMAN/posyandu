from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation

class ProfilScreen(Screen):
    sidebar_visible = False  # Untuk melacak status tampilan sidebar

    def toggle_sidebar(self):
        # Jika sidebar sedang terlihat, sembunyikan; jika tersembunyi, tampilkan
        if self.sidebar_visible:
            self.hide_sidebar()
        else:
            self.show_sidebar()

    def show_sidebar(self):
        # Menggunakan animasi untuk menampilkan sidebar
        anim = Animation(x=0, duration=0.3)  # Memindahkan sidebar ke posisi terlihat
        anim.start(self.ids.sidebar)
        self.sidebar_visible = True

    def hide_sidebar(self):
        # Menggunakan animasi untuk menyembunyikan sidebar
        anim = Animation(x=-self.ids.sidebar.width, duration=0.3)  # Memindahkan sidebar keluar layar
        anim.start(self.ids.sidebar)
        self.sidebar_visible = False

    def on_enter(self):
        # Setiap kali masuk ke layar ini, pastikan sidebar dalam keadaan tersembunyi
        self.hide_sidebar()