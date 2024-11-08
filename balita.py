from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.uix.behaviors import ButtonBehavior


# Subclass ButtonBehavior untuk menambahkan klik ke BoxLayout
class ClickableBox(ButtonBehavior, BoxLayout):
    pass

class BalitaScreen(Screen):
    sidebar_open = False  # Status sidebar, tertutup pada awalnya

    def on_enter(self):
        # Setiap kali masuk ke layar ini, sembunyikan sidebar dan muat data balita
        self.hide_sidebar()
        self.load_data()  # Memanggil fungsi untuk memuat data balita dari Firebase

    def load_data(self):
        # Bersihkan data sebelumnya
        self.ids.data_container.clear_widgets()
        database = App.get_running_app().database
        data_balita = database.db.child("balita").child("user1").get()

        # Periksa apakah data_balita bukan None dan terdapat data
        if data_balita is not None and data_balita.each() is not None:
            for index, balita in enumerate(data_balita.each()):
                info = balita.val()
                if all(key in info for key in ['nama', 'ibu', 'telepon', 'umur']):
                    # Membuat ClickableBox untuk setiap data balita
                    container = ClickableBox(orientation='vertical', padding=10, size_hint_y=None, height=170)
                    container.balita_info = info  # Menyimpan info balita untuk diakses saat diklik
                    container.bind(on_release=self.show_details)  # Tambahkan event on_release untuk klik
                    

                    # Canvas untuk latar belakang ClickableBox
                    with container.canvas.before:
                        from kivy.graphics import Color, Rectangle
                        Color(0.9, 0.9, 0.9, 1)  # Warna latar abu-abu muda
                        Rectangle(pos=container.pos, size=container.size)

                    # Membuat label ringkasan data balita dengan styling
                    summary = Label(
                        text=f"Nama: {info['nama']}\nUmur: {info['umur']}",
                        color=(0, 0, 0, 1),
                        bold=True,
                        font_size=20
                    )
                    container.add_widget(summary)

                    # Tambahan label telepon atau info lain
                    summary2 = Label(
                        text=f"Telepon: {info['telepon']}",
                        color=(0, 0, 0, 1),
                        font_size=20
                    )
                    container.add_widget(summary2)

                    # Tambahkan container ke data_container utama
                    self.ids.data_container.add_widget(container)

                    # Tambahkan pemisah setelah setiap ClickableBox
                    separator = Label(size_hint_y=None, height=2, color=(0, 0, 0, 1))  # Label sebagai pemisah
                    self.ids.data_container.add_widget(separator)
                else:
                    print("Data balita tidak lengkap:", info)  # Debugging jika data balita tidak lengkap
        else:
            # Jika tidak ada data balita yang ditemukan, tampilkan pesan di layar
            self.ids.data_container.add_widget(Label(text="Tidak ada data balita yang ditemukan.", color=(0, 0, 0, 1)))
            print("Tidak ada data balita atau data_balita adalah None")  # Debugging untuk memastikan data diambil

    def show_details(self, instance):
    # Tampilkan detail balita jika box container diklik
        info = instance.balita_info
        detail_layout = GridLayout(cols=2, spacing=4, padding=10, size_hint_y=None)
        
        # Tambahkan detail informasi ke dalam popup dengan teks putih
        for key, value in [("Nama", info['nama']), ("Ibu", info['ibu']), 
                        ("Telepon", info['telepon']), ("Umur", info['umur'])]:
            detail_layout.add_widget(Label(text=f"{key}:", color=(1, 1, 1, 1), halign='right', valign='middle', size_hint_y=None, height=50))
            detail_layout.add_widget(Label(text=value, color=(1, 1, 1, 1), halign='left', valign='middle', size_hint_y=None, height=50))

        # Sesuaikan tinggi layout berdasarkan jumlah data
        detail_layout.bind(minimum_height=detail_layout.setter('height'))

        # Membuat popup untuk menampilkan detail, dengan ukuran yang menyesuaikan tinggi konten
        popup = Popup(title="Detail Balita", content=detail_layout, size_hint=(None, None), 
                    size=(350, detail_layout.height + 250))  # +100 untuk memberikan ruang tambahan pada popup

        # Membuka popup
        popup.open()



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
