import argparse
from IO.IO import IO


parser = argparse.ArgumentParser()
parser.add_argument('--num_keys', default=61)
args = parser.parse_args()
if __name__ == "__main__":
    io = IO(args.num_keys)
