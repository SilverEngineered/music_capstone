import board
from neopixel import NeoPixel
import mido
import rtmidi
import threading

class Lights:
    def __init__(self, num_keys):
        self.num_keys = num_keys
        self.pixels = NeoPixel(board.D18, num_keys)

    def reset(self):
        for i in range(self.num_keys):
            self.on(i, (0,0,0))
    def on(self, index, color):
        self.pixels[index] = color

class MIDI:
    def __init__(self, func):
        self.inport = mido.open_input(mido.get_input_names()[0])
        self.inport.callback = func
    
    def receive(self):
        self.inport.receive()


if __name__ == "__main__":
    light = Lights(61)
    light.reset() 
    def cbfun(msg):
        #print(msg.note_on)
        num = msg.note - 72
        if msg.type == 'note_on':
            light.on(num, (255,0,0))
        else:
            light.on(num, (0,0,0))

    mm = MIDI(cbfun)
    t1 = threading.Thread(target = mm.receive())
    t1.start()
