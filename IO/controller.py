import IO2
import rtmidi
import mido
import threading


def callback(port, msg):
    port.light(msg.note-72, (255,255,0))


if __name__ == "__main__":
    io = IO2.IO2(callback)
    
