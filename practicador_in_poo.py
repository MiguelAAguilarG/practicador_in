import random
import os
import lista



class Inicio():
	"""docstring for ClassName"""
	def __init__(self):
		self.lista = lista.lista() #Se carga la lista general, se usa en la función 'constructor'
		self.lista_de_repeticion = [] #Lista auxiliar para la función 'constructor'
		self.c1 = 0
		self.e1 = 0
		self.c2 = 0
		self.e2 = 0
		self.i = 0

		self.mostrar_lista = 's'
		self.verificar_elementos = 1
		self.forma_traducir = '1'
		self.ingresar_mismo_elemento = 's'
		self.limite_inf_rango = 340
		self.limite_sup_rango = 342

	def modificar_parametros(self):
		os.system('cls')
		print('---Programa para practicar palabras en inglés---')
		print('Se mostrarán varias listas de palabras en inglés con tematicas diferentes para elegir\n')

		print(f'''***Parámetros por defecto***
-Mostar la lista seleccionada en cada palabra/frase a traducir: si[s]/ no[n]: {self.mostrar_lista}
--En palabras/frases con varias traducciones, para dar una respuesta por buena ¿cuántas traducciones tomar?: {self.verificar_elementos}
Traducir del:
ETAPA 1: inglés --> español [1] español --> inglés [2]: {self.forma_traducir}
ETAPA 2: En cada intento ingresar la misma palabra/frase a traducir: si [s] no [n]: {self.ingresar_mismo_elemento}
-límite inferior del rango de listas a imprimir: {self.limite_inf_rango}
--límite superior del rango de listas a imprimir: {self.limite_sup_rango}''')

		self.modificar = input('\nContinuar [enter]/ Modificar parámetros [Cualquier tecla]: ')

		if self.modificar == '':
			pass
		else:
			self.mostrar_lista = input('\n-Mostar la lista seleccionada en cada palabra/frase a traducir: si[s]/ no[n]: ').lower()
			self.verificar_elementos = int(input('\n--En palabras/frases con varias traducciones, para dar una respuesta por buena ¿cuántas traducciones tomar?: ').lower())
			print('\nTraducir del:')
			self.forma_traducir = input('ETAPA 1: inglés --> español [1] español --> inglés [2]: ')
			self.ingresar_mismo_elemento = input('ETAPA 2: En cada intento ingresar la misma palabra/frase a traducir: si [s] no [n]: ')
			self.limite_inf_rango = int(input('\n-límite inferior del rango de listas a imprimir: '))
			self.limite_sup_rango = int(input('--límite superior del rango de listas a imprimir: '))

	def seleccionador_opciones_listas(self):
		'''Función para seleccionar una lista de palabras especifica'''

		while True:
			print('Seleccione una lista')
			identificador = input('Ingresar identificador o número de lista: ').lower()

			try:
				i = int(identificador)-1
				if i <= len(self.lista)-1 and i >= 0:
					identificador = self.lista[i][1]
					self.indice_identificador = i
					self.identificador = identificador
					break
				else:
					print('ERROR. No es un número de lista valido')
			except:
				for i,x in enumerate(self.lista):
					if identificador == x[1][0]:
						self.indice_identificador = i
						self.identificador = identificador
						break
				else:
					print('ERROR. No es un identificador')

