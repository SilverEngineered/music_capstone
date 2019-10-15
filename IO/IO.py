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
		self.queue = []
		self.pause = False

	def listen(self):
		with mido.open_input(self.inputs[0]) as port:
			start = time.time()
			for msg in port:
				if not self.pause:
					self.queue.append((msg, time.time() - start))

	def light(self, key, color):
		print("lighting")
		self.pixels[key] = color

	def reset_queue(self):
		self.queue = []

	def pop(self):
		self.queue.pop(-1)


	def threaded_listen(self):
		listen_thread = threading.Thread(target=self.listen)
		listen_thread.start()
