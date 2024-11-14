from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from database import Database  # Pastikan Anda mengimpor kelas Database dari file database Anda

class ProfilScreen(Screen):
    sidebar_visible = False  # Untuk melacak status tampilan sidebar

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database()  # Inisialisasi database
        self.username = ""  # Menyimpan username yang sedang login
        self.user_data = {}  # Menyimpan data pengguna

    def on_enter(self):
        # Setiap kali masuk ke layar ini, pastikan sidebar dalam keadaan tersembunyi
        self.hide_sidebar()
        self.load_user_data()  # Ambil data pengguna saat memasuki layar

    def load_user_data(self):
        # Ambil data pengguna berdasarkan username
        if self.username:  # Pastikan username tidak kosong
            self.user_data = self.db.get_user_data(self.username)
            if self.user_data:
                # Tampilkan data pengguna di label
                self.ids.username_label.text = f"Username: {self.user_data.get('username', 'Tidak ada')}"
                self.ids.password_label.text = f"Password: {self.user_data.get('password', 'Tidak ada')}"
            else:
                print("Data pengguna tidak ditemukan.")

    def set_username(self, username):
        self.username = username  # Atur username
        self.load_user_data()  # Muat data pengguna setelah username diatur

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

    def logout(self):
        # Fungsi yang dijalankan saat pengguna logout
        self.username = ""  # Kosongkan username
        self.user_data = {}  # Kosongkan data pengguna
        self.show_logout_popup()  # Tampilkan pesan logout berhasil

    def show_logout_popup(self):
        # Buat layout pop-up
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=10, size_hint=(None, None), size=(300, 200))
        
        # Teks pesan
        message_label = Label(text="Logout berhasil!", halign='center', valign='middle', text_size=(280, None), color=(0, 0, 0, 1))
        close_button = Button(text="OK", size_hint=(0.5, None), height=40, pos_hint={'center_x': 0.5}, background_color=(0.1, 0.6, 0.1, 1), color=(1, 1, 1, 1))
        
        # Tambahkan komponen ke layout pop-up
        popup_layout.add_widget(message_label)
        popup_layout.add_widget(close_button)

        # Buat dan tampilkan pop-up
        popup = Popup(title="Pesan", content=popup_layout, size_hint=(None, None), size=(300, 200), auto_dismiss=False)
        close_button.bind(on_release=popup.dismiss)  # Tutup pop-up saat tombol OK diklik
        popup.open()
