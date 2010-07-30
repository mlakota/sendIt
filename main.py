import bufor
import input
import output

def main(lista):
	if lista[0] == '--source-file':
		source = lista[1]
		if lista[2] == '--bufor':
			bufor = int(lista[3])
			if lista[4] == '--dest-file':
				dest = lista[5]
				send(source,bufor,dest)
	else:
		raise RuntimeError("Unknown parameter:" + lista[0])

def send(source,bufor,dest):
	plik = open(source,"rb")
	plik2 = open(dest,"wb")
	while 1:
		temp = plik.read(bufor)
		if not temp:
			break
		plik2.write(temp)


def gen(howMany):
	pass


if __name__ == '__main__':
	main('--source-file ala --bufor 1000000 --dest-file kot'.split())
#	main('--source-gen 10032410 --bufor 1000000 --dest-file kot'.split())
