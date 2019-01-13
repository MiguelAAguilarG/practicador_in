'''Ayuda a hacer listas para aprenderlas cuando se hacen'''

lista = []
n = 0
exit = ''
while exit == '':

	nombre = input('Ingrese nombre de la lista: ')
	identificador = input('Ingrese identificador de la lista: ')
	num = int(input('Ingrese número de elementos de la lista: '))

	lista.append([])
	lista[n].append([nombre])
	lista[n].append([identificador])
	lista[n].append([])
	lista[n].append([])

	salir = 'n'
	for x in range(num):
		uno = input(f'\nInglés.  Ingrese elemento {x+1}: ')
		dos = input(f'Español. Ingrese elemento {x+1}: ')

		lista[n][2].append(uno)
		lista[n][3].append(dos)

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