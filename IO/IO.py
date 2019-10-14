import board
from neopixel import NeoPixel
import mido
import time
import rtmidi

class IO(object):
	def __init__(self, num_keys):
		self.num_keys = num_keys
		self.pixels = NeoPixel(board.D18, self.num_keys)
		self.inputs = mido.get_input_names()

	def listen(self, duration):
		msg_list = []
		start = time.time()
		with mido.open_input(self.inputs[0]) as port:
			if time.time() - start > duration:
				for msg in port:
					msg_list.append(msg)
			return msg_list

	def light(self, key, color):
		print("lighting")
		self.pixels[key] = color