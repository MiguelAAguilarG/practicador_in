import random
import os
import lista

lista = lista.lista()#Se carga la lista general, se usa en la función 'constructor'
lista_de_repeticion = []#Lista auxiliar para la función 'constructor'

def constructor(lista_del_constructor,lista_de_repeticion_del_constructor,limpia_del_contructor):
	'''Los palabras de las listas se dan a traducir de forma aleatoria, sin repetir ninguna palabra, hasta que se haya completado la lista,
	cuentan las traducciones erroneas

	Esta función hace posible esto
	#Si 'limpia_del_constructor' es 'False' la lista elegida seguira mostrandose aleatoriamente, pero se repetiran las palabras de la lista sin que se alla mostrado la lista completa
	'''
	numeros_buscar_lista = [x for x in range(len(lista_del_constructor))]
	
	while True:
		r = random.choice(numeros_buscar_lista)

		if not r in lista_de_repeticion_del_constructor:
			if limpia_del_contructor == True:
				lista_de_repeticion_del_constructor.append(r)
			return r, lista_del_constructor[r]

		if (len(lista_de_repeticion_del_constructor) == len(lista_del_constructor)) and (limpia_del_contructor == True):
			del lista_de_repeticion_del_constructor[:]

def verificador_traductor(lista_del_verificador_traductor, forma, lista_de_repeticion_del_verificador_traductor = lista_de_repeticion, limpia_ingresada_del_verificador_traductor = True):
	'''Se verifica la validez de la traduccíón según condiciones elegidas por el usuario'''

	if forma == '1':
		lista1 = lista_del_verificador_traductor[2]
		lista2 = lista_del_verificador_traductor[3]
	else:
		lista1 = lista_del_verificador_traductor[3]
		lista2 = lista_del_verificador_traductor[2]

	indice, variable = constructor(lista1,lista_de_repeticion_del_verificador_traductor,limpia_ingresada_del_verificador_traductor )

	print('--{}---'.format(variable))

	insercion = input('Traducción: \n').lower()
	insercion = insercion.split(',')

	for i,x in enumerate(insercion):
		insercion[i] = insercion[i].strip(' ')

	traduccion_aux = lista2[indice].split(',')
	traduccion = 0

	for i,x in enumerate(traduccion_aux):
		traduccion_aux[i] = traduccion_aux[i].strip(' ')

	for x in traduccion_aux:
		for y in insercion:
			if x == y:
				traduccion = traduccion + 1;

	print(lista2[indice].strip(' '))

	if dificultad == 'd':
		if not traduccion_aux[-1].find('-') == -1:
			definiciones = len(traduccion_aux)-1
		else:
			definiciones = len(traduccion_aux)
	else:
		definiciones = 1

	if traduccion >= definiciones:
		print('BIEN')
		global c
		c = c + 1
	else:
		global e
		print('MAL')
		e = e + 1

def impresor1(lista = lista):
	'''Imprime todas las listas que posee el programa'''
	descripcion_listas = ['lista','idenficador','inglés','español']

	for x in range(len(lista)):#listas
		print(f'---{x+1}---')
		for y in range(len(lista[x])-1):#sublistas
			a = len(descripcion_listas[2])
			for z in range(len(lista[x][y])):#ver longitud mayor
				if len(lista[x][y][z]) > a:
					a = len(lista[x][y][z])
			if y == 2:
				b = descripcion_listas[y]+'>'
				print(f'-----<{b:-<{a+2}}<{descripcion_listas[y+1]}>')
			else:
				print(f'-----<{descripcion_listas[y]}>')
			for z in range(len(lista[x][y])):#elementos de listas
				if y == 2:
					if z < 9:
						print(f'-{z+1}--. {lista[x][y][z]:_<{a+3}}{lista[x][y+1][z]}')
					else:
						print(f'-{z+1}-. {lista[x][y][z]:_<{a+3}}{lista[x][y+1][z]}')
				else:
					print(f'--{z+1}-. {lista[x][y][z]}')
		print('')

