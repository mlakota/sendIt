class bufor(object):
	def __init__(self,input,output,howMany):
		self.input = input
		self.output = output
		self.howMany = howMany

	def run(self):
		theList = []
		while 1:
			temp = input.give(howMany)
			if not temp:
				input.close()
				output.close()
				break
			output.take(temp)


	def close(self):
		self.fileHandle.close()
