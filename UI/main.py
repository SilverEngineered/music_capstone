from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('kv_files/menus.kv')
Builder.load_file('kv_files/piano.kv')

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class PianoGame(Widget):
    tap_count = NumericProperty(0)

    def on_touch_down(self, touch):
        self.tap_count += 1

class PianoApp(App):
    manager = ScreenManager()

    def add_manager_widgets(self):
        self.manager.add_widget(MenuScreen(name='menu'))
        self.manager.add_widget(SettingsScreen(name='settings'))

    def build(self):
        self.add_manager_widgets()
        return self.manager

if __name__ == '__main__':
    PianoApp().run()