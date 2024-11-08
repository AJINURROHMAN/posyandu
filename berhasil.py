from kivy.app import App
from kivy .lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen

Builder.load_file('berhasil.kv')

class BerhasilScreen(Screen):
    pass
class BerhasilScreen(Screen):
    def on_enter(self):
        # Animasi pertama untuk memunculkan top_box dengan fade-in dan geser dari atas
        anim_appear = Animation(opacity=1, pos_hint={'top': 1}, d=1)
        
        # Animasi kedua untuk menunggu selama 0.5 detik lalu menghilangkan top_box
        anim_disappear = Animation(opacity=0, d=1)

        # Jalankan animasi pertama
        anim_appear.start(self.ids.top_box)
        
        # Setelah animasi pertama selesai, tunggu 0.5 detik lalu jalankan animasi menghilang
        anim_appear.bind(on_complete=lambda *x: anim_disappear.start(self.ids.top_box)) # Memulai animas

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BerhasilScreen(name='berhasil_screen'))
        sm.current = 'berhasil_screen'
        return sm

if __name__ == '__main__':
    Window.size = (360, 640)
    TestApp().run()
