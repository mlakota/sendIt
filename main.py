def main(lista):
	if lista[0] == '--source-file':
		source = lista[1]
		if lista[2] == '--bufor':
			bufor = int(lista[3])
			if lista[4] == '--dest-file':
				dest = lista[5]
				send(source,bufor,dest)

def send(source,bufor,dest):
	plik = open(source)
	while 1:
		temp = plik.read(bufor)
		if not temp:
			break



if __name__ == '__main__':
	main('--source-file ala --bufor 1000000 --dest-file kot'.split())
