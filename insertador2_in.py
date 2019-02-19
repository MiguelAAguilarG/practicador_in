'''Ayuda a hacer listas para aprenderlas cuando se hacen'''

lista = []
n = 0
exit = ''
while exit == '':

	print('Para salir ingrese un número cuando se pide un elemento')
	nombre = input('Ingrese nombre de la lista: ')
	identificador = input('Ingrese identificador de la lista: ')

	lista.append([])
	lista[n].append([nombre])
	lista[n].append([identificador])
	lista[n].append([])
	lista[n].append([])

	salir = 'n'
	uno = 1
	x = 1

	while uno != -1:
		uno = input(f'\nInglés.  Ingrese elemento {x}: ')
		dos = input(f'Español. Ingrese elemento {x}: ')

		try:
			int(uno)
			uno = -1
			int(dos)
			uno = -1
		except:
			lista[n][2].append(uno)
			lista[n][3].append(dos)

			x = x+1

	n = n+1

	exit = input('\nContinuar [enter]/ Salir [Cualquier tecla]: ')

for n in range(len(lista)):
	print(f'''
n = n+1
lista.append([])
lista[n].append({lista[n][0]})
lista[n].append({lista[n][1]})
lista[n].append({lista[n][2]})
lista[n].append({lista[n][3]})''')

input('FIN')