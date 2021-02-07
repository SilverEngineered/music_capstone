from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window


def load_resources():
    Builder.load_file('UI/kv_files/custom_widgets.kv')
    Builder.load_file('UI/kv_files/main.kv')


def set_screen(width=1280, height=800):
    # Set the size of the window to the touchscreen resolution and lock size
    Window.size = width, height
    Window.borderless = True
    Window.top = 0
    Window.left = 0
