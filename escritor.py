import os
import sys
import time
import threading

def contar_tiempo():
	global intentos
	global tiempo_final
	global tiempo_inicial

	while intentos < limite_intentos_generales:

		tiempo_final = time.perf_counter()
		contador = 0
		while tiempo >= tiempo_final-tiempo_inicial:
			longitud_2 = len(texto)
			tiempo_final = time.perf_counter()
			if longitud_1 <= longitud_2 and tiempo <= tiempo_final-tiempo_inicial:
				print('SALTO')
				intentos = intentos + 1
				tiempo_inicial = time.perf_counter()
				if intentos >= 3:
					break
	if intentos >= limite_intentos_generales:
		print('Se acabo.\nSalir [cualquier tecla]:')

print('Haga un escrito')
print('Cada tantos segundos se pasara a otro renglón')
print('El programa te sacará al tercer renglón que te hayas pasado')
tiempo = 3

input('Comenzar [enter]: ')

texto = []
longitud_1 = len(texto)
limite_intentos_generales = 3
intentos = 0

os.system('cls')
hilo = threading.Thread(target = contar_tiempo)
tiempo_inicial = time.perf_counter()
hilo.start()
while intentos < limite_intentos_generales:
	tiempo_inicial = time.perf_counter()
	entrada = input()

	texto.append(entrada)
	longitud_1 = len(texto)

for renglon in texto:
	if 'SALTO' in renglon:
		texto.remove(renglon)

for renglon in texto:
	print(renglon)

input('FIN')