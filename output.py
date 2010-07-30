class fileWrite(object):
	def __init__(self,fileName):
		self.fileHandle = open(fileName,"wb")
	
	def take(self, data):
		self.fileHandle.write(data)

	def close(self):
		self.fileHandle.close()
