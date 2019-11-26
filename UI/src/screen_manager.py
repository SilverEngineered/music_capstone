from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.properties import StringProperty
from src.custom_widgets import CScreen


class MainMenuScreen(CScreen):
    pass


class SelectionScreen(CScreen):
    pass


class GameScreen(CScreen):
    s_title = StringProperty(' ')
    s_artist = StringProperty(' ')
    s_tpath = StringProperty('')

    def set_song(self, song):
        print('Set the song to {}'.format(song.name))
        self.s_title = song.name
        self.s_artist = song.artist
        self.s_tpath = song.source

    def get_den(self, title):
        font_size = None
        mult = 1
        text = self.s_title
        if not title:
            mult = 2
            text = self.s_artist
        font_size = (mult * len(text))
        if font_size > 50:
            font_size = 50
        elif font_size < 18:
            font_size = 18
        return font_size


class MainManager(ScreenManager):
    '''
    Class responsible for managing the screens of the game and swapping
    between them as needed
    '''
    wds = {}  # Dictionary of registered screens
    selected_song = None

    def __init__(self, **kwargs):

        # Initialize the super class
        ScreenManager.__init__(self)
        self.transition = SlideTransition(direction='up')
        self.add_screen('main_menu', MainMenuScreen(
            {'print': self.print_screens,
             'switch': self.select_screen}))

        self.add_screen('game', GameScreen(
            {'print': self.print_screens,
             'switch': self.select_screen}))

        self.add_screen('selection', SelectionScreen(
            {'print': self.print_screens,
             'set_song': self.wds['game'].set_song,
             'switch': self.select_screen}))

    def add_screen(self, name, scr):
        # Add a screen to the screen manager
        self.wds[name] = scr
        scr.name = name
        self.add_widget(scr)

    def print_screens(self):
        [print(screen_i) for screen_i in self.wds]

    def select_screen(self, name):
        self.current = name

    def get_song(self):
        return self.selected_song

    def set_song(self, name):
        self.selected_song = name
