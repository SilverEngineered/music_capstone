import argparse
import pickle
from IO.IO import IO
from UI.ui_main import PianoApp
import threading

parser = argparse.ArgumentParser()
parser.add_argument('--num_keys', default=61)
parser.add_argument('--midi_dump', default='Resources/midi_dumps/swmid.p')
args = parser.parse_args()


def get_relative_times(times):
    new_times = []
    total_time = 0
    for i in times:
        new_times.append(i-total_time)
        total_time = i
    return new_times


if __name__ == "__main__":
    infile = open(args.midi_dump, 'rb')
    data = pickle.load(infile)
    notes = data['notes']
    times = data['times']
    relative_times = get_relative_times(times)
    io = IO(args.num_keys, notes, relative_times)

    song_info = [('Can\'t feel my face', './UI/resources/astroboy.jpg', 'The Weekend'),
     ('Generic Song Name', './UI/resources/gray.jpg', 'Jamie Gray'),
     ('I THINK' './UI/resources/igor.png', 'Tyler The Creator'),
     ('STOP TRYING TO BE GOD' './UI/resources/astro.jpg', 'Travis Scott'),
     ('99.9%' './UI/resources/99.jpeg', 'Kaytranada')]
    PianoApp(io, song_info).run()