class Impresores(Inicio):
	"""docstring for Impresores"""
	def __init__(self):
		super().__init__()

	def impresor_total_listas(self):
		'''Imprime todas las listas que posee el programa'''
		descripcion_listas = ['lista','idenficador','inglés','español']

		ss1 = ''
		for x in range(len(self.lista)):#listas
			if self.limite_inf_rango-1 <= x and self.limite_sup_rango-1 >= x:
				s1 = f'---{x+1}---'
				s2 = f'\n-----<{descripcion_listas[0]}>'
				s3 = f'\n--1-. {self.lista[x][0][0]}'
				s4 = f'\n-----<{descripcion_listas[1]}>'
				s5 = f'\n--1-. {self.lista[x][1][0]}'

				a = []
				for y in range(len(self.lista[x])):#sublistas
					if y%2 == 0:
						n = 2
					else:
						n = 3

					if y >= 2:
						a.append(len(descripcion_listas[n]))
					else:
						a.append(1)

					for z in range(len(self.lista[x][y])):#ver longitud mayor
						if len(self.lista[x][y][z]) > a[y]:
							a[y] = len(self.lista[x][y][z])

				b = descripcion_listas[2]+'>'
				c = descripcion_listas[3]+'>'
				s6 = f'\n{"":-<{5}}<{b:-<{a[2]+2}}<{c: <{a[3]+2}}'
				s7 = ''
				for y in range(4,len(self.lista[x]),2):#sublistas
					b = descripcion_listas[2]+'>'
					c = descripcion_listas[3]+'>'
					s7 = s7 + f'<{b:-<{a[y]+2}}<{c: <{a[y+1]+2}}'	
				s8 = '\n'
				
				z = 0
				s9 = ''
				while z < len(self.lista[x][2]):

					if z < 9:
						rep = 2
					else:
						rep = 1

					yy = 2
					while yy < len(self.lista[x]):
						if yy == 2:
							s9 = s9 + f'-{z+1}{"-"*rep}. {self.lista[x][yy][z]:_<{a[yy]+3}}{self.lista[x][yy+1][z]: <{a[yy+1]+3}}'
						else:
							s9 = s9 + f'{self.lista[x][yy][z]:_<{a[yy]+3}}{self.lista[x][yy+1][z]: <{a[yy+1]+3}}'
						yy = yy + 2
					s9 = s9 + '\n'

					z = z + 1

				ss1 = ss1 + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + '\n'

		print(ss1)

	def impresor_total_identificadores(self):
		'''Imprime todos los nombres de las listas con identificadores'''
		descripcion_listas = ['lista','idenficador','inglés','español']

		ss1 = ''
		for x in range(len(self.lista)):#listas
			if self.limite_inf_rango-1 <= x and self.limite_sup_rango-1 >= x:
				s1 = f'\n---{x+1}---'

				s2 = ''
				s3 = ''
				for y in range(2):#sublistas
					s2 = s2 + f'\n----<{descripcion_listas[y]}>'
					s2 = s2 + f'\n---- {self.lista[x][y][0]}'

				ss1 = ss1 + s1 + s2 + '\n'

		print(ss1)

	def impresor_lista_seleccionada(self):
		'''Imprime la lista seleccionada'''

		if self.mostrar_lista == 's':
			if self.forma_traducir == '2':
				descripcion_listas = ['lista','idenficador','español','inglés']
				lista1 = self.lista[self.indice_identificador][3]
				lista2 = self.lista[self.indice_identificador][2]
			if self.forma_traducir == '1':
				descripcion_listas = ['lista','idenficador','inglés','español']
				lista1 = self.lista[self.indice_identificador][2]
				lista2 = self.lista[self.indice_identificador][3]

			print(f'---{self.indice_identificador+1}---')
			for y in range(len(self.lista[self.indice_identificador])-1):#sublistas
				if y == 2:
					a = len(descripcion_listas[2])
					for z in range(len(lista1)):#ver longitud mayor
						if len(lista1[z]) > a:
							a = len(lista1[z])

					b = descripcion_listas[y]+'>'
					print(f'-----<{b:-<{a+2}}<{descripcion_listas[y+1]}>')
				else:
					print(f'-----<{descripcion_listas[y]}>')
				for z in range(len(self.lista[self.indice_identificador][y])):#elementos de listas
					if y == 2:
						if z < 9:
							print(f'-{z+1}--. {lista1[z]:_<{a+3}}{lista2[z]}')
						else:
							print(f'-{z+1}-. {lista1[z]:_<{a+3}}{lista2[z]}')
					else:
						print(f'-{z+1}--. {self.lista[self.indice_identificador][y][z]}')
			input('Continuar [enter]: ')

class Calculos(Impresores):
	"""docstring for Calculos"""
	def __init__(self):
		super().__init__()
		self.limpia_del_constructor = True

	def constructor(self, lista_del_constructor,lista_de_repeticion_del_constructor,limpia_del_constructor):
		'''Los palabras de las listas se dan a traducir de forma_traducir aleatoria, sin repetir ninguna palabra, hasta que se haya completado la lista,
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

	def verificador_traductor(self, lista_de_repeticion_del_verificador_traductor):
		'''Se verifica la validez de la traduccíón según condiciones elegidas por el usuario'''

		if self.forma_traducir == '2':
			self.lista1 = self.lista[self.indice_identificador][3]
			self.lista2 = self.lista[self.indice_identificador][2]
		if self.forma_traducir == '1':
			self.lista1 = self.lista[self.indice_identificador][2]
			self.lista2 = self.lista[self.indice_identificador][3]

		self.indice_identificador, variable, lista_de_repeticion_del_constructor = constructor(lista1, lista_de_repeticion_del_verificador_traductor, limpia_ingresada_del_verificador_traductor)

		print(f'--{variable}---')

		insercion = input('Traducción: \n')
		insertado = insercion
		insercion = insercion.split(',')

		for i,x in enumerate(insercion):
			insercion[i] = insercion[i].strip(' ')

		traduccion_aux = lista2[self.indice_identificador].split(',')
		traduccion = 0

		for i,x in enumerate(traduccion_aux):
			traduccion_aux[i] = traduccion_aux[i].strip(' ')

		for x in traduccion_aux:
			for y in insercion:
				if x == y:
					traduccion = traduccion + 1;

		print(lista2[self.indice_identificador].strip(' '))

		if not traduccion_aux[-1].find(' - ') == -1:
			definiciones = len(traduccion_aux)-1
		else:
			definiciones = len(traduccion_aux)

		if verificar_elementos >= definiciones:
			numero_elementos_contar = definiciones
		else:
			numero_elementos_contar = verificar_elementos

		if traduccion >= numero_elementos_contar:
			print('BIEN')
			c1 = c1 + 1
		else:
			print('MAL')
			e1 = e1 + 1
	
	
if __name__ == '__main__':

	validacion_fin = ''
	while validacion_fin == '':
		imprimir = Impresores()
		imprimir.modificar_parametros()
		imprimir.impresor_total_listas()
		imprimir.impresor_total_identificadores()
		imprimir.seleccionador_opciones_listas()

		validacion = ''
		while validacion == '':

			#os.system('cls')
			imprimir.impresor_lista_seleccionada()#Se imprime la lista elegida
			#os.system('cls')
			'''c1, e1, c2, e2, lista_de_repeticion = verificador_traductor(lista[self.indice_identificador_identificador], verificar_elementos, forma_traducir, ingresar_mismo_elemento, lista_de_repeticion, c1, e1, c2, e2) #Se verifica lo ingresado

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
		if not ingresar_mismo_elemento == 'n':
			print('\ncorrectos/ETAPA 2')
			print(c2)
			print('incorrectos/ETAPA 2')
			print(e2)'''

		validacion_fin = input('\nContinuar [enter]/ Salir [Cualquier tecla]: ')

	input('FIN')