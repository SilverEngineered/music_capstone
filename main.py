import argparse
import pickle
#from IO.IO import IO


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
    print(times)
    print(relative_times)
    exit()
    io = IO(args.num_keys, notes, relative_times)
    io.play()
