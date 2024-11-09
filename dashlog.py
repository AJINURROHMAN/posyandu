from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.clock import Clock

class DashlogScreen(Screen):
    sidebar_visible = False  # Status sidebar
    sidebar_open = False  # Status sidebar
    popup_shown = False

    def on_enter(self):
        # Cek apakah popup sudah pernah ditampilkan
        if not self.popup_shown:
            print('show pop up on_enter')
            Clock.schedule_once(self.show_popup, 0)
            self.popup_shown = True  # Delay sedikit agar popup dapat ditampilkan setelah layar muncul

    def show_popup(self, dt):
        # Mengatur opacity popup ke 0 (tersembunyi)
        self.ids.popup_box.opacity = 0
        print( 'show pop up')

        # Animasi fade-in selama 1 detik
        anim_appear = Animation(opacity=1, duration=1.0)
        anim_appear.start(self.ids.popup_box)

        # Menjadwalkan penghilangan popup setelah 2 detik
        Clock.schedule_once(self.hide_popup, 2)
        print(' test pop up hide ')
    def hide_popup(self, dt):
        # Animasi fade-out selama 1 detik
        anim_disappear = Animation(opacity=0, duration=1.0)
        anim_disappear.start(self.ids.popup_box)

    def toggle_sidebar(self):
        # Toggle sidebar visibility
        anim = Animation(x=0 if self.sidebar_open else -self.ids.sidebar.width, duration=0.3)
        anim.start(self.ids.sidebar)
        self.sidebar_open = not self.sidebar_open

    def hide_sidebar(self):
        # Menyembunyikan sidebar
        anim = Animation(x=-self.ids.sidebar.width, duration=0.3)
        anim.start(self.ids.sidebar)
        self.sidebar_open = False
