from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import RoundedRectangle
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
import random



# Subclass ButtonBehavior untuk menambahkan klik ke BoxLayout
class ClickableBox(ButtonBehavior, BoxLayout):
    pass

class BumilScreen(Screen):
    sidebar_open = False  # Status sidebar, tertutup pada awalnya

    def on_enter(self):
        # Setiap kali masuk ke layar ini, sembunyikan sidebar dan muat data balita
        self.hide_sidebar()
        self.load_data()  # Memanggil fungsi untuk memuat data balita dari Firebase

    def load_data(self):
        # Bersihkan data sebelumnya
        self.ids.data_container.clear_widgets()
        database = App.get_running_app().database
        data_bumil = database.db.child("bumil").child("user1").get()
        print('profil')
        

        # Warna bergantian untuk setiap data balita
        colors = [
            get_color_from_hex("#82B1FF"),  # Biru Muda Terang
            get_color_from_hex("#FFD180") , # Peach Terang
            get_color_from_hex("#FF9E80") , # Merah Muda Salmon
            get_color_from_hex("#B9F6CA"),  # Hijau Mint Cerah
            get_color_from_hex("#FFEB3B")  # Kuning Cerah
        ]

        if data_bumil is not None and data_bumil.each() is not None:
            for index, balita in enumerate(data_bumil.each()):
                info = balita.val()
                if all(key in info for key in ['nama', 'suami','alamat', 'telepon']):
                    # Buat BoxLayout untuk setiap data balita
                    container = BoxLayout(orientation='vertical', padding=10, size_hint_y=None, height=170)
                    container.bumil_info = info  # Menyimpan info balita untuk diakses saat diklik

                    # Tombol di dalam BoxLayout dengan warna latar berbeda
                    button = Button(
                        text=f"[b][/b]\n {info['nama']}\n[b][/b] {info['alamat']}",
                        size_hint_y=None,
                        height=150,
                        font_size=25,
                        color=(1, 1, 1, 1),  # Warna teks putih
                        background_normal='',  # Menghilangkan background image default
                        background_color=colors[index % len(colors)],  # Warna bergantian
                        markup= True
                        
                    )
                    button.bind(on_release=self.show_details)  # Bind ke fungsi show_details untuk event klik
                    button.balita_info = info  # Menyimpan info balita di button

                    # Tambahkan tombol ke dalam container
                    container.add_widget(button)

                    # Tambahkan container ke data_container utama
                    self.ids.data_container.add_widget(container)

                    # Tambahkan pemisah setelah setiap BoxLayout
                    separator = Label(size_hint_y=None, height=2)
                    self.ids.data_container.add_widget(separator)
                else:
                    print("Data bumil tidak lengkap:", info)  # Debugging jika data bumil tidak lengkap
        else:
            # Jika tidak ada data balita yang ditemukan, tampilkan pesan di layar
            self.ids.data_container.add_widget(Label(text="Tidak ada data bumil yang ditemukan.", color=(0, 0, 0, 1)))
            print("Tidak ada data balita atau data_bumil adalah None")  # Debugging untuk memastikan data diambil

    def show_details(self, instance):
        """Menampilkan popup dengan detail informasi bumil yang lebih rapi dan tombol 'Tutup' di tengah bawah."""
        info = instance.balita_info

        # Membuat layout utama untuk konten popup
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=[20, 20, 20, 10])

        # Membuat layout untuk teks informasi balita
        text_layout = BoxLayout(orientation='vertical', spacing=10)

        # Menambahkan setiap detail informasi balita sebagai Label terpisah
        text_layout.add_widget(Label(
            text=f"Nama:\n{info['nama']}", color=(1, 1, 1, 1), font_size=18, halign="center", valign="middle", text_size=(360, None)
        ))
        text_layout.add_widget(Label(
            text=f"Suami:\n{info['suami']}", color=(1, 1, 1, 1), font_size=18, halign="center", valign="middle", text_size=(360, None)
        ))
        text_layout.add_widget(Label(
            text=f"Alamat:\n{info['alamat']}", color=(1, 1, 1, 1), font_size=18, halign="center", valign="middle", text_size=(360, None)
        ))
        text_layout.add_widget(Label(
            text=f"Telepon:\n{info['telepon']}", color=(1, 1, 1, 1), font_size=18, halign="center", valign="middle", text_size=(360, None)
        ))

        # Menambahkan layout teks ke layout utama
        main_layout.add_widget(text_layout)

        # Membuat layout untuk tombol dan menempatkannya di tengah bawah dengan styling
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=60)
        button_layout.add_widget(BoxLayout())  # Spacer untuk pusat tombol

        # Membuat tombol "Tutup" dengan ukuran dan warna yang disesuaikan
        close_button = Button(
            text="Tutup",
            size_hint=(None, None),
            width=120,
            height=45,
            background_normal='',  # Menghilangkan background default
            background_color=(0.2, 0.6, 0.8, 1),  # Warna background tombol
            color=(1, 1, 1, 1),  # Warna teks tombol
            font_size=18
        )
        close_button.bind(on_release=lambda *args: popup.dismiss())  # Menutup popup saat tombol ditekan
        button_layout.add_widget(close_button)

        button_layout.add_widget(BoxLayout())  # Spacer untuk pusat tombol

        # Menambahkan layout tombol ke layout utama
        main_layout.add_widget(button_layout)

        # Membuat popup dan menampilkannya dengan layout utama
        popup = Popup(
            title="Detail Bumil",
            content=main_layout,
            size_hint=(None, None),
            size=(400, 450),
            auto_dismiss=True
        )
        popup.open()

    def search_data(self, search_text):
        """Mencari data bumil berdasarkan nama."""
        self.ids.data_container.clear_widgets()
        database = App.get_running_app().database
        data_bumil = database.db.child("bumil").child("user1").get()

        # Daftar warna untuk tombol
        colors = [
            get_color_from_hex("#82B1FF"),  # Biru Muda Terang
            get_color_from_hex("#FFD180"),  # Peach Terang
            get_color_from_hex("#FF9E80"),  # Merah Muda Salmon
            get_color_from_hex("#B9F6CA"),  # Hijau Mint Cerah
            get_color_from_hex("#FFEB3B")   # Kuning Cerah
        ]

        if data_bumil is not None and data_bumil.each() is not None:
            for index,balita in data_bumil.each():
                info = balita.val()
                if all(key in info for key in ['nama', 'suami', 'alamat', 'telepon']):
                    if search_text.lower() in info['nama'].lower():  # Pencarian berdasarkan nama
                        container = BoxLayout(orientation='vertical', padding=10, size_hint_y=None, height=170)
                        container.balita_info = info

                        # Pilih warna acak dari daftar
                       

                        button = Button(
                            text=f"[b]{info['nama']}[/b]\n[b]{info['alamat']}[/b]",
                            size_hint_y=None,
                            height=150,
                            font_size=20,
                            color=(1, 1, 1, 1),
                            background_normal='',
                            background_color=colors[index % len(colors)], # Gunakan warna acak
                            markup=True
                        )
                        button.bind(on_release=self.show_details)
                        button.bumil_info = info

                        container.add_widget(button)
                        self.ids.data_container.add_widget(container)

                        separator = Label(size_hint_y=None, height=2)
                        self.ids.data_container.add_widget(separator)

        else:
            self.ids.data_container.add_widget(Label(text="Tidak ada data bumil yang ditemukan.", color=(0, 0, 0, 1)))
            
    def update_rect(self, instance, value):
        # Perbarui posisi dan ukuran Rectangle sesuai ukuran BoxLayout
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def toggle_sidebar(self):
        # Jika sidebar sedang terlihat, sembunyikan; jika tersembunyi, tampilkan
        if self.sidebar_open:
            self.hide_sidebar()
        else:
            self.show_sidebar()

    def show_sidebar(self):
        # Menggunakan animasi untuk menampilkan sidebar
        anim = Animation(x=0, duration=0.3)
        anim.start(self.ids.sidebar)
        self.sidebar_open = True

    def hide_sidebar(self):
        # Menggunakan animasi untuk menyembunyikan sidebar
        anim = Animation(x=-self.ids.sidebar.width, duration=0.3)
        anim.start(self.ids.sidebar)
        self.sidebar_open = False
