import mido
import rtmidi
import threading
import board
from neopixel import NeoPixel
import time

ITV=0.01
PT = 0.5
SHOW = 0.1
LOFF = 50
white = [0,2,4,5,7,9,11]
black = [1,3,-1,6,8,10,-1]
class Lights:
    def __init__(self, num_keys):
        self.num_keys = num_keys
        self.pixels = NeoPixel(board.D18, num_keys)
        self.array = []
        for i in range(num_keys):
            self.array.append([])


    def __del__(self):
        self.reset()

    def reset(self):
        for i in range(36, 61 + 36):
            self.off(i)

    def on(self, key, color):
        #print("lighting " + str(index) + str(color)) 
        index = self.getindex(key)
        self.pixels[index] = color
    
    def off(self, key):
        index = self.getindex(key)
        self.pixels[index] = (0,0,0)
    
    def getindex(self, key):
        key = key - 36
        r = key % 12
        offset = key // 12
        if r in white:
            v = white.index(r)
            return 7*offset + v
        else:
            v = black.index(r)
            return 69 - 7*offset - v
            



class MIDI:
    def __init__(self, func):
        self.inport = mido.open_input(mido.get_input_names()[0])
        self.inport.callback = func
    
    def receive(self):
        self.inport.receive()

    def open(path):
        return mido.MidiFile(path)


class Contr:
    def __init__(self):
        self.light = Lights(71)
        self.light.reset()
        self.array = []
        self.playing = False
        self.play_time = 0
        t = threading.Thread(target = self.renew)
        t.start()

    def receive(self, msg):
        if msg.type == 'note_on' and msg.velocity != 0:
            self.array.append((msg.note, time.time()))

    def renew(self):
        while(1):
            for i in range(len(self.array)-1,-1,-1): 
                note = self.array[i] 
                if time.time() - note[1] > PT + SHOW:
                    self.light.off(note[0] - LOFF)
                    self.array.pop(i)
                    continue
                color = self.calc(note[1])
                self.light.on(note[0] - LOFF, color)
            time.sleep(ITV)


    def calc(self, t):
        cur = time.time()
        if cur - t > PT:
            return (255,255,0)
        return (int((cur - t)/PT*255), int((cur - t)/PT*255),0)

    def play(self, name):
        #print("given name: " + str(name))
        #name = 'Resources/midi/mozart.mid'
        path = 'Resources/midi/' + str(name) + '.mid'
        mz = mido.MidiFile(path)
        
        self.play_time = mz.length
        DELAY = 3 
        self.playing = True
        for msg in mz:
            time.sleep(msg.time * DELAY)
            self.receive(msg)
    
    def this_runtime(self):
        return self.play_time or 1000


if __name__ == '__main__':
    #ctr = Contr()
    #mz = mido.MidiFile('../Resources/midi/mozart.mid')
    #DELAY = 2 
    #for msg in mz:
    #    time.sleep(msg.time * DELAY)
    #    ctr.receive(msg)
    l = Lights(71)
    mm = MIDI(lambda x: l.on(x.note, (255,0,0) if x.type == 'note_on' else l.off(x.note)))
    mm.receive()
