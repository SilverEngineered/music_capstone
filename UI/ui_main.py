# Gather all me modules
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

import loader
import os.path

from loader import tld

from src import screen_manager as sm

# I've gathered all me modules !

# Set the size of the window to the touchscreen resolution and lock size
Config.set('graphics', 'width', 1280)
Config.set('graphics', 'height', 800)
Config.set('graphics', 'resizable', False)

# Create the App
print(tld)


class PianoApp(App):

    def __init__(self, **kwargs):
        App.__init__(self)

        # Initialize the screen manager
        self.psm = sm.PianoSM()

    def build(self):
        return self.psm

    def callback_manager(self, message):
        '''
        Handles the callback for given input systems
        '''
        print(message)

    def get_text(self, prompt):
        '''
        Based on the prompt returns the text that should be on the button
        '''
        return tld[prompt]

    def get_value(self, key):
        return 1


if __name__ == '__main__':
    PianoApp().run()
