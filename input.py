class FileRead(object):
	def __init__(self, fileName):
		self.fileHandle = open(fileName,"rb")

	def give(self, howMany):
		return self.fileHandle.read(howMany)

