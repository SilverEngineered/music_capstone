from kivy.lang import Builder
from kivy.config import Config


def load_resources():
    # Builder.load_file('kv_files/custom_widgets.kv')
    Builder.load_file('kv_files/main.kv')


def set_config(width=1280, height=800, resizable=False):
    # Set the size of the window to the touchscreen resolution and lock size
    Config.set('graphics', 'width', width)
    Config.set('graphics', 'height', height)
    Config.set('graphics', 'resizable', resizable)

    # Set the keyboard mode
    # TODO: Currently Not In Use
    Config.set('kivy', 'keyboard_mode', 'dock')
