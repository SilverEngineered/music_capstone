from kivy.uix.widget import Widget
from kivy.app import App

from UI.src import custom_widgets
from UI.src.screen_manager import MainManager
import UI.src.mutils as mutils
from kivy.core.window import Window
import threading
import pprint
import threading

# Call the Config Setter
mutils.set_screen(width=1200, height=800)

# Call resource loader
mutils.load_resources()


class PianoApp(App):
    manager = None
    io = None
    # Create the app for our specific case "Piano App"

    def __init__(self, io, **kwargs):
        App.__init__(self)
        self.io_play = threading.Thread(target=io.play)
        # Initialize the screen manager
        self.manager = MainManager()

    def build(self):
        return self.manager

    def play(self):
        self.io_play.start()

if __name__ == '__main__':
    PianoApp().run()
