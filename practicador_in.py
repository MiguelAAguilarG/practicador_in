import random
import os
import lista

lista = lista.lista() #Se carga la lista general, se usa en la función 'constructor'
lista_de_repeticion = [] #Lista auxiliar para la función 'constructor'
rango = 5 #Número de las ultimas sub-listas que se imprimirán al iniciar el programa

def constructor(lista_del_constructor,lista_de_repeticion_del_constructor,limpia_del_constructor):
	'''Los palabras de las listas se dan a traducir de forma aleatoria, sin repetir ninguna palabra, hasta que se haya completado la lista,
	cuentan las traducciones erroneas

	Esta función hace posible esto
	#Si 'limpia_del_constructor' es 'False' la lista elegida seguira mostrandose aleatoriamente, pero se repetiran las palabras de la lista sin que se alla mostrado la lista completa
	'''
	numeros_buscar_lista = [x for x in range(len(lista_del_constructor))]

	if (len(lista_de_repeticion_del_constructor) == len(lista_del_constructor)) and (limpia_del_constructor == True):
		del lista_de_repeticion_del_constructor[:]

	for x in lista_de_repeticion_del_constructor:
		numeros_buscar_lista.remove(x)

	r = random.choice(numeros_buscar_lista)

	if limpia_del_constructor == True:
		lista_de_repeticion_del_constructor.append(r)

	return r, lista_del_constructor[r], lista_de_repeticion_del_constructor

def verificador_traductor(lista_del_verificador_traductor, forma, etapa_2, lista_de_repeticion_del_verificador_traductor, c1, e1, c2, e2, limpia_ingresada_del_verificador_traductor = True):
	'''Se verifica la validez de la traduccíón según condiciones elegidas por el usuario'''

	if forma == '2':
		lista1 = lista_del_verificador_traductor[3]
		lista2 = lista_del_verificador_traductor[2]
	else:
		lista1 = lista_del_verificador_traductor[2]
		lista2 = lista_del_verificador_traductor[3]

	indice, variable, lista_de_repeticion_del_constructor = constructor(lista1, lista_de_repeticion_del_verificador_traductor, limpia_ingresada_del_verificador_traductor)

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
		c1 = c1 + 1
	else:
		print('MAL')
		e1 = e1 + 1

	if not etapa_2 == 'n':
		if forma == '2':
			lista1 = lista_del_verificador_traductor[2]
			lista2 = lista_del_verificador_traductor[3]
		else:
			lista1 = lista_del_verificador_traductor[3]
			lista2 = lista_del_verificador_traductor[2]

		os.system('cls')
		print(lista1[indice])
		if traduccion >= definiciones:
			print('BIEN')
		else:
			print('MAL')
		print('*****************')

		insercion = input('palabra/frase: \n').lower()
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
			c2 = c2 + 1
		else:
			print('MAL')
			e2 = e2 + 1

	return c1, e1, c2, e2, lista_de_repeticion_del_constructor

def impresor1(rango = rango, lista = lista):
	'''Imprime todas las listas que posee el programa'''
	descripcion_listas = ['lista','idenficador','inglés','español']

	for x in range(len(lista)):#listas
		if rango >= (len(lista)-x):
			print(f'---{x+1}---')
			print(f'-----<{descripcion_listas[0]}>')
			print(f'--1-. {lista[x][0][0]}')
			print(f'-----<{descripcion_listas[1]}>')
			print(f'--1-. {lista[x][1][0]}')

			a = []
			for y in range(len(lista[x])):#sublistas
				if y%2 == 0:
					n = 2
				else:
					n = 3

				if y >= 2:
					a.append(len(descripcion_listas[n]))
				else:
					a.append(1)

				for z in range(len(lista[x][y])):#ver longitud mayor
					if len(lista[x][y][z]) > a[y]:
						a[y] = len(lista[x][y][z])

			b = descripcion_listas[2]+'>'
			c = descripcion_listas[3]+'>'
			print(f'{"":-<{5}}<{b:-<{a[2]+2}}<{c: <{a[3]+2}}', end = '')
			for y in range(4,len(lista[x]),2):#sublistas
				b = descripcion_listas[2]+'>'
				c = descripcion_listas[3]+'>'
				print(f'<{b:-<{a[y]+2}}<{c: <{a[y+1]+2}}', end = '')		
			print('')
			
			z = 0
			while z < len(lista[x][2]):

				if z < 9:
					rep = 2
				else:
					rep = 1

				yy = 2
				while yy < len(lista[x]):
					if yy == 2:
						print(f'-{z+1}{"-"*rep}. {lista[x][yy][z]:_<{a[yy]+3}}{lista[x][yy+1][z]: <{a[yy+1]+3}}', end = '')
					else:
						print(f'{lista[x][yy][z]:_<{a[yy]+3}}{lista[x][yy+1][z]: <{a[yy+1]+3}}', end = '')
					yy = yy + 2
				print('')

				z = z + 1
			print('')

