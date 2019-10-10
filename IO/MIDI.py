from midi import MidiConnector
from midi import Message
conn = MidiConnector()
msg = Message(cc, channel=1)
while(1):
  print (msg)