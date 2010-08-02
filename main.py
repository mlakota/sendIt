import bufor
import input
import output

def main(lista):
	if lista[0] == '--source-file':
		source = input.fileRead(lista[1])
	elif lista[0] == '--source-gen':
		source = input.genRead(int(lista[1]))
	else:
		raise RuntimeError("Unknown parameter:" + lista[0])

	if lista[2] == '--bufor':
		if lista[4] == '--dest-file':
			dest = output.fileWrite(lista[5])
			bufor.bufor(source,dest,int(lista[3])).run()

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
	main('--source-file ala --bufor 1000000 --dest-file kot'.split())
	main('--source-gen 7 --bufor 100 --dest-file kot'.split())
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
	main('--source-gen 20 --bufor 203 --path'.split() + 
		["%2s %f %3s %f %f %f"] + 
		'kot1 kot2 kot3 kot4'.split())
