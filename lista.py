'''listas que usa practicador.py'''
def lista():
	lista = []
	n = 0
	lista.append([])
	lista[n].append(['verbos modales'])
	lista[n].append(['vmod'])
	lista[n].append(['can','could','may','might','must','should','ought to'])
	lista[n].append(['puedo, -presente-'])
	lista[n][3].append('podría, pude, podía, pudiera, -condicional-pretérito-copretérito-pretérito(subjuntivo)')
	lista[n][3].append('podría, quizás, puede que')
	lista[n][3].append('podría, quizás, puede que')
	lista[n][3].append('debo, debo de')
	lista[n][3].append('debería, tendría que')
	lista[n][3].append('debería, tendría que')

	n = n+1
	lista.append([])
	lista[n].append(['pronombres relativos'])
	lista[n].append(['prel'])
	lista[n].append(['who', 'that', 'which', 'whom', 'whose', 'what'])
	lista[n].append(['quien, quienes, que, - se usa sólo para personas'])
	lista[n][3].append('que, -se usa para cosas y personas')
	lista[n][3].append('que, el/la cual, los/las cuales, lo que, -se usa para cosas')
	lista[n][3].append('a quien, a quienes, al que')
	lista[n][3].append('cuyo/a, cuyos/as, de quien, de quienes')
	lista[n][3].append('lo que')

	n = n+1
	lista.append([])
	lista[n].append(['cuantificadores incontables'])
	lista[n].append(['cinc'])
	lista[n].append(['much','so much','too much','little','a little','less','the least','a large amount of','a great deal of'])
	lista[n].append(['mucho', 'tanto', 'demasiado', 'poco', 'algo de', 'menos, menor cantidad de', 'la menor cantidad', 'una gran cantidad de', 'mucho/a'])

	n = n+1
	lista.append([])
	lista[n].append(['cuantificadores contables'])
	lista[n].append(['ccon'])
	lista[n].append(['many', 'so many', 'too many', 'few', 'a few', 'fewer', 'the fewest', 'a large number of', 'a great many'])
	lista[n].append(['muchos', 'tantos', 'demasiados', 'pocos', 'algunos', 'menor número que', 'el menor número de', 'un gran número de', 'muchisímos'])

	n = n+1
	lista.append([])
	lista[n].append(['pronombres indefinidos'])
	lista[n].append(['pind'])
	lista[n].append(['everyone', 'everybody', 'no one', 'nobody', 'someone', 'somebody', 'anyone, -al preguntar-', 'anybody, -al preguntar-', 'anyone, -al afirmar', 'anybody, -al afirmar',
	'anyone, -al negar', 'anybody, -al negar', 'everything', 'nothing', 'something', 'anything, -al preguntar-', 'anything, -al afirmar-', 'anything, -al negar-'])
	lista[n].append(['todos/as, todo el mundo','todos/as, todo el mundo','nadie','nadie','alguien','alguien','alguien, -al preguntar-',
	'alguien, -al preguntar-','cualquiera, -al afirmar','cualquiera, -al afirmar','nadie, -al negar','nadie, -al negar','todo','nada',
	'algo','algo, -al preguntar-','cualquier cosa, -al afirmar-','nada, -al negar-'])

	n = n+1
	lista.append([])
	lista[n].append(['pronombres recíprocos'])
	lista[n].append(['prec'])
	lista[n].append(['each other', 'one another'])
	lista[n].append(['se, nos, uno al otro, mutuamente, unos a otros','se, nos, uno al otro, mutuamente, unos a otros'])

	n = n+1
	lista.append([])
	lista[n].append(['conectores copulativos'])
	lista[n].append(['ccop'])
	lista[n].append(['and', 'not only...but also...', 'not only...but...as well', 'both...and...', 'no sooner...than...'])
	lista[n].append(['y', 'no solo...sino también...', 'no solo...sino...también','tanto...como..., ambas cosas','apenas...cuando...'])

	n = n+1
	lista.append([])
	lista[n].append(['conectores disyuntivos'])
	lista[n].append(['cdis'])
	lista[n].append(['or', 'either...or...', 'neither...or...', 'whether...or...', 'or else...', 'otherwise'])
	lista[n].append(['o', 'o...o...', 'no...ni...', 'si...o...', 'o sino...', 'de otro modo'])
	
	n = n+1
	lista.append([])
	lista[n].append(['conectores condicionales'])
	lista[n].append(['ccond'])
	lista[n].append(['if', 'whether', 'unless', 'provided, providing', 'as long as', 'in case'])
	lista[n].append(['si', 'si', 'a menos que', 'siempre que, mientras', 'siempre que, mientras', 'en caso de que'])

	n = n+1
	lista.append([])
	lista[n].append(['conectores concesivos'])
	lista[n].append(['ccons'])
	lista[n].append(['although, though, even though', 'even if', 'not even if', 'despite, in spite of', 'regardless of'])
	lista[n].append(['aunque', 'incluso si', 'ni siquiera si', 'a pesar de', 'sin importar, sin que importe'])

	n = n+1
	lista.append([])
	lista[n].append(['conectores conclusivos'])
	lista[n].append(['cconc'])
	lista[n].append(['therefore', 'hence', 'thus', 'so', 'consequently'])
	lista[n].append(['por lo tanto', 'de ahí', 'por lo tanto', 'entonces', 'por lo tanto, en consecuencia'])

	n = n+1
	lista.append([])
	lista[n].append(['conectores continuativos'])
	lista[n].append(['ccont'])
	lista[n].append(['then', 'moreover', 'furthermore', 'besides', 'in addition to'])
	lista[n].append(['entonces', 'además', 'además', 'además', 'además de'])

	n = n+1
	lista.append([])
	lista[n].append(['conectores adversativos'])
	lista[n].append(['cadv'])
	lista[n].append(['but', 'however', 'nonetheless, nevertheless', 'yet, even so', 'still', 'instead', 'on the contrary'])
	lista[n].append(['pero', 'sin embargo', 'sin embargo', 'sin embargo, aun así', 'sin embargo', 'en su lugar, en lugar de ello', 'por el contrario'])

	n = n+1
	lista.append([])
	lista[n].append(['conectores causales'])
	lista[n].append(['ccau'])
	lista[n].append(['because', 'for', 'because of', 'since', 'as', 'due to, owing to'])
	lista[n].append(['porque, asi que', 'para, porque', 'debido a, porque', 'puesto que, ya que', 'puesto que, como', 'debido a'])

	n = n+1
	lista.append([])
	lista[n].append(['conectores comparativos'])
	lista[n].append(['ccom'])
	lista[n].append(['as', 'as...as', 'not as...as', 'not so...as', 'as if, as though', 'than'])
	lista[n].append(['como','tan...como','no tan...como','no tan...como','como si','que'])

	n = n+1
	lista.append([])
	lista[n].append(['conectores funcionales'])
	lista[n].append(['cfun'])
	lista[n].append(['so', 'so that', 'so as to', 'so as not to', 'in order to'])
	lista[n].append(['entonces', 'para que', 'para que, de manera que', 'para no', 'para'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de modo 1'])
	lista[n].append(['amod1'])
	lista[n].append(['slowly', 'easily', 'carefully', 'simply', 'happily', 'naturally'])
	lista[n].append(['lentamente', 'fácilmente', 'cuidadosamente', 'simplemente', 'felizmente', 'naturalmente'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de modo 2'])
	lista[n].append(['amod1'])
	lista[n].append(['well', 'fast', 'hard'])
	lista[n].append(['bien', 'rápidamente', 'duramente'])

	'''n = n+1
	lista.append([])
	lista[n].append(['adverbios de modo 3'])
	lista[n].append(['amod1'])
	lista[n].append(['better', 'together', 'right', 'badly', 'worse', 'separately', 'carelessly', 'wrong'])
	lista[n].append(['mejor', 'juntos', 'correctamente'])'''

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de lugar 1'])
	lista[n].append(['alug1'])
	lista[n].append(['here', 'there', 'near', 'nearby', 'far', 'away'])
	lista[n].append(['aquí', 'allá', 'cerca', 'cerca', 'lejos', 'lejos'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de lugar 2'])
	lista[n].append(['alug2'])
	lista[n].append(['home', 'abroad', 'overseas', 'in', 'out', 'insider', 'outside'])
	lista[n].append(['a/en casa', 'al/en el extranjero', 'al/en el extranjero', 'adentro', 'afuera', 'adentro', 'afuera'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de lugar 3'])
	lista[n].append(['alug3'])
	lista[n].append(['indoors', 'outdoors', 'above', 'below', 'underneath', 'beneath'])
	lista[n].append(['adentro, bajo techo', 'al aire libre', 'arriba, encima', 'abajo, debajo', 'debajo, abajo, por debajo', 'debajo, abajo, por debajo'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de lugar 4'])
	lista[n].append(['alug4'])
	lista[n].append(['ahead', 'behind', 'in front', 'opposite', 'around', 'beyond'])
	lista[n].append(['adelante', 'atrás, detrás', 'en frente', 'en frente', 'alrededor, por aquí', 'más allá'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de lugar 5'])
	lista[n].append(['alug5'])
	lista[n].append(['aside', 'sideways', 'back', 'over', 'all over', 'over here', 'over there', 'right here', 'right there', 'up here', 'down there', 'up', 'down'])
	lista[n].append(['a un lado, aparte', 'hacia un lado, de lado', 'detrás, en la parte trasera, hacia atrás', 'encima', 'por todas partes', 'por aquí', 'por allí', 'justo aquí', 'justo allí', 'aquí arriba', 'allí abajo', 'arriba, encima, en lo alto', 'abajo, hacia abajo'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de lugar 6'])
	lista[n].append(['alug6'])
	lista[n].append(['uptown', 'downtown', 'upstairs', 'downstairs', 'uphill', 'downhill'])
	lista[n].append(['en la zona residencial', 'en el centro de la ciudad', 'en el piso de arriba', 'en el piso de abajo', 'cuesta arriba', 'cuesta abajo'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de lugar 7'])
	lista[n].append(['alug7'])
	lista[n].append(['upwards', 'downwards', 'inwards', 'outwards', 'forward', 'backwards', 'onwards', 'homeward'])
	lista[n].append(['hacia arriba', 'hacia abajo', 'hacia adentro', 'hacia afuera', 'hacia adelante', 'hacia atrás', 'hacia adelante', 'hacia casa'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de lugar 8'])
	lista[n].append(['alug8'])
	lista[n].append(['everywhere', 'nowhere', 'somewhere', 'anywhere', 'elsewhere'])
	lista[n].append(['en/a todas partes', 'en/a ninguna parte', 'en algún lugar', 'en cualquier/ningún lugar', 'en otra parte'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de lugar 9'])
	lista[n].append(['alug9'])
	lista[n].append(['south', 'north', 'west', 'east'])
	lista[n].append(['al sur', 'al norte', 'al oeste', 'al este'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de lugar 10'])
	lista[n].append(['alug10'])
	lista[n].append(['southwards', 'northwards', 'westwards', 'eastwards'])
	lista[n].append(['hacia el sur', 'hacia el norte', 'hacia el oeste', 'hacia el este'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de lugar 11'])
	lista[n].append(['alug11'])
	lista[n].append(['southbound', 'northbound', 'westbound', 'eastbound'])
	lista[n].append(['rumbo al sur', 'rumbo al norte', 'rumbo al oeste', 'rumbo al este'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de tiempo 1'])
	lista[n].append(['atie1'])
	lista[n].append(['early', 'late', 'earlier', 'later', 'then', 'before', 'after', 'afterwards'])
	lista[n].append(['temprano', 'tarde', 'antes, más temprano', 'luego, más tarde', 'luego, entonces', 'antes', 'después', 'luego'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de tiempo 2'])
	lista[n].append(['atie2'])
	lista[n].append(['now', 'nowadays', 'these days', 'currently', 'at present', 'today', 'tomorrow', 'yesterday'])
	lista[n].append(['ahora', 'hoy en día', 'en estos días', 'actualmente', 'en el presente', 'hoy', 'mañana', 'ayer'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de tiempo 3'])
	lista[n].append(['atie3'])
	lista[n].append(['still', 'already', 'yet', 'not yet', 'no longer', 'not anymore', 'just'])
	lista[n].append(['todavía/aún, -positivas-', 'ya', 'ya, todavía/aún, -negativas/preguntas-', 'aún no', 'ya no', 'ya no', 'justo, recién, acabo de'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de tiempo 4'])
	lista[n].append(['atie4'])
	lista[n].append(['ever', 'soon', 'again', 'thereafter', 'lately', 'recently', 'formerly', 'latterly'])
	lista[n].append(['alguna vez', 'pronto', 'de nuevo, otra vez', 'después de eso', 'últimamente', 'recientemente', 'anteriormente', 'últimamente'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de tiempo 5'])
	lista[n].append(['atie5'])
	lista[n].append(['in the past', 'in the future', 'this week', 'next week', 'last week', 'this year', 'next year', 'last year', 'meanwhile', 'someday', 'shortly'])
	lista[n].append(['en el pasado', 'en el futuro', 'esta semana', 'la semana próxima', 'la semana pasada', 'este año', 'el año que viene', 'el año pasado', 'entretanto', 'algún día', 'en poco tiempo'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de tiempo 6'])
	lista[n].append(['atie6'])
	lista[n].append(['five minutes ago', 'two weeks ago', 'four days ago', 'long ago'])
	lista[n].append(['hace cinco minutos', 'hace dos semanas', 'hace cuatro días', 'hace mucho tiempo'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de duración 1'])
	lista[n].append(['adur1'])
	lista[n].append(['all day', 'all week', 'the whole morning', 'for a while', 'for five minutes', 'for two years'])
	lista[n].append(['todo el día', 'toda la semana', 'la mañana entera', 'por un rato/tiempo', 'por cinco minutos', 'por dos años'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de duración 2'])
	lista[n].append(['adur2'])
	lista[n].append(['for several days', 'for three centuries', 'since', 'since then', 'ever since', 'since Monday'])
	lista[n].append(['por varios días', 'por tres siglos', 'desde', 'desde entonces', 'desde entonces', 'desde el lunes'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de duración 3'])
	lista[n].append(['adur3'])
	lista[n].append(['from the beginning', 'since 1985', 'until now', 'till now', 'up to now', 'until Sunday', 'so far', 'as yet'])
	lista[n].append(['desde el comienzo', 'desde 1985', 'hasta ahora', 'hasta ahora', 'hasta ahora', 'hasta el domingo', 'hasta ahora', 'hasta ahora'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de duración 4'])
	lista[n].append(['adur4'])
	lista[n].append(['from now on', 'hereafter', 'forever', 'eternally', 'temporarily', 'permanently'])
	lista[n].append(['desde ahora en adelante', 'desde ahora en adelante', 'por siempre', 'eternamente', 'temporalmente', 'permanentemente'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de frecuencia 1'])
	lista[n].append(['afre1'])
	lista[n].append(['always', 'usually', 'frequently', 'often', 'sometimes', 'occasionally', 'rarely', 'seldom', 'hardly ever'])
	lista[n].append(['siempre', 'generalmente', 'frecuentemente', 'a menudo', 'algunas veces', 'ocasionalmente, de vez en cuando', 
	'raramente, casi nunca', 'raramente, casi nunca', 'casi nunca', 'nunca'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de frecuencia 2'])
	lista[n].append(['afre2'])
	lista[n].append(['annually', 'yearly', 'monthly', 'weekly', 'daily', 'hourly'])
	lista[n].append(['anualmente', 'anualmente, anual', 'mensualmente, mensual', 'semanalmente, semanal', 'diaramente, diario', 
	'cada hora'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de frecuencia 3'])
	lista[n].append(['afre3'])
	lista[n].append(['every day', 'ever', 'yearly', 'every month', 'every year', 'normally', 'regularly'])
	lista[n].append(['todos los días', 'alguna vez, siempre, -preguntas/positivas-', 'anualmente', 'todos los meses', 'todos los años', 'normalmente', 'regularmente'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de frecuencia 4'])
	lista[n].append(['afre4'])
	lista[n].append(['once', 'twice', 'three times', 'once a day', 'twice a month', 'every other day', 'every day', 'from time to time', 'once in a while', 'every now and then'])
	lista[n].append(['una vez', 'dos veces', 'tres veces', 'una vez al día', 'dos veces al mes', 'cualquier otro día', 'todos los días', 'de vez en cuando', 'de vez en cuando', 'de vez en cuando'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de orden 1'])
	lista[n].append(['aord1'])
	lista[n].append(['first', 'at first', 'initially', 'first of all', 'in the first place', 'secondly', 'thirdly', 'fourthly'])
	lista[n].append(['primero', 'al principio', 'inicialmente', 'antes que nada', 'en primer lugar, primero que todo', 'en segundo lugar', 'en tercer lugar', 'en cuarto lugar'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de orden 2'])
	lista[n].append(['aord2'])
	lista[n].append(['lastly', 'at last', 'finally', 'eventually', 'in the end'])
	lista[n].append(['por último, finalmente', 'por fin, finalmente', 'finalmente', 'finalmente', 'al final'])


	return lista

'''def seleccionador_grupo(lista):
	grupos_set = set()

	for x in lista:
		for y in x[4]:
			grupos_set.add(y)
			
	grupos_num_dict = zip(grupos_set,[x for x in range(len(grupos_set))])
	grupos_num_dict = dict(grupos_num_dict)

	print('-grupos de la lista-')
	for x,y in grupos_num_dict.items():
		if y < 9:
			print(f'-{y+1}--. {x}')
		else:
			print(f'-{y+1}-. {x}')

	while True:
		grupo = input('Ingrese un grupo de la lista [nombre o número]: ').lower()

		try:
			grupo = int(grupo)-1
			print(grupo)
			if grupo in grupos_num_dict.values():
				return grupo
			else:
				print('ERROR. No es un número de lista valido')
		except:
			if grupo in grupos_num_dict.keys():
				return grupo
			else:
				print('ERROR. No es un nombre de grupo')

seleccionador_grupo(lista())'''