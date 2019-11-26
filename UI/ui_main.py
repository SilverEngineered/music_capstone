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
    io_play_t = None
    # Create the app for our specific case "Piano App"

    def __init__(self, io, **kwargs):
        App.__init__(self)
        self.io_reset_queue = threading.Thread(target=io.reset_queue)
        self.io_threaded_listen = threading.Thread(target=io.threaded_listen)
        # Initialize the screen manager
        self.manager = MainManager()

    def build(self):
        return self.manager

    def play(self):

        try:
            if not self.io_play_t.is_alive():
                self.io_play_t.start()
        except RuntimeError:
            self.io_play_t = threading.Thread(target=self.io.play)
            self.play()

    def reset_queue(self):
        self.io_reset_queue.start()

    def threaded_listen(self):
        self.io_threaded_listen.start()


if __name__ == '__main__':
    PianoApp().run()
