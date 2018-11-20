'''listas que usa practicador.py'''
def lista():
	lista = []

	lista.append([])
	lista[0].append(['verbos modales'])
	lista[0].append(['vm'])
	lista[0].append(['can','could','may','might','must','should','ought to'])
	lista[0].append(['puedo, -presente-'])
	lista[0][3].append('podría, pude, podía, pudiera, -condicional-pretérito-copretérito-pretérito(subjuntivo)')
	lista[0][3].append('podría, quizás, puede que')
	lista[0][3].append('podría, quizás, puede que')
	lista[0][3].append('debo, debo de')
	lista[0][3].append('debería, tendría que')
	lista[0][3].append('debería, tendría que')

	lista.append([])
	lista[1].append(['pronombres relativos'])
	lista[1].append(['pr'])
	lista[1].append(['who', 'that', 'which', 'whom', 'whose', 'what'])
	lista[1].append(['quien, quienes, que, - se usa sólo para personas'])
	lista[1][3].append('que, -se usa para cosas y personas')
	lista[1][3].append('que, el/la cual, los/las cuales, lo que, -se usa para cosas')
	lista[1][3].append('a quien, a quienes, al que')
	lista[1][3].append('cuyo/a, cuyos/as, de quien, de quienes')
	lista[1][3].append('lo que')

	lista.append([])
	lista[2].append(['cuantificadores incontables'])
	lista[2].append(['ci'])
	lista[2].append(['much','so much','too much','little','a little','less','the least','a large amount of','a great deal of'])
	lista[2].append(['mucho', 'tanto', 'demasiado', 'poco', 'algo de', 'menos, menor cantidad de', 'la menor cantidad', 'una gran cantidad de', 'mucho/a'])

	lista.append([])
	lista[3].append(['cuantificadores contables'])
	lista[3].append(['cc'])
	lista[3].append(['many', 'so many', 'too many', 'few', 'a few', 'fewer', 'the fewest', 'a large number of', 'a great many'])
	lista[3].append(['muchos', 'tantos', 'demasiados', 'pocos', 'algunos', 'menor número que', 'el menor numero de', 'un gran número de', 'muchisímos'])

	return list(lista)