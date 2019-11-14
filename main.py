import argparse
import pickle
from IO.IO import IO


parser = argparse.ArgumentParser()
parser.add_argument('--num_keys', default=61)
parser.add_argument('--midi_dump', default='Resources/midi_dumps/swmid.p')
args = parser.parse_args()


if __name__ == "__main__":
    infile = open(args.midi_dump, 'rb')
    data = pickle.load(infile)
    notes = data['notes']
    times = data['times']
    io = IO(args.num_keys, notes, times)
    io.play()