def impresor1_2(rango = rango, lista = lista):
	'''Imprime todos los nombres de las listas con identificadores'''
	descripcion_listas = ['lista','idenficador','inglés','español']

	for x in range(len(lista)):#listas
		if rango >= (len(lista)-x):
			print(f'---{x+1}---')
			for y in range(2):#sublistas
				print(f'----<{descripcion_listas[y]}>')
				print(f'---- {lista[x][y][0]}')
			print('')

def impresor2(modo,indice,forma,lista = lista):
	'''Imprime la lista seleccionada'''

	if not (modo == 'd' or modo == 'm'):
		if forma == '2':
			descripcion_listas = ['lista','idenficador','español','inglés']
			lista1 = lista[indice][3]
			lista2 = lista[indice][2]
		else:
			descripcion_listas = ['lista','idenficador','inglés','español']
			lista1 = lista[indice][2]
			lista2 = lista[indice][3]

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
		c1 = 0
		e1 = 0
		c2 = 0
		e2 = 0
		i = 0

		os.system('cls')
		print('---Programa para practicar palabras en inglés---')
		print('Se mostrarán varias listas de palabras en inglés con tematicas diferentes para elegir\n')
		print('->Ingrese nivel de dificultad<-')
		print('> FÁCIL: Cada que se tenga que traducir una palabra, se mostrara con anterioridad la lista elegida')
		print('>> MEDIO: Cada que se tenga que traducir una palabra, YA NO se mostrara con anterioridad la lista elegida')
		print('>>> DIFÍCIL: Igual que MEDIO y se tendrán que dar todos los significados de la palabra')

		dificultad = input('\nDIFÍCIL [d]/ MEDIO [m]/ FÁCIL [Cualquier tecla]: ').lower()
		print('\nTraducir del:')
		forma = input('ETAPA 1: inglés --> español [Cualquier tecla] español --> inglés [2]: ')
		etapa_2 = input('ETAPA 2: En cada intento ingresar la misma palabra/frase a traducir: si [Cualquier tecla] no [n]: ')
		os.system('cls')

		impresor1()#Se imprime la lista general
		impresor1_2()#Se imprime la lista general con solo indicadores
		indice_identificador, identificador = seleccionador_opciones_listas()#Se selecciona una lista
		
		while validacion == '':

			os.system('cls')
			impresor2(dificultad,indice_identificador,forma)#Se imprime la lista elegida
			os.system('cls')
			c1, e1, c2, e2, lista_de_repeticion = verificador_traductor(lista[indice_identificador], forma, etapa_2, lista_de_repeticion, c1, e1, c2, e2) #Se verifica lo ingresado

			print(f'intentos: {i+1}')#Te muestra los intentos que llevas en la misma lista
			validacion = input('Continuar con la misma lista [enter]/ Seleccionar otra lista[Cualquier tecla]: ')
			os.system('cls')
			i = i + 1

		print('intentos')
		print(i)
		print('\ncorrectos/ETAPA 1')
		print(c1)
		print('incorrectos/ETAPA 1')
		print(e1)
		if not etapa_2 == 'n':
			print('\ncorrectos/ETAPA 2')
			print(c2)
			print('incorrectos/ETAPA 2')
			print(e2)

		validacion_fin = input('\nContinuar [enter]/ Salir [Cualquier tecla]: ')

	input('FIN')