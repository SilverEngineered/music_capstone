from kivy.uix.widget import Widget
from kivy.app import App

from src import custom_widgets
from src.screen_manager import MainManager
import src.mutils as mutils

import pprint


# Call the Config Setter
mutils.set_config(width=1280, height=800, resizable=False)

# Call resource loader
mutils.load_resources()


class PianoApp(App):
    psm = None
    manager = None

    # Create the app for our specific case "Piano App"
    def __init__(self, **kwargs):
        App.__init__(self)

        # Initialize the screen manager
        self.manager = MainManager()

    def build(self):
        return self.manager


if __name__ == '__main__':
    PianoApp().run()
