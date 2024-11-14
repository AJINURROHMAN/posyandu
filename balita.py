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
from kivy.uix.textinput import TextInput  # Import TextInput untuk input pencarian
from kivy.utils import get_color_from_hex

# Subclass ButtonBehavior untuk menambahkan klik ke BoxLayout
class ClickableBox(ButtonBehavior, BoxLayout):
    pass

class BalitaScreen(Screen):
    sidebar_open = False  # Status sidebar, tertutup pada awalnya

    def on_enter(self):
        self.hide_sidebar()
        self.load_data()  # Memanggil fungsi untuk memuat data balita dari Firebase

    def load_data(self):
        self.ids.data_container.clear_widgets()
        database = App.get_running_app().database
        data_balita = database.db.child("balita").child("user1").get()
        print('profil')
        
        colors = [
            get_color_from_hex("#82B1FF"),  # Biru Muda Terang
            get_color_from_hex("#FFD180"),  # Peach Terang
            get_color_from_hex("#FF9E80"),  # Merah Muda Salmon
            get_color_from_hex("#B9F6CA"),  # Hijau Mint Cerah
            get_color_from_hex("#FFEB3B")   # Kuning Cerah
        ]

        if data_balita is not None and data_balita.each() is not None:
            for index, balita in enumerate(data_balita.each()):
                info = balita.val()
                if all(key in info for key in ['nama', 'ibu', 'telepon', 'umur']):
                    container = BoxLayout(orientation='vertical', padding=10, size_hint_y=None, height=170)
                    container.balita_info = info

                    button = Button(
                        text=f" {info['nama']}\n[b]Umur:[/b] {info['umur']}",
                        size_hint_y=None,
                        height=150,
                        font_size=25,
                        color=(1, 1, 1, 1),
                        background_normal='',
                        background_color=colors[index % len(colors)],
                        markup=True
                    )
                    button.bind(on_release=self.show_details)
                    button.balita_info = info

                    container.add_widget(button)
                    self.ids.data_container.add_widget(container)

                    separator = Label(size_hint_y=None, height=2)
                    self.ids.data_container.add_widget(separator)
        else:
            self.ids.data_container.add_widget(Label(text="Tidak ada data balita yang ditemukan.", color=(0, 0, 0, 1)))
            print("Tidak ada data balita atau data_balita adalah None")

    def show_details(self, instance):
        info = instance.balita_info
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=[20, 20, 20, 10])
        text_layout = BoxLayout(orientation='vertical', spacing=10)

        text_layout.add_widget(Label(text=f"Nama:\n{info['nama']}", color=(1, 1, 1, 1), font_size=18, halign="center", valign="middle", text_size=(360, None)))
        text_layout.add_widget(Label(text=f"Ibu:\n{info['ibu']}", color=(1, 1, 1, 1), font_size=18, halign="center", valign="middle", text_size=(360, None)))
        text_layout.add_widget(Label(text=f"Telepon:\n{info['telepon']}", color=(1, 1, 1, 1), font_size=18, halign="center", valign="middle", text_size=(360, None)))
        text_layout.add_widget(Label(text=f"Umur:\n{info['umur']}", color=(1, 1, 1, 1), font_size=18, halign="center", valign="middle", text_size=(360, None)))

        main_layout.add_widget(text_layout)

        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=60)
        button_layout.add_widget(BoxLayout())  # Spacer

        close_button = Button(
            text="Tutup",
            size_hint=(None, None),
            width=120,
            height=45,
            background_normal='',
            background_color=(0.2, 0.6, 0.8, 1),
            color=(1, 1, 1, 1),
            font_size=18
        )
        close_button.bind(on_release=lambda *args: popup.dismiss())
        button_layout.add_widget(close_button)

        button_layout.add_widget(BoxLayout())  # Spacer
        main_layout.add_widget(button_layout)

        popup = Popup(
            title="Detail Balita",
            content=main_layout,
            size_hint=(None, None),
            size=(400, 450),
            auto_dismiss=True
        )
        popup.open()

    def search_data(self, search_text):
        """Mencari data balita berdasarkan nama."""
        self.ids.data_container.clear_widgets()
        database = App.get_running_app().database
        data_balita = database.db.child("balita").child("user1").get()

        if data_balita is not None and data_balita.each() is not None:
            for balita in data_balita.each():
                info = balita.val()
                if all(key in info for key in ['nama', 'ibu', 'telepon', 'umur']):
                    if search_text.lower() in info['nama'].lower():  # Pencarian berdasarkan nama
                        container = BoxLayout(orientation='vertical', padding=10, size_hint_y=None, height=170)
                        container.balita_info = info

                        button = Button(
                            text=f"[b]{info['nama']}[/b]\n[b]{info['umur']}[/b]",
                            size_hint_y=None,
                            height=150,
                            font_size=20,
                            
                            color=(1, 1, 1, 1),
                            background_normal='',
                            background_color=(0.82, 0.82, 0.82, 1),  # Warna tetap
                            markup=True
                        )
                        button.bind(on_release=self.show_details)
                        button.balita_info = info

                        container.add_widget(button)
                        self.ids.data_container.add_widget(container)

                        separator = Label(size_hint_y=None, height=2)
                        self.ids.data_container.add_widget(separator)

        else:
            self.ids.data_container.add_widget(Label(text="Tidak ada data balita yang ditemukan.", color=(0, 0, 0, 1)))
        
    def toggle_sidebar(self):
        if self.sidebar_open:
            self.hide_sidebar()
        else:
            self.show_sidebar()

    def show_sidebar(self):
        anim = Animation(x=0, duration=0.3)
        anim.start(self.ids.sidebar)
        self.sidebar_open = True

    def hide_sidebar(self):
        anim = Animation(x=-self.ids.sidebar.width, duration=0.3)
        anim.start(self.ids.sidebar)
        self.sidebar_open = False

# Tambahkan tombol pencarian di layout Anda
class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Membuat layout untuk tombol pencarian
        search_layout = BoxLayout(size_hint_y=None, height=50, padding=10)
        
        # Input untuk pencarian
        self.search_input = TextInput(hint_text="Cari nama balita...", size_hint_x=0.8)
        search_layout.add_widget(self.search_input)

        # Tombol pencarian
        search_button = Button(text="Cari", size_hint_x=0.2)
        search_button.bind(on_release=lambda x: self.balita_screen.search_data(self.search_input.text))
        search_layout.add_widget(search_button)

        layout.add_widget(search_layout)

        # Tambahkan BalitaScreen ke layout
        self.balita_screen = BalitaScreen(name='balita_screen')
        layout.add_widget(self.balita_screen)

        return layout

if __name__ == '__main__':
    MyApp().run()