class bufor(object):
	def __init__(self,input,output,howMany):
		self.input = input
		self.output = output
		self.howMany = howMany

	def run(self):
		theList = []
		while 1:
			temp = self.input.give(self.howMany)
			if not temp:
				self.input.close()
				self.output.close()
				break
			self.output.take(temp)

	def close(self):
		self.fileHandle.close()
