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
    song_dict = None

    # Song info in format
    def __init__(self, io, song_info, ** kwargs):
        App.__init__(self)
        self.format_song_info(song_info)
        self.io = io
        self.playing = False
        # Initialize the screen manager
        self.manager = MainManager()

    def build(self):
        return self.manager

    def format_song_info(self, song_info):
        song_dict = {}
        for song in song_info:
            song_dict[song[0]] = (song[1], song[2])
        self.song_dict = song_dict

    def play(self, song_name):
        if self.io_play_t is not None and self.io_play_t.is_alive():
            pass
        else:
            if self.io_play_t is not None:
                self.io_play_t.join()
            self.io_play_t = threading.Thread(target=self.io.play, args=(song_name,))
            if not self.io.playing:
                self.io_play_t.start()

    def get_runtime(self):
        return self.io.this_runtime()
