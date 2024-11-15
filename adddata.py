from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

# Memuat file .kv untuk tampilan
Builder.load_file('adddata.kv')

class CustomTextInput(TextInput):
    pass

class AddDataScreen(Screen):
    def simpan_data_perkembangan(self):
        # Ambil data dari field input
        Nama = self.ids.nama.text
        Berat = self.ids.berat.text
        Lingkar_K = self.ids.lingkark.text  # Sesuaikan dengan ID yang ada di adddata.kv
        Tinggi = self.ids.tinggi.text
        Lingkar_l = self.ids.lingkarl.text  # Sesuaikan dengan ID yang ada di adddata.kv
        
        # Validasi input
        if not Nama or not Berat or not Lingkar_K or not Tinggi or not Lingkar_l:
            self.show_popup("Semua field harus diisi!")
            return

        try:
            # Ambil username dari MainApp
            username = App.get_running_app().user

            # Simpan data ke Firebase
            App.get_running_app().database.simpan_data_perkembangan(username, Nama, Berat, Tinggi, Lingkar_K, Lingkar_l)
            self.show_popup("Data berhasil disimpan!")

            # Kosongkan field setelah simpan
            self.ids.nama.text = ''
            self.ids.berat.text = ''
            self.ids.tinggi.text = ''
            self.ids.lingkark.text = ''
            self.ids.lingkarl.text = ''
            
            # Alihkan ke halaman updatebalita_screen
            self.manager.current = 'updatebalita_screen'
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
