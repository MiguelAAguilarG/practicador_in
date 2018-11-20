import random
import os
import re

lista = []

lista.append([])
lista[0].append(['cuantificadores contables'])
lista[0].append(['cc'])
lista[0].append(['many,so many,too many,few,a few,fewer,the fewest,a large number of,a great many'])
lista[0].append(['muchos,tantos,demasiados,pocos,algunos,menor número que,el menor numero de,un gran número de,muchisímos'])

print(lista[0][2][0].split(','))
print(lista[0][3][0].split(','))
