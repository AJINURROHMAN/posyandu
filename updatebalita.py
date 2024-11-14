from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import RoundedRectangle
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex

# Subclass ButtonBehavior untuk menambahkan klik ke BoxLayout
class ClickableBox(ButtonBehavior, BoxLayout):
    pass

class UpdateBalitaScreen(Screen):
    sidebar_open = False  # Status sidebar, tertutup pada awalnya

    def on_enter(self):
        self.hide_sidebar()
        self.load_data()  # Memanggil fungsi untuk memuat data balita dari Firebase

    def load_data(self):
        self.ids.data_container.clear_widgets()
        database = App.get_running_app().database
        data_adddata = database.db.child("adddata").child("user1").get()
        print("UpdateBalitaScreen jjj")
        
        
        colors = [
            get_color_from_hex("#82B1FF"),
            get_color_from_hex("#FFD180"),
            get_color_from_hex("#FF9E80"),
            get_color_from_hex("#B9F6CA"),
            get_color_from_hex("#FFEB3B")
        ]

        if data_adddata is not None and data_adddata.each() is not None:
            print(f"isi data {data_adddata}")
            
            for index, updatebalita in enumerate(data_adddata.each()):
                
                info = updatebalita.val()
                if all(key in info for key in ['nama', 'berat', 'lingkar_k', 'tinggi', 'lingkar_l']):
                    container = BoxLayout(orientation='vertical', padding=10, size_hint_y=None, height=170)
                    container.balita_info = info

                    button = Button(
                        text=f"{info['nama']}\nBerat: {info['berat']}",
                        size_hint_y=None,
                        height=150,
                        font_size=25,
                        color=(1, 1, 1, 1),
                        background_normal='',
                        background_color=colors[index % len(colors)],
                        markup=True
                    )
                    button.bind(on_release=self.show_details)
                    button.updatebalita_info = info

                    container.add_widget(button)
                    self.ids.data_container.add_widget(container)

                    separator = Label(size_hint_y=None, height=2)
                    self.ids.data_container.add_widget(separator)
        else:
            self.ids.data_container.add_widget(Label(text="Tidak ada data balita yang ditemukan.", color=(0, 0, 0, 1)))

    def show_details(self, instance):
        info = instance.balita_info
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=[20, 20, 20, 10])
        text_layout = BoxLayout(orientation='vertical', spacing=10)

        text_layout.add_widget(Label(text=f"Nama: {info['nama']}", color=(1, 1, 1, 1), font_size=18))
        text_layout.add_widget(Label(text=f"Tinggi: {info['tinggi']}", color=(1, 1, 1, 1), font_size=18))
        text_layout.add_widget(Label(text=f"Berat: {info['berat']}", color=(1, 1, 1, 1), font_size=18))
        text_layout.add_widget(Label(text=f"LingkarK: {info['lingkar_k']}", color=(1, 1, 1, 1), font_size=18))
        text_layout.add_widget(Label(text=f"LingkarL: {info['lingkar_l']}", color=(1, 1, 1, 1), font_size=18))

        main_layout.add_widget(text_layout)

        close_button = Button(text="Tutup", size_hint=(None, None), width=120, height=45, background_color=(0.2, 0.6, 0.8, 1), color=(1, 1, 1, 1), font_size=18)
        close_button.bind(on_release=lambda *args: popup.dismiss())

        main_layout.add_widget(close_button)

        popup = Popup(title="Detail Balita", content=main_layout, size_hint=(None, None), size=(400, 450), auto_dismiss=True)
        popup.open()

    def search_data(self, search_text):
        """Mencari data balita berdasarkan nama."""
        self.ids.data_container.clear_widgets()
        database = App.get_running_app().database
        data_adddata = database.db.child("updatebalita").child("user1").get()

        if data_adddata is not None and data_adddata.each() is not None:
            for data_adddata in data_adddata.each():
                info =data_adddata.val()
                if all(key in info for key in ['nama', 'berat', 'tinggi', 'lingkar_k', 'lingkar_l']):
                    if search_text.lower() in info['nama'].lower():
                        container = BoxLayout(orientation='vertical', padding=10, size_hint_y=None, height=170)
                        container.balita_info = info

                        button = Button(
                            text=f"{info['nama']}\nBerat: {info['berat']}",
                            size_hint_y=None,
                            height=150,
                            font_size=20,
                            color=(1, 1, 1, 1),
                            background_normal='',
                            background_color=(0.82, 0.82, 0.82, 1),
                            markup=True
                        )
                        button.bind(on_release=self.show_details)
                        button.updatebalita_info = info

                        container.add_widget(button)
                        self.ids.data_container.add_widget(container)

                        separator = Label(size_hint_y=None, height=2)
                        self.ids.data_container.add_widget(separator)

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

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(UpdateBalitaScreen(name='updatebalita_screen'))

        return sm

if __name__ == '__main__':
    MyApp().run()
