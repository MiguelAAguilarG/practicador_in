'''Ayuda a dar formato más rápido a las palabras para lista.py

lista = 'first,at first,initially,first of all,in the first place,secondly,thirdly,fourthly' #Palabras a traducir en una string, separadas por una coma, sin espacios entre cada palabra o frase
print(lista.split(',')) #Se hace una lista con la string en el formato adecuado
#Ahora se puede pasar la lista impresa a lista.py
'''

lista = 'first,at first,initially,first of all,in the first place,secondly,thirdly,fourthly' 
print(lista.split(','))
lista = 'primero,al principio,inicialmente,antes que nada,en primer lugar,en segundo lugar,en tecer lugar,en cuarto lugar'
print(lista.split(','))

lista = 'lastly,at last,finally,eventually,in the end'
print(lista.split(','))
lista = 'por último, finalmente,por fin, finalmente,finalmente,finalmente,al final'
print(lista.split(','))

'''
lista = []
lista.append([])
lista[0].append(['cuantificadores contables'])
lista[0].append(['cc'])
lista[0].append(['annually,yearly,monthly,weekly,daily,hourly'])
lista[0].append(['anualmente,anualmente,mensualmente,semanalmente,diaramente,a cada hora'])

print(lista[0][2][0].split(','))
print(lista[0][3][0].split(','))'''
