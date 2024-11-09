from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.animation import Animation
from kivy.clock import Clock

class LoginScreen(Screen):
    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text

        # Validasi username dan password dengan data dari Firebase
        if self.validate_credentials(username, password):
            App.get_running_app().user = username  # Simpan username di MainApp
            self.ids.popup_box.opacity = 0
            print( 'show pop up')

            # Animasi fade-in selama 1 detik
            anim_appear = Animation(opacity=1, duration=1.0)
            anim_appear.start(self.ids.popup_box)

            # Menjadwalkan penghilangan popup setelah 2 detik
            Clock.schedule_once(self.hide_popup, 2)
            
            self.manager.current = 'dashlog_screen'  # Alihkan ke dashboard
        else:
            self.show_popup("Login gagal! Periksa username dan password.")
            print('Login gagal! Periksa username dan password.')
    def hide_popup(self, dt):
            # Animasi fade-out selama 1 detik
            anim_disappear = Animation(opacity=0, duration=1.0)
            anim_disappear.start(self.ids.popup_box)

    def validate_credentials(self, username, password):
        # Ambil data login dari Firebase
        database = App.get_running_app().database
        user_data = database.db.child("login").get()

        if user_data is not None and user_data.each():
            for data in user_data.each():
                info = data.val()
                # Cek apakah username dan password sesuai dengan data di database
                if info.get("username") == username and info.get("password") == password:
                    return True  # Login berhasil
        return False  # Login gagal

    def show_popup(self, message):
        # Buat tampilan popup dengan desain yang lebih rapi
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        message_label = Label(text=message, halign='center', valign='middle', text_size=(300, None), color=(0, 0, 0, 1))
        close_button = Button(text="Tutup", size_hint=(0.4, None), height=40, pos_hint={'center_x': 0.5}, background_color=(0.7, 0, 0, 1), color=(1, 1, 1, 1))

        # Atur tata letak dan tambahan widget
        popup_layout.add_widget(message_label)
        popup_layout.add_widget(close_button)

        # Membuat popup
        popup = Popup(title="Pesan Login", content=popup_layout, size_hint=(None, None), size=(350, 200), auto_dismiss=False)
        close_button.bind(on_release=popup.dismiss)
        
        # Tampilkan popup
        popup.open()
