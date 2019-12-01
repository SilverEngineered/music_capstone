
import board
from neopixel import NeoPixel
import mido
import time
import rtmidi
import threading
import time

class IO(object):
	def __init__(self, num_keys, song_data):
		self.num_keys = num_keys
		self.song_data = song_data
		self.cur_song = None
		self.pixels = NeoPixel(board.D18, self.num_keys)
		self.inputs = mido.get_input_names()
		self.queue = []
		self.BLUE = (0, 0, 255)
		self.RED = (255, 0, 0)
		self.OFF = (0, 0, 0)
		self.playing = False

	def get_relative_times(self, times):
		new_times = []
		total_time = 0
		for i in times:
			new_times.append(i - total_time)
			total_time = i
		return new_times

	def listen(self):
		with mido.open_input(self.inputs[0]) as port:
			start = time.time()
			for msg in port:
				if self.play:
					self.queue.append((msg, time.time() - start))

	def light(self, key, color):
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

	def print_message(self, msg, time_i):
		print(str(time_i) + "---" + str(msg.type) + ":" + str(msg.note))

	def this_runtime(self):
		return sum(self.get_relative_times(self.song_data[self.cur_song]['times']))

	def play(self, song):
		self.cur_song = song
		notes = self.song_data[self.cur_song]['notes']
		times = self.get_relative_times(self.song_data[self.cur_song]['times'])
		self.reset_queue()
		self.playing = True
		self.threaded_listen()
		print("Started Play")
		for i in range(len(notes)):
			self.light_many(notes[i], self.BLUE)
			if i != len(notes) - 1:
				time.sleep(times[i])
				self.light_many(notes[i], self.OFF)
			else:
				self.light_many(notes[i], self.RED)
				time.sleep(5)
				self.light_many(notes[i], self.OFF)
		self.playing = False
		print("Ended Play")
		self.queue.sort(key=lambda x: x[1])
		for b_msg in self.queue:
			self.print_message(b_msg[0], b_msg[1])

