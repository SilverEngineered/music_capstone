import board
from neopixel import NeoPixel
import mido
import rtmidi

class IO(object):
	def __init__(self, num_keys):
		self.num_keys = num_keys
		self.pixels = NeoPixel(board.D18, self.num_keys)
		self.inputs = mido.get_input_names()

	def listen(self):
		with mido.open_input(self.inputs[0]) as port:
			for msg in port:
				print(msg)

	def light(self,key):
		print("lighting")
		self.pixels[key] = (255, 255, 255)