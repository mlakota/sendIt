import bufor
import input
import output

def main(lista):
	source = dest = bufSize = i = 0
	while i<len(lista):
		if not source:
			if lista[i] == '--source-file':
				source = input.fileRead(lista[i+1])
				i+=2
			elif lista[i] == '--source-gen':
				source = input.genRead(int(lista[i+1]))
				i+=2
			else: raise RuntimeError("Unknown parameter:" + lista[i])
		elif not bufSize:
			if lista[i] == '--bufor':
				bufSize = int(lista[i+1])
				i+=2
		elif not dest:
			if lista[i] == '--dest-file':
				dest = output.fileWrite(lista[i+1])
				i+=2
			elif lista[i] == '--path':
				parse = __parsePath(lista[i+1],lista[i+2:])
				if parse[0] is not None:
					dest = parse[0]
				else: raise RuntimeError('Bad parameter:'+lista[i+1])
				i+=parse[1]
		else:
			break
	bufor.bufor(source,dest,bufSize).run()

def send(source,bufor,dest):
	plik = open(source,"rb")
	plik2 = open(dest,"wb")
	while 1:
		temp = plik.read(bufor)
		if not temp:
			break
		plik2.write(temp)


def __parsePath(path, args):
	pass

def __parseElem(path, args):
	pass

if __name__ == '__main__':
	# test1: file->file (local)
	main('--source-file ala --bufor 1000000 --dest-file kot'.split())
	# test2: gen->file (local)
	main('--source-gen 7 --bufor 100 --dest-file kot0'.split())
	# test3: file->splitter [without cmdLine]
	source = input.fileRead('ala')
	dest = output.fileWrite('kot1')
	dest2 = output.fileWrite('kot2')
	dest3 = output.fileWrite('kot3')
	bufor.bufor(source,
		output.splitter(
			dest,
			output.splitter(dest2,dest3)
		)
	,10000).run()
	# test4: gen->splitter [using cmdLine]
	#main('--source-gen 20 --bufor 203 --path'.split() + 
	#	["%2s %f %3s %f %f %f"] + 
	#	'kot4 kot5 kot6 kot7'.split())
