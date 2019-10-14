import board
from neopixel import NeoPixel

class IO(object):
	def __init__(self, num_keys):
		self.num_keys = num_keys
		self.pixels = NeoPixel(board.D18, self.num_keys)


	def listen(self):
		print("listening")

	def light(self,key):
		print("lighting")
		self.pixels[key] = (255, 255, 255)