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




if __name__ == '__main__':
	main('--source-file ala --bufor 1000000 --dest-file kot'.split())
#	main('--source-gen 10032410 --bufor 1000000 --dest-file kot'.split())
