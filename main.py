def main(lista):
	if lista[0] == '--source-file':
		source = lista[1]
		if lista[2] == '--bufor':
			bufor = lista[3]
			if lista[4] == '--dest-file':
				dest = lista[5]
				send(source,bufor,dest)

def send(source,bufor,dest):
	pass



if __name__ == '__main__':
	main('--source-file ale --bufor 1000000 --dest-file kot'.split())
	#
