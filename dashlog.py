from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.animation import Animation
import pyrebase

class DashlogScreen(Screen):
    sidebar_visible = False  # Status sidebar
    sidebar_open = False  # Status sidebar
    popup_shown = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.firebase_config = {
            'apiKey': "AIzaSyB2_TfaI8Cdoi8VRMpmJuerxtgLxj6xwmU",
            'authDomain': "posyandu-cc282.firebaseapp.com",
            'databaseURL': "https://posyandu-cc282-default-rtdb.firebaseio.com",
            'projectId': "posyandu-cc282",
            'storageBucket': "posyandu-cc282.firebasestorage.app",
            'messagingSenderId': "952523595613",
            'appId': "1:952523595613:web:090a3f320f359738f1d2b4",
        }
        self.firebase = pyrebase.initialize_app(self.firebase_config)
        self.db = self.firebase.database()

    def on_enter(self):
        # Cek apakah popup sudah pernah ditampilkan
        if not self.popup_shown:
            print('show pop up on_enter')
            Clock.schedule_once(self.show_popup, 0)
            self.popup_shown = True  # Delay sedikit agar popup dapat ditampilkan setelah layar muncul
            Clock.schedule_once(self.get_babies_count, 0)
            Clock.schedule_once(self.get_pregnant_mothers_count, 0)  # Ambil jumlah ibu hamil

        # Ambil jumlah balita dan ibu hamil dari Firebase dan tampilkan
        Clock.schedule_once(self.get_babies_count, 0)
        Clock.schedule_once(self.get_pregnant_mothers_count, 0)

        # Waktu swipe otomatis
        Clock.schedule_interval(self.change_carousel_image, 3)

    def get_babies_count(self, dt):
        try:
            # Mengambil data balita dari Firebase
            babies_data = self.db.child('balita').get()
            print("Data yang diterima (Balita):", babies_data.val())  # Debugging: Tampilkan data yang diterima

            if babies_data:
                # Menghitung jumlah data balita, hitung berdasarkan entri dalam user1
                babies_count = len(babies_data.val().get('user1', {}))  # Hitung entri di dalam 'user1'
            else:
                babies_count = 0

            print(babies_count)  # Debugging: Tampilkan jumlah balita yang dihitung

            # Menampilkan jumlah balita di label
            if hasattr(self.ids, 'babies_count_label'):
                self.ids.babies_count_label.text = f" {babies_count}"
            else:
                print("ID 'babies_count_label' tidak ditemukan.")
        except Exception as e:
            print(f"Error retrieving babies count: {e}")

    def get_pregnant_mothers_count(self, dt):
        try:
            # Mengambil data ibu hamil dari Firebase
            pregnant_mothers_data = self.db.child('bumil').get()
            print("Data yang diterima (bumil):", pregnant_mothers_data.val())  # Debugging: Tampilkan data yang diterima

            if pregnant_mothers_data:
                # Menghitung jumlah data ibu hamil, hitung berdasarkan entri dalam user1
                pregnant_mothers_count = len(pregnant_mothers_data.val().get('user1', {}))  # Hitung entri di dalam 'user1'
            else:
                pregnant_mothers_count = 0

            print( pregnant_mothers_count)  # Debugging: Tampilkan jumlah ibu hamil yang dihitung

            # Menampilkan jumlah ibu hamil di label
            if hasattr(self.ids, 'pregnant_mothers_count_label'):
                self.ids.pregnant_mothers_count_label.text = f"{pregnant_mothers_count}"
            else:
                print("ID 'pregnant_mothers_count_label' tidak ditemukan.")
        except Exception as e:
            print(f"Error retrieving pregnant mothers count: {e}")


    def show_popup(self, dt):
        # Mengatur opacity popup ke 0 (tersembunyi)
        self.ids.popup_box.opacity = 0
        print('show pop up')

        # Animasi fade-in selama 1 detik
        anim_appear = Animation(opacity=1, duration=1.0)
        anim_appear.start(self.ids.popup_box)

        # Menjadwalkan penghilangan popup setelah 2 detik
        Clock.schedule_once(self.hide_popup, 2)
        print('test pop up hide')

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

    def change_carousel_image(self, dt):
        # Berganti ke gambar berikutnya dalam Carousel
        carousel = self.ids.calendar_carousel
        carousel.load_next()
