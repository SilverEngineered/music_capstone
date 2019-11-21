from kivy.properties import NumericProperty, StringProperty, DictProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image

import pprint

hard_songs = {
    'Astro Boy': '/home/hirshjack/Desktop/ui_v2.1/UI/resources/2.jpg',
    'Jamie Gray': '/home/hirshjack/Desktop/ui_v2.1/UI/resources/1.jpg'
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
    song_title = Label(text='')

    def __init__(self, **kwargs):
        super(SongSelector, self).__init__(**kwargs)
        for key in hard_songs:
            self.add_song(hard_songs[key], key)
        self.add_widget(self.song_title)
        self.song_title.size_hint = .4, .1
        self.song_title.pos_hint = {'center_x': .5, 'center_y': .3}
        self.song_title.font_size = 40
        self.song_title.color = .149, .047, .047, 1

    def add_song(self, t_path, name):
        if name in self.songs.keys():
            self.songs[name].set_thumbnail(t_path)
        else:
            new_song = SongTile(name=name, t_path=t_path)
            self.songs[name] = new_song
            self.add_widget(new_song)
            new_song.size_hint = 0, 0
            new_song.pos_hint = {'x': 0, 'y': 0}
            self.lineup.append(new_song)
            self.song_count += 1

    def draw_songs(self):
        if self.song_count > 0:
            c_song = self.lineup[self.cur_song]
            # Set all non main songs invisible
            for song in self.lineup:
                song.size_hint = 0, 0
                song.pos_hint = {'x': 0, 'y': 0}

            # Center the main song
            c_song.size_hint = .5, .5
            c_song.pos_hint = {'center_x': .5, 'center_y': .6}
            self.song_title.text = c_song.name
        else:
            return

    def inc_song(self, inc):
        if self.song_count <= 0:
            return

        if inc == 1 and self.cur_song < self.song_count - 1:
            self.cur_song += inc
        elif inc == -1 and self.cur_song > 0:
            self.cur_song += inc

        self.draw_songs()


class SongTile(Image):
    idn = StringProperty('')
    idt = StringProperty('')
    name = StringProperty('')

    def __init__(self, name, t_path, **kwargs):
        super(SongTile, self).__init__(**kwargs)
        self.source = t_path
        self.name = name

    def set_thumbnail(self, t_path):
        self.source = t_path
        self.height = 50
        self.width = 50
        self.canvas.ask_update()
