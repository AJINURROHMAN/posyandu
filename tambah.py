from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

# Memuat file .kv untuk tampilan
Builder.load_file('tambah.kv')

class TambahScreen(Screen):
    def simpan_data(self):
        # Ambil data dari field input
        nama = self.ids.nama.text
        ibu = self.ids.ibu.text
        umur = self.ids.umur.text
        telepon = self.ids.telepon.text

        # Validasi input
        if not nama or not ibu or not umur or not telepon:
            self.show_popup("Semua field harus diisi!")
            return

        try:
            # Ambil username dari MainApp
            username = App.get_running_app().user

            # Simpan data ke Firebase
            App.get_running_app().database.simpan_data(username, nama, ibu, umur, telepon)
            self.show_popup("Data berhasil disimpan!")

            # Kosongkan field setelah simpan
            self.ids.nama.text = ''
            self.ids.ibu.text = ''
            self.ids.umur.text = ''
            self.ids.telepon.text = ''
            
            # Alihkan ke halaman BalitaScreen
            self.manager.current = 'balita_screen'
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
