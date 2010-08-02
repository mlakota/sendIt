class fileWrite(object):
	def __init__(self,fileName):
		self.fileHandle = open(fileName,"wb")
	
	def take(self, data):
		self.fileHandle.write(data)

	def close(self):
		self.fileHandle.close()

class splitter(object):
	def __init__(self, *args):
		self.ways = list(args)

	def take(self, data):
		for i in self.ways:
			i.take(data)

	def close(self):
		for i in self.ways:
			i.close()