def impresor2(modo,indice,forma,lista = lista):
	'''Imprime la lista seleccionada'''

	if not (modo == 'd' or modo == 'm'):
		if forma == '1':
			descripcion_listas = ['lista','idenficador','inglés','español']
			lista1 = lista[indice][2]
			lista2 = lista[indice][3]
		else:
			descripcion_listas = ['lista','idenficador','español','inglés']
			lista1 = lista[indice][3]
			lista2 = lista[indice][2]

		print(f'---{indice+1}---')
		for y in range(len(lista[indice])-1):#sublistas
			if y == 2:
				a = len(descripcion_listas[2])
				for z in range(len(lista1)):#ver longitud mayor
					if len(lista1[z]) > a:
						a = len(lista1[z])

				b = descripcion_listas[y]+'>'
				print(f'-----<{b:-<{a+2}}<{descripcion_listas[y+1]}>')
			else:
				print(f'-----<{descripcion_listas[y]}>')
			for z in range(len(lista[indice][y])):#elementos de listas
				if y == 2:
					if z < 9:
						print(f'-{z+1}--. {lista1[z]:_<{a+3}}{lista2[z]}')
					else:
						print(f'-{z+1}-. {lista1[z]:_<{a+3}}{lista2[z]}')
				else:
					print(f'-{z+1}--. {lista[indice][y][z]}')
		input('Continuar [enter]: ')

def impresor1_2(lista = lista):
	'''Imprime todos los nombres de las listas con identificadores'''
	descripcion_listas = ['lista','idenficador','inglés','español']

	for x in range(len(lista)):#listas
		print(f'---{x+1}---')
		for y in range(2):#sublistas
			print(f'----<{descripcion_listas[y]}>')
			print(f'---- {lista[x][y][0]}')
		print('')

def seleccionador_opciones_listas():
	'''Función para seleccionar una lista de palabras especifica'''

	while True:
		print('Seleccione una lista')
		identificador = input('Ingresar identificador o número de lista: ').lower()

		try:
			i = int(identificador)-1
			if i <= len(lista)-1 and i >= 0:
				identificador = lista[i][1]
				return i, identificador
			else:
				print('ERROR. No es un número de lista valido')
		except:
			for i,x in enumerate(lista):
				if identificador == x[1][0]:
					return i, identificador
			else:
				print('ERROR. No es un identificador')

		input('Continuar [enter]: ')
		os.system('cls')
		impresor1()
		impresor1_2()

if __name__ == '__main__':

	validacion_fin = ''
	while validacion_fin == '':
		del lista_de_repeticion[:] #Se borra la 'lista_de_repetición' cada vez que se elige nueva lista
		validacion = ''
		i=0
		c=0
		e=0

		os.system('cls')
		print('---Programa para practicar palabras en inglés---')
		print('Se mostrarán varias listas de palabras en inglés con tematicas diferentes para elegir\n')
		print('->Ingrese nivel de dificultad<-')
		print('> FÁCIL: Cada que se tenga que traducir una palabra, se mostrara con anterioridad la lista elegida')
		print('>> MEDIO: Cada que se tenga que traducir una palabra, YA NO se mostrara con anterioridad la lista elegida')
		print('>>> DIFÍCIL: Igual que MEDIO y se tendrán que dar todos los significados de la palabra')

		dificultad = input('\nDIFICIL [d]/ MEDIO [m]/ FACIL [Cualquier tecla]: ').lower()
		print('\nTraducir del:')
		forma = input('inglés --> español (1) español --> inglés (2): ')
		os.system('cls')

		impresor1()#Se imprime la lista general
		impresor1_2()
		indice_identificador, identificador = seleccionador_opciones_listas()#Se selecciona una lista

		while validacion == '':

			os.system('cls')
			impresor2(dificultad,indice_identificador,forma)#Se imprime la lista elegida
			os.system('cls')
			verificador_traductor(lista[indice_identificador], forma = forma)#Se verifica lo ingresado

			print(f'intentos: {i+1}')#Te muestra los intentos que llevas en la misma lista
			validacion = input('Continuar con la misma lista [enter]/ Seleccionar otra lista[Cualquier tecla]: ')
			os.system('cls')
			i = i + 1

		print('intentos')
		print(i)
		print('correctos')
		print(c)
		print('incorrectos')
		print(e)

		validacion_fin = input('Continuar [enter]/ Salir [Cualquier tecla]: ')

	input('FIN')