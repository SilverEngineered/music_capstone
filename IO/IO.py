from Strip import Strip

class IO(object):
	def __init__(self, num_keys):
		self.num_keys = num_keys
		s = Strip(self.num_keys)

	def listen(self):
		print("listening")

	def light(self):
		print("lighting")