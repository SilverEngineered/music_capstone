from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
import os.path

# ---------------
# Classes representing the Screens of the App


class MainMenuScreen(Screen):
    '''
    Class representing the main menu of the app
    '''
    pass


class SettingsScreen(Screen):
    ''' 
    Class representing the settings menu of the app
    '''
    pass


class SelectionScreen(Screen):
    '''
    Class representing the song selection menu of the app
    '''
    pass


class GameplayScreen(Screen):
    '''
    Class representing the screen for the gameplay
    '''
    pass


class EndScreen(Screen):
    '''
    Class representing the screen for when a user has finished a song and
    '''
    pass

# ---------------


class PianoSM(ScreenManager):
    '''
    Class responsible for managing the screens of the game and swapping
    between them as needed
    '''

    def __init__(self, **kwargs):

        # Initialize the super class
        ScreenManager.__init__(self)
