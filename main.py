import argparse
import pickle
from IO.IO import IO
from UI.ui_main import PianoApp
import csv
import threading

parser = argparse.ArgumentParser()
parser.add_argument('--num_keys', default=61)
args = parser.parse_args()


def get_relative_times(times):
    new_times = []
    total_time = 0
    for i in times:
        new_times.append(i-total_time)
        total_time = i
    return new_times

def get_tuple_data_from_csv(path):
    data = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                data.append((row[0], row[1], row[2], row[3]))
                line_count += 1
        return data

def get_song_data_hash(song_info):
    song_data = {}
    for i in song_info:
        song_data[i[0]] = pickle.load(i[3])
    return song_data

if __name__ == "__main__":
    infile = open(args.midi_dump, 'rb')
    data = pickle.load(infile)
    path = 'song_data.csv'
    io = IO(args.num_keys)
    song_info = get_tuple_data_from_csv(path)
    song_tuples = [(i[0], i[1], i[2]) for i in song_info]
    PianoApp(io, song_tuples).run()
