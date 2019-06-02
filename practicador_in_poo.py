import random
import os
import lista

class Inicio():
	"""docstring for ClassName"""
	def __init__(self):
		self.lista = lista.lista() #Se carga la lista general, se usa en la función 'constructor'

		self.mostrar_lista = 's'
		self.verificar_elementos = 1
		self.forma_traducir = 3
		self.ingresar_mismo_elemento = 's'
		self.limite_inf_rango = 340
		self.limite_sup_rango = 365

	def modificar_parametros(self):
		os.system('cls')
		print('---Programa para practicar palabras en inglés---')
		print('Se mostrarán varias listas de palabras en inglés con tematicas diferentes para elegir\n')

		print(f'''***Parámetros por defecto***
-Mostar la lista seleccionada en cada palabra/frase a traducir: si[s]/ no[n]: {self.mostrar_lista}
--En palabras/frases con varias traducciones, para dar una respuesta por buena ¿cuántas traducciones tomar?: {self.verificar_elementos}
Traducir del:
ETAPA 1: inglés --> español <[1]>, español --> inglés <[2]>, salteado ([1],[2],[1],...,[2]) <[3]>: {self.forma_traducir}
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
			self.forma_traducir = int(input('ETAPA 1: inglés --> español <[1]>, español --> inglés <[2]>, salteado ([1],[2],[1],...,[2]) <[3]>: '))
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
			if self.forma_traducir == 1 or self.forma_traducir == 3:
				descripcion_listas = ['lista','idenficador','inglés','español']
				lista1 = self.lista[self.indice_identificador][2]
				lista2 = self.lista[self.indice_identificador][3]
			if self.forma_traducir == 2:
				descripcion_listas = ['lista','idenficador','español','inglés']
				lista1 = self.lista[self.indice_identificador][3]
				lista2 = self.lista[self.indice_identificador][2]

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

class Clase_Constructor():
	"""docstring for Calculos"""
	def __init__(self, lista, indice_identificador_constructor):
		self.limpia_del_constructor = True
		self.lista_del_constructor = lista[indice_identificador_constructor][2]
		self.numeros_buscar_lista = [x for x in range(len(self.lista_del_constructor))]

	def constructor(self):
		'''Los palabras de las listas se dan a traducir de forma_traducir aleatoria, sin repetir ninguna palabra, hasta que se haya completado la lista,
		cuentan las traducciones erroneas

		Esta función hace posible esto
		#Si 'limpia_del_constructor' es 'False' la lista elegida seguira mostrandose aleatoriamente, pero se repetiran las palabras de la lista sin que se alla mostrado la lista completa
		'''

		if len(self.numeros_buscar_lista) == 0:
			self.numeros_buscar_lista = [x for x in range(len(self.lista_del_constructor))]

		self.indice = random.choice(self.numeros_buscar_lista)

		if self.limpia_del_constructor == True:
			self.numeros_buscar_lista.remove(self.indice)

class Clase_Verificador():
	"""docstring for Calculos"""

	def __init__(self, lista, indice_identificador, forma_traducir, verificar_elementos):
		self.forma_traducir = forma_traducir
		self.verificar_elementos = verificar_elementos
		self.c1 = 0
		self.e1 = 0

		if self.forma_traducir == 1 or self.forma_traducir == 3:
			self.lista1 = lista[indice_identificador][2]
			self.lista2 = lista[indice_identificador][3]
		if self.forma_traducir == 2:
			self.lista1 = lista[indice_identificador][3]
			self.lista2 = lista[indice_identificador][2]

	def verificador_traductor(self, indice, segunda_impresion, insertado, correcto):
		#Se verifica la validez de la traduccíón según condiciones elegidas por el usuario
		self.indice = indice

		if segunda_impresion == False:
			print(f'--{self.lista1[self.indice]}---')

			insercion = input('Traducción: \n')
			self.insertado = insercion
		else:
			os.system('cls')
			print(insertado)
			print(self.lista1[self.indice])
			if correcto == True:
				print('BIEN')
			else:
				print('MAL')
			print('*****************')

			insercion = input('palabra/frase: \n')
			self.insertado = insercion

		insercion = insercion.split(',')

		for i,x in enumerate(insercion):
			insercion[i] = insercion[i].strip(' ')

		traduccion_aux = self.lista2[self.indice].split(',')
		traduccion = 0

		for i,x in enumerate(traduccion_aux):
			traduccion_aux[i] = traduccion_aux[i].strip(' ')

		for x in traduccion_aux:
			for y in insercion:
				if x == y:
					traduccion = traduccion + 1;

		print(self.lista2[self.indice].strip(' '))

		if not traduccion_aux[-1].find(' - ') == -1:
			definiciones = len(traduccion_aux)-1
		else:
			definiciones = len(traduccion_aux)

		if self.verificar_elementos >= definiciones:
			numero_elementos_contar = definiciones
		else:
			numero_elementos_contar = self.verificar_elementos

		if traduccion >= numero_elementos_contar:
			print('BIEN')
			self.correcto = True
			self.c1 = self.c1 + 1
		else:
			print('MAL')
			self.correcto = False
			self.e1 = self.e1 + 1
	
if __name__ == '__main__':

	validacion_fin = ''
	while validacion_fin == '':
		inicio = Impresores()
		inicio.modificar_parametros()
		os.system('cls')
		inicio.impresor_total_listas()
		inicio.impresor_total_identificadores()
		inicio.seleccionador_opciones_listas()
		lista_elementos = Clase_Constructor(inicio.lista, inicio.indice_identificador)
		a_verificar_etapa1 = Clase_Verificador(inicio.lista, inicio.indice_identificador, inicio.forma_traducir, inicio.verificar_elementos)
		forma_traducir = inicio.forma_traducir
		if inicio.ingresar_mismo_elemento == 's':
			if forma_traducir == 1 or forma_traducir == 3:
				aux = 2
			if forma_traducir == 2:
				aux = 1
			a_verificar_etapa2 = Clase_Verificador(inicio.lista, inicio.indice_identificador, aux, inicio.verificar_elementos)

		validacion = ''
		i = 1
		contador_forma3 = 1
		while validacion == '':

			os.system('cls')
			inicio.impresor_lista_seleccionada()#Se imprime la lista elegida
			os.system('cls')
			lista_elementos.constructor()
			indice = lista_elementos.indice

			if not contador_forma3%2 == 0:
				segunda_impresion = False
				a_verificar_etapa1.verificador_traductor(indice, segunda_impresion, None, None)

				if inicio.ingresar_mismo_elemento == 's':
					segunda_impresion = True
					a_verificar_etapa2.verificador_traductor(indice, segunda_impresion, a_verificar_etapa1.insertado, a_verificar_etapa1.correcto)
			else:
				segunda_impresion = False
				a_verificar_etapa2.verificador_traductor(indice, segunda_impresion, None, None)

				if inicio.ingresar_mismo_elemento == 's':
					segunda_impresion = True
					a_verificar_etapa1.verificador_traductor(indice, segunda_impresion, a_verificar_etapa2.insertado, a_verificar_etapa2.correcto)

			print(f'intentos: {i}')#Te muestra los intentos que llevas en la misma lista
			validacion = input('Continuar con la misma lista [enter]/ Seleccionar otra lista[Cualquier tecla]: ')

			os.system('cls')

			if forma_traducir == 3 and i%len(inicio.lista[inicio.indice_identificador][2]) == 0:
				contador_forma3 = contador_forma3 + 1

			i = i + 1

		print('intentos')
		print(i-1)
		print('\ncorrectos/ETAPA 1')
		print(a_verificar_etapa1.c1)
		print('incorrectos/ETAPA 1')
		print(a_verificar_etapa1.e1)
		if inicio.ingresar_mismo_elemento == 's':
			print('\ncorrectos/ETAPA 2')
			print(a_verificar_etapa2.c1)
			print('incorrectos/ETAPA 2')
			print(a_verificar_etapa2.e1)

		validacion_fin = input('\nContinuar [enter]/ Salir [Cualquier tecla]: ')

	input('FIN')