from kivy.properties import NumericProperty, StringProperty, DictProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.app import App
from kivy.clock import Clock
import pprint

hard_songs = {
    'Can\'t feel my face': ('./UI/resources/astroboy.jpg', 'The Weekend'),
    'Generic Song Name': ('./UI/resources/gray.jpg', 'Jamie Gray'),
    'I THINK':  ('./UI/resources/igor.png', 'Tyler The Creator'),
    'STOP TRYING TO BE GOD':  ('./UI/resources/astro.jpg', 'Travis Scott'),
    '99.9%': ('./UI/resources/99.jpeg', 'Kaytranada')
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
    song_title = CLabel(
        text='', font_name='./UI/resources/font.ttf', id='title')
    song_artist = CLabel(text='', font_name='./UI/resources/font.ttf')
    callbacks = DictProperty({})

    def __init__(self,  **kwargs):
        super(SongSelector, self).__init__(**kwargs)
        # TODO: Implement actual addition of songs
        # This is temporary
        song_dict = App.get_running_app().song_dict
        for key in song_dict:
            self.add_song(t_path=song_dict[key][0],
                          name=key, artist=song_dict[key][1])

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
                print("removing songtile: {}".format(widget.name))
                self.remove_widget(widget)

        if self.song_count > 0:
            # Draw the tiles to the right of the main one
            self.draw_adj(1, (.35, .35), {
                          'center_x': .65, 'center_y': .6}, self.cur_song)

            # Draw the tiles to the left of the main one
            self.draw_adj(-1, (.35, .35),
                          {'center_x': .35, 'center_y': .6}, self.cur_song)

            c_song = self.lineup[self.cur_song]
            self.add_widget(c_song)

            # Center the main song
            c_song.size_hint = .5, .5
            c_song.pos_hint = {'center_x': .5, 'center_y': .6}
            self.song_title.text = c_song.name
            self.song_artist.text = c_song.artist

    def draw_adj(self, loc, size_hint, pos_hint, root_i, recur=True):
        if self.song_count > 1:
            n_song = None

            # This is to add the songtile on the right
            if loc == 1 and root_i < self.song_count - 1:
                n_song = self.lineup[root_i + 1]
                print("adding song: {}".format(self.lineup[root_i + 1].name))
                if recur:
                    self.draw_adj(1,
                                  (size_hint[0] - .10, size_hint[1] - .1),
                                  {'center_x': pos_hint['center_x']+.08,
                                      'center_y': pos_hint['center_y']},
                                  root_i=root_i + 1, recur=False
                                  )

            # This is to add the songtile on the left
            elif loc == -1 and root_i > 0:
                n_song = self.lineup[root_i - 1]
                print("adding song: {}".format(self.lineup[root_i - 1].name))
                if recur:
                    self.draw_adj(-1,
                                  (size_hint[0] - .10, size_hint[1] - .1),
                                  {'center_x': pos_hint['center_x']-.08,
                                      'center_y': pos_hint['center_y']},
                                  root_i=root_i - 1, recur=False
                                  )
            else:
                return

            # Now we actually add the widget
            n_song.size_hint = size_hint
            n_song.pos_hint = pos_hint
            self.add_widget(n_song)

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

    def select_callback(self):
        self.callbacks['set_song'](self.lineup[self.cur_song])
        self.callbacks['switch']('game')
        App.get_running_app().play(self.get_song_name())
        Clock.schedule_once(
            lambda dt: self.callbacks['switch']('selection'), App.get_running_app().get_runtime())


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
