from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window

# Muat file .kv
Builder.load_file('menu.kv')
Builder.load_file('balita.kv')


class MenuScreen(Screen):
    pass
class BalitaScreen(Screen):
    pass
class BerandaScreen(Screen):
    pass
class DashboardScreen(Screen):
    pass


class MyApp(App):
    def build(self):
        sm = ScreenManager()

        # Tambahkan screen ke dalam ScreenManager
        sm.add_widget(MenuScreen(name='menu_screen'))
        sm.add_widget(BalitaScreen(name='balita_screen'))
        sm.add_widget(BerandaScreen(name='beranda_screen'))
        sm.add_widget(DashboardScreen(name='dashboard_screen'))
        sm.current = 'menu_screen'
        
        return sm

if __name__ == '__main__':
    Window.size = (360, 640)
    MyApp().run()
