from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput



# Memuat file .kv untuk tampilan
Builder.load_file('tambah_bumil.kv')

class CustomTextInput(TextInput):
    pass
class TambahBumilScreen(Screen):
    def simpan_data_bumil(self):
        # Ambil data dari field input
        nama = self.ids.nama.text
        suami = self.ids.suami.text
        alamat = self.ids.alamat.text
        telepon = self.ids.telepon.text
       
        # Validasi input
        if not nama or not suami or not alamat or not telepon:
            self.show_popup("Semua field harus diisi!")
            return

        try:
            # Ambil username dari MainApp
            username = App.get_running_app().user

            # Simpan data ke Firebase
            App.get_running_app().database.simpan_data_bumil(username, nama, suami, alamat, telepon)
            self.show_popup("Data berhasil disimpan!")

            # Kosongkan field setelah simpan
            self.ids.nama.text = ''
            self.ids.suami.text = ''
            self.ids.alamat.text = ''
            self.ids.telepon.text = ''
          
            
            # Alihkan ke halaman BumilScreen
            self.manager.current = 'bumil_screen'
        except Exception as e:
            self.show_popup(f"Error saat menyimpan data: {e}")

    def show_popup(self, message):
        popup_content = BoxLayout(orientation='vertical', padding=10)
        message_label = Label(text=message)
        close_button = Button(text="Tutup", size_hint_y=None, height=40)
        
        popup_content.add_widget(message_label)
        popup_content.add_widget(close_button)

        popup = Popup(title="Pesan", content=popup_content, size_hint=(0.8, 0.4), auto_dismiss=False)
        close_button.bind(on_release=popup.dismiss)
        popup.open()
