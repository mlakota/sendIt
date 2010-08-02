class fileRead(object):
	def __init__(self, fileName):
		self.fileHandle = open(fileName,"rb")

	def give(self, howMany):
		return self.fileHandle.read(howMany)

	def close(self):
		self.fileHandle.close()

	def __str__(self):
		return "fileRead: "+str(self.fileHandle.name)

	__repr__ = __str__


class genRead(object):
	def __init__(self, howMany):
		self.howMany = howMany

	def give(self, howMany):
		temp = min(self.howMany,howMany)
		self.howMany -= temp
		return 'a'* temp

	def close(self):
		pass

	def __str__(self):
		return "genRead: size "+str(self.howMany)

	__repr__ = __str__
