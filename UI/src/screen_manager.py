from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from src.custom_widgets import CScreen


class MainMenuScreen(CScreen):
    pass


class SelectionScreen(CScreen):
    pass


class MainManager(ScreenManager):
    '''
    Class responsible for managing the screens of the game and swapping
    between them as needed
    '''
    wds = {}  # Dictionary of registered screens

    def __init__(self, **kwargs):

        # Initialize the super class
        ScreenManager.__init__(self)
        self.transition = SlideTransition(direction='up')
        self.add_screen('main_menu', MainMenuScreen(
            {'print': self.print_screens,
             'switch': self.select_screen}))

        self.add_screen('selection', SelectionScreen(
            {'print': self.print_screens}))

    def add_screen(self, name, scr):
        # Add a screen to the screen manager
        self.wds[name] = scr
        scr.name = name
        self.add_widget(scr)

    def print_screens(self):
        [print(screen_i) for screen_i in self.wds]

    def select_screen(self, name):
        self.current = name
