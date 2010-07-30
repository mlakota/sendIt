class fileRead(object):
	def __init__(self, fileName):
		self.fileHandle = open(fileName,"rb")

	def give(self, howMany):
		return self.fileHandle.read(howMany)

	def close(self):
		self.fileHandle.close()



class genRead(object):
	def __init__(self, howMany):
		self.howMany = howMany

	def give(self, howMany):
		temp = min(self.howMany,howMany)
		self.howMany -= temp
		return 'a'* temp

	def close(self):
		pass
