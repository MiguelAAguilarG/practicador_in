def extractor_filas(titulo_archivo_subtitulos):
	from io import open

	archivo_subtitulos = open(titulo_archivo_subtitulos,'r')
	lista_texto = archivo_subtitulos.readlines()
	archivo_subtitulos.close()

	lista_texto_a_utilizar = []

	for linea in lista_texto:

		if linea.find('<') != -1 and linea.find('>') != -1:
			while linea.find('<') != -1 and linea.find('>') != -1:

				menor = linea.find('<')
				mayor = linea.find('>')

				linea = linea[:menor] + linea[mayor+1:]
		
			lista_texto_a_utilizar.append(linea)

	return lista_texto_a_utilizar

def creador_archivo_palabras_a_traducir(titulo_archivo_palabras_a_traducir, lista_a_escribir):
	from io import open

	archivo_palabras_a_traducir = open(titulo_archivo_palabras_a_traducir,'w')
	archivo_palabras_a_traducir.writelines([ele+'\n' for ele in lista_a_escribir])
	archivo_palabras_a_traducir.close()

def lector_archivo_palabras_traducidas(titulo_archivo_palabras_traducidas):
	from io import open

	archivo_palabras_traducidas = open(titulo_archivo_palabras_traducidas,'r')
	lista_palabras_traducidas = archivo_palabras_traducidas.readlines()
	archivo_palabras_traducidas.close()

	for x in range(len(lista_palabras_traducidas)):
		lista_palabras_traducidas[x] = lista_palabras_traducidas[x][:-1]

	return lista_palabras_traducidas

def extractor_palabras(lista_texto_a_utilizar):

	lista_palabras_a_utilizar = []
	for elemento in lista_texto_a_utilizar:
		lista_auxiliar = elemento.split(' ')
		for palabra in lista_auxiliar:
			palabra = palabra.replace('\n', '')
			palabra = palabra.lower()
			lista_palabras_a_utilizar.append(palabra)

	return lista_palabras_a_utilizar

def verificador_duplicidad(lista_base, lista_a_verificar):

	lista_auxiliar = []
	for x in lista_a_verificar:
		if not x in lista_auxiliar:
			lista_auxiliar.append(x)

	lista_a_verificar = lista_auxiliar

	lista_general = []
	for x in lista_a_verificar:
		if not x in lista_base:
			lista_general.append(x)

	return lista_general


def impresor_lista_traductor(lista_general, longitud):

	lista_a_traducir = []
	n = 0
	x = 0
	while x < len(lista_general):
		y = 1

		lista_a_traducir.append([])

		while y <= longitud:
			if x < len(lista_general):
				lista_a_traducir[n].append(lista_general[x])
			y = y+1
			x = x+1

		n = n +1

	return lista_a_traducir


def impresor_lista_final(lista_0, lista_1, titulo, indice, lon, longitud):

	lista = []
	n = 0
	x = 0
	while x < len(lista_0):
		y = 1

		lista.append([])
		lista[n].append([f'{titulo} {lon}'])
		lista[n].append([f'{indice}{lon}'])
		lista[n].append([])
		lista[n].append([])


		while y <= longitud:
			if x < len(lista_0):
				lista[n][2].append(lista_0[x])
				lista[n][3].append(lista_1[x])
			y = y+1
			x = x+1

		n = n+1
		lon = lon + 1

	for n in range(len(lista)):
		print(f'''
		n = n+1
		lista.append([])
		lista[n].append({lista[n][0]})
		lista[n].append({lista[n][1]})
		lista[n].append({lista[n][2]})
		lista[n].append({lista[n][3]})''')

if __name__ == '__main__':
	import lista

	lista_texto_a_utilizar = extractor_filas('The Fastest Xbox of All Time (inglés_ASR).srt')
	lista_palabras_a_utilizar = extractor_palabras(lista_texto_a_utilizar)

	lista_auxiliar = lista.lista()
	lista_base = []
	for x in lista_auxiliar:
		for y in x[2]:
			lista_base.append(y)

	lista_general = verificador_duplicidad(lista_base, lista_palabras_a_utilizar)

	creador_archivo_palabras_a_traducir('salida.txt', lista_general)

	lista_palabras_traducidas = lector_archivo_palabras_traducidas('traduccion.txt')

	impresor_lista_final(lista_general, lista_palabras_traducidas, 'palabras random', 'pran', 1, 8)

	input()