class fileWrite(object):
	def __init__(self,fileName):
		self.fileHandle = open(fileName,"wb")
	
	def take(self, data):
		self.fileHandle.write(data)

	def close(self):
		self.fileHandle.close()

class splitter(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def take(self, data):
		self.a.take(data)
		self.b.take(data)

	def close(self):
		self.a.close()
		self.b.close()
