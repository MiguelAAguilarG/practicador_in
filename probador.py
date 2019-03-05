import lista
import os

#lista.contador()
#input()

while True:
	os.system('cls')
	palabra = input('Inserte palabra a encontrar en la lista general: ')
	parametro = input('Inserte idioma [ingles (por defecto o 1)/español o 2]: ')
	lista.encontrador(palabra, parametro)

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

'''from io import open

titulo_archivo_subtitulos = 'uno.txt'

archivo_subtitulos = open(titulo_archivo_subtitulos,'r')
lista_texto = archivo_subtitulos.readlines()
archivo_subtitulos.close()

util = []

for linea in lista_texto:

	if linea.find('-') != -1:
		division = linea.find('-')

		parte_util = linea[division+1:]

		util.append(parte_util)

for i,x in enumerate(util):

	util[i] = util[i].replace('\n', '')
	util[i] = util[i].strip(' ')
	util[i] = util[i].lower()

print(util)

lo = []
for x in range(len(util)):
	lo.append(str(x+1)+'.txt')

print(lo)'''

'''
titulo = ['partes de la ciudad', 'tiendas y comercios', 'problemas de salud y enfermedades', 'medicinas y remedios', 'el hospital', 'el cuerpo humano', 'partes de la casa', 'el cuarto del bebé', 'el baño', 'el dormitorio', 'el comedor', 'el jardín', 'la cocina', 'la sala', 'el cuarto de servicio', 'taller y herramientas', 'las flores', 'geografía', 'plantas y árboles', 'el universo y el cosmos', 'el tiempo', 'familia y parientes', 'trabajos y profesiones', 'sentimientos y emociones', 'estados de ánimo', 'ropa de hombre', 'ropa de mujer', 'personalidad (rasgos positivos)', 'personalidad (rasgos negativos)', 'países', 'delitos y justicia', 'militares y guerra', 'armas', 'nacionalidades', 'política y gobierno', 'religión', 'escuela y educación', 'colores y patrones', 'envases y cantidades', 'materiales y telas', 'formas y texturas', 'calendario y tiempo', 'puntos en el tiempo', 'aeropuerto y aviones', 'medios de transporte', 'el automóvil', 'la bicicleta', 'las embarcaciones', 'el barco']
numero = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt', '8.txt', '9.txt', '10.txt', '11.txt', '12.txt', '13.txt', '14.txt', '15.txt', '16.txt', '17.txt', '18.txt', '19.txt', '20.txt', '21.txt', '22.txt', '23.txt', '24.txt', '25.txt', '26.txt', '27.txt', '28.txt', '29.txt', '30.txt', '31.txt', '32.txt', '33.txt', '34.txt', '35.txt', '36.txt', '37.txt', '38.txt', '39.txt', '40.txt', '41.txt', '42.txt', '43.txt', '44.txt', '45.txt', '46.txt', '47.txt', '48.txt', '49.txt']
indice = ['pdlc', 'tyc', 'pdsye', 'myr', 'eh', 'ech', 'pdlc', 'ecdb', 'eb', 'ed', 'ec', 'ej', 'lc', 'ls', 'ecds', 'tyh', 'lf', 'g', 'pyá', 'euyec', 'et', 'fyp', 'typ', 'sye', 'edá', 'rdh', 'rdm', 'p(p', 'p(n', 'p', 'dyj', 'myg', 'a', 'n', 'pyg', 'r', 'eye', 'cyp', 'eyc', 'myt', 'fyt', 'cyt', 'peet', 'aya', 'mdt', 'ea', 'lb', 'le', 'eb']
'''
'''lista_indice = []
for i,x in enumerate(titulo):

	partido = titulo[i].split(' ')

	indice = ''
	for a,b in enumerate(partido):
		indice = indice + b[0]

	lista_indice.append(indice)

print(lista_indice)'''

input('FIN')