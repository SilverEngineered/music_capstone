from kivy.properties import NumericProperty, StringProperty, DictProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex

import pprint

hard_songs = {
    'Can\'t feel my face': ('./resources/astroboy.jpg', 'The Weekend'),
    'Generic Song Name': ('./resources/gray.jpg', 'Jamie Gray'),
    'I THINK':  ('./resources/igor.png', 'Tyler The Creator'),
    'STOP TRYING TO BE GOD':  ('./resources/astro.jpg', 'Travis Scott')
}


class CButton(Button):
    idn = StringProperty('')
    idt = StringProperty('')

    def set_size(self, height, width):
        print("called")
        print(self.size_hint)
        print(str(height) + str(width))
        self.size_hint = height, width


class CScreen(Screen):
    idn = StringProperty('')
    idt = StringProperty('')
    callbacks = DictProperty({})

    def __init__(self, callbacks, **kwargs):
        super(CScreen, self).__init__(**kwargs)
        # Set the callbacks to the dict passed by the manager
        self.callbacks = callbacks
        self.callbacks['print_widg'] = self.print_widgets

    def print_widgets(self):
        print("Printing widgets for {}:".format(self.idn))
        pp = pprint.PrettyPrinter(indent=4)
        [pp.pprint(widget.idn + ":" + widget.idt) for widget in self.walk()]


class CFlay(FloatLayout):
    idn = StringProperty('')
    idt = StringProperty('')


class CLabel(Label):
    idn = StringProperty('')
    idt = StringProperty('')
    header_size = NumericProperty(52)
    block_size = NumericProperty(24)


class SongSelector(FloatLayout):
    idn = StringProperty('')
    idt = StringProperty('')
    songs = DictProperty({})
    lineup = ListProperty([])
    cur_song = 0
    song_count = 0
    song_title = CLabel(text='', font_name='./resources/font.ttf', id='title')
    song_artist = CLabel(text='', font_name='./resources/font.ttf')

    def __init__(self, **kwargs):
        super(SongSelector, self).__init__(**kwargs)
        # TODO: Implement actual addition of songs
        # This is temporary
        for key in hard_songs:
            self.add_song(t_path=hard_songs[key][0],
                          name=key, artist=hard_songs[key][1])

        # Set up the title for the Song
        self.setup_title()

        # Draw the songs
        self.draw_songs()

    def setup_title(self):
        self.add_widget(self.song_title)
        self.song_title.size_hint = .4, .1
        self.song_title.pos_hint = {'center_x': .5, 'center_y': .3}
        self.song_title.font_size = 40
        self.song_title.color = get_color_from_hex('#565c5c')

        self.add_widget(self.song_artist)
        self.song_artist.size_hint = .4, .06
        self.song_artist.pos_hint = {'center_x': .5, 'center_y': .25}
        self.song_artist.font_size = 28
        self.song_artist.color = get_color_from_hex('#879191')

    def add_song(self, t_path, name, artist):
        if name in self.songs.keys():
            self.songs[name].set_thumbnail(t_path)
        else:
            new_song = SongTile(name=name, t_path=t_path, artist=artist)
            self.songs[name] = new_song
            self.lineup.append(new_song)
            self.song_count += 1

    def draw_songs(self):
        for widget in self.walk():
            if type(widget) is SongTile:
                self.remove_widget(widget)

        if self.song_count > 0:
            if self.cur_song < self.song_count - 1:
                n_song = self.lineup[self.cur_song + 1]
                self.add_widget(n_song)
                n_song.size_hint = .35, .35
                n_song.pos_hint = {'center_x': .65, 'center_y': .6}

            if self.cur_song > 0:
                p_song = self.lineup[self.cur_song - 1]
                self.add_widget(p_song)
                p_song.size_hint = .35, .35
                p_song.pos_hint = {'center_x': .35, 'center_y': .6}

            c_song = self.lineup[self.cur_song]
            self.add_widget(c_song)

            # Center the main song
            c_song.size_hint = .5, .5
            c_song.pos_hint = {'center_x': .5, 'center_y': .6}
            self.song_title.text = c_song.name
            self.song_artist.text = c_song.artist

    def inc_song(self, inc):
        if self.song_count <= 0:
            return

        if inc == 1 and self.cur_song < self.song_count - 1:
            self.cur_song += inc
        elif inc == -1 and self.cur_song > 0:
            self.cur_song += inc

        self.draw_songs()

    def get_song_name(self):
        return self.lineup[self.cur_song].name


class SongTile(Image):
    idn = StringProperty('')
    idt = StringProperty('')
    name = StringProperty('')
    artist = StringProperty('')

    def __init__(self, name, t_path, artist, **kwargs):
        super(SongTile, self).__init__(**kwargs)
        self.source = t_path
        self.name = name
        self.artist = artist

    def set_thumbnail(self, t_path):
        self.source = t_path
        self.canvas.ask_update()
