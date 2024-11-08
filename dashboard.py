from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock

class DashboardScreen(Screen):
    def on_enter(self):
        # Menampilkan popup saat layar terbuka
        self.show_popup()

    def show_popup(self):
        # Mengatur popup agar mulai dengan opacity 0 (transparan)
        self.ids.popup_box.opacity = 1

        # Animasi untuk fade-in (muncul) selama 1 detik
        anim_appear = Animation(opacity=1, d=1.0)
        anim_appear.start(self.ids.popup_box)

        # Setelah animasi fade-in selesai, tunggu 1 detik, lalu jalankan fade-out
        Clock.schedule_once(self.hide_popup, 1.5)  # Total 1 detik muncul + 0.5 detik untuk fade-in

    def hide_popup(self, dt):
        # Animasi untuk fade-out (menghilang) selama 1 detik
        anim_disappear = Animation(opacity=0, d=1.0)
        anim_disappear.start(self.ids.popup_box)

class MenuScreen(Screen):
    pass

class DashboardApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name='dashboard_screen'))
        sm.add_widget(MenuScreen(name='menu_screen'))
        sm.current = 'dashboard_screen'
        return sm

if __name__ == '__main__':
    Window.size = (360, 640)
    DashboardApp().run()
