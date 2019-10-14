import Strip

class IO(object):
	def __init__(self, num_keys):
		self.num_keys = num_keys
		s = Strip(self.num_keys)

	def listen(self):
		pass

	def light(self):
		pass