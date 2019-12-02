from IO2 import *
import mido
import rtmidi
import threading

ITV=0.01
PT = 0.5
SHOW = 0.1
LOFF = 50

class Controller:
    def __init__(self):
        self.light = Lights(61)
        self.light.reset()
        self.array = []
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
        name = '../Resources/midi/elise.mid'
        m = mido.MidiFile(name)
        DELAY = 2
        for msg in mz:
            time.sleep(msg.time * DELAY)
            self.receive(msg)


if __name__ == '__main__':
    #light = Lights(61)
    #light.reset()
    ctr = Controller()
    mz = mido.MidiFile('../Resources/midi/mozart.mid')
    DELAY = 2 
    for msg in mz:
        time.sleep(msg.time * DELAY)
        ctr.receive(msg)

