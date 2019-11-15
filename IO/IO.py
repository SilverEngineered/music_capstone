
import board
from neopixel import NeoPixel
import mido
import time
import rtmidi
import threading
import time

class IO(object):
	def __init__(self, num_keys, notes, times):
		self.num_keys = num_keys
		self.notes = notes
		self.times = times
		self.pixels = NeoPixel(board.D18, self.num_keys)
		self.inputs = mido.get_input_names()
		self.queue = []
		self.pause = False
		self.BLUE = (0, 0, 255)
		self.RED = (255, 0, 0)
		self.OFF = (0, 0, 0)

	def listen(self):
		with mido.open_input(self.inputs[0]) as port:
			start = time.time()
			for msg in port:
				if not self.pause:
					self.queue.append((msg, time.time() - start))

	def light(self, key, color):
		print("lighting")
		if key <= self.num_keys:
			self.pixels[key] = color

	def light_many(self, notes, color):
		for i in notes:
			self.light(i, color)

	def reset_queue(self):
		self.queue = []

	def pop(self):
		self.queue.pop(-1)

	def threaded_listen(self):
		listen_thread = threading.Thread(target=self.listen)
		listen_thread.start()

	def set_notes(self, notes):
		self.notes = notes

	def set_times(self, times):
		self.times = times

	def play(self):
		for i in range(len(self.notes)):
			self.light_many(self.notes[i], self.BLUE)
			if i != len(self.notes - 1):
				time.sleep(self.times[i])
				self.light_many(self.notes[i], self.OFF)
			else:
				self.light_many(self.notes[i], self.RED)
				time.sleep(5)
				self.light_many(self.notes[i], self.OFF)

