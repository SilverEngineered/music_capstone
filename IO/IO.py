import board
from neopixel import NeoPixel
import mido
import time
import rtmidi
import threading

class IO(object):
	def __init__(self, num_keys):
		self.num_keys = num_keys
		self.pixels = NeoPixel(board.D18, self.num_keys)
		self.inputs = mido.get_input_names()
		self.queue = [()]

	def listen(self, duration):
		msg_list = []
		with mido.open_input(self.inputs[0]) as port:
			start = time.time()
			for msg in port:
				if time.time() - start > duration:
					return msg_list
				else:
					msg_list.append((msg, start - time.time()))

	def light(self, key, color):
		print("lighting")
		self.pixels[key] = color