from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App

Builder.load_file('datab.kv')

class MainScreen(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return MainScreen()

    def add_data(self):
        # Tambahkan data baru ke tampilan
        data_button = Button(text=f"Data {self.root.ids.data_box.children.__len__() + 1}")
        self.root.ids.data_box.add_widget(data_button)

    def show_data(self, data):
        # Fungsi untuk menampilkan data, bisa dikembangkan sesuai kebutuhan
        print(f"Menampilkan data: {data}")

if __name__ == '__main__':
    MyApp().run()
