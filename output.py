class fileWrite(object):
	def __init__(self,fileName):
		self.fileHandle = open(fileName,"wb")

	def take(self, data):
		self.fileHandle.write(data)

	def close(self):
		self.fileHandle.close()

	def __str__(self):
		return "fileWrite:"+str(self.fileHandle.name)

	__repr__ = __str__


class splitter(object):
	def __init__(self, *args):
		if isinstance(args[0],list):
			self.ways = list(args[0])
		else:
			self.ways = list(args)

	def take(self, data):
		for i in self.ways:
			i.take(data)

	def close(self):
		for i in self.ways:
			i.close()

	def __str__(self):
		aList = ['splitter(']
		for i in self.ways:
			aList.append(str(i))
			aList.append(',')
		aList.pop()
		aList.append(')')
		from string import join
		return join(aList)

	__repr__ = __str__
