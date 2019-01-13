'''listas que usa practicador.py'''

def lista():
	lista = [] #Lista general
	n = 0 #Número para las listas en lista general
	lista.append([])
	lista[n].append(['verbos modales']) #Nombre de la lista
	lista[n].append(['vmod']) #Identificador alfanúmerico
	lista[n].append(['can','could','may','might','must','should','ought to']) #Palabras en inglés
	lista[n].append(['puedo, -presente-']) #Traducción o traducciones de palabras en inglés, las traducciones se separán por una coma
	lista[n][3].append('podría, pude, podía, pudiera, -condicional-pretérito-copretérito-pretérito(subjuntivo)') 
	lista[n][3].append('podría, quizás, puede que')#Las ayudas para la traducción se ponen al final de todas las traducciones, se separan con una coma como las traducciones, se idetifican con un guión en cualquier lugar de la ayuda
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

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de grado 1'])
	lista[n].append(['agra1'])
	lista[n].append(['much', 'so much', 'too much', 'very little', 'so little', 'too little'])
	lista[n].append(['mucho', 'tanto', 'demasiado', 'muy poco', 'tan poco', 'demasiado poco'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de grado 2'])
	lista[n].append(['agra2'])
	lista[n].append(['more', 'much more', 'far more', 'less', 'much less', 'far less'])
	lista[n].append(['más', 'mucho más', 'mucho más', 'menos', 'mucho menos', 'mucho menos'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de grado 3'])
	lista[n].append(['agra3'])
	lista[n].append(['almost', 'nearly', 'barely', 'scarcely', 'hardly', 'not at all', 'even', 'even more', 'even less', 'not even'])
	lista[n].append(['casi', 'casi', 'apenas', 'apenas', 'apenas, casi no', 'para nada, en absoluto', 'incluso, aún', 'aún más', 'aún menos', 'ni siquiera'])
	
	n = n+1
	lista.append([])
	lista[n].append(['adverbios de grado 4'])
	lista[n].append(['agra4'])
	lista[n].append(['partially', 'partly', 'entirely', 'completely', 'absolutely', 'relatively', 'at least', 'at most'])
	lista[n].append(['parcialmente, a medias', 'en parte', 'enteramente', 'completamente', 'absolutamente', 'relativamente', 'al menos', 'como máximo'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de grado 5'])
	lista[n].append(['agra5'])
	lista[n].append(['largely', 'mostly', 'mainly', 'totally', 'extremely', 'altogether'])
	lista[n].append(['en gran parte', 'en su mayor parte', 'principalmente', 'totalmente', 'sumamente', 'en total'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de grado 6'])
	lista[n].append(['agra6'])
	lista[n].append(['so', 'very', 'too', 'enough', 'just', 'only'])
	lista[n].append(['tan', 'muy', 'demasiado', 'suficiente', 'justo, apenas, sólo', 'sólo, solamente'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de grado 7'])
	lista[n].append(['agra7'])
	lista[n].append(['pretty', 'quite', 'fairly', 'rather'])
	lista[n].append(['bastante', 'bastante, completamente', 'bastante', 'más bien'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de certeza 1'])
	lista[n].append(['acer1'])
	lista[n].append(['certainly', 'of course', 'definitely', 'indeed', 'obviously', 'really'])
	lista[n].append(['ciertamente, desde luego', 'por supuesto', 'sin duda', 'efectivamente, de veras', 'evidentemente', 'realmente'])

	n = n+1
	lista.append([])
	lista[n].append(['adverbios de certeza 2'])
	lista[n].append(['acer2'])
	lista[n].append(['surely', 'truly', 'undoubtedly', 'likely', 'perhaps', 'maybe', 'possibly', 'probably'])
	lista[n].append(['ciertamente, sin duda', 'realmente', 'indudablemente', 'probablemente', 'quizás, tal vez', 'quizás', 'posiblemente, tal vez', 'probablemente'])

	n = n+1
	lista.append([])
	lista[n].append(['preposiciones de lugar 1'])
	lista[n].append(['plug1'])
	lista[n].append(['on', 'upon', 'in', 'at', 'inside', 'outside', 'above', 'below'])
	lista[n].append(['sobre, en, encima de', 'sobre, en , encima de, -formal-', 'en, adentro de', 'en', 'dentro de, en', 'afuera, fuera, fuera de', 'encima de, sobre, arriba', 'debajo de'])

	n = n+1
	lista.append([])
	lista[n].append(['preposiciones de lugar 2'])
	lista[n].append(['plug2'])
	lista[n].append(['over', 'under', 'beneath', 'underneath', 'by', 'near', 'close to', 'across'])
	lista[n].append(['encima de, sobre', 'debajo de, bajo', 'bajo, debajo de', 'bajo, debajo de', 'al lado de, junto a', 'cerca de', 'cerca de', 'a lo ancho de, a través de, al otro lado de'])

	n = n+1
	lista.append([])
	lista[n].append(['preposiciones de lugar 3'])
	lista[n].append(['plug3'])
	lista[n].append(['along', 'around', 'round', 'against', 'on top of', 'at the bottom of', 'in front of', 'opposite', 'behind'])
	lista[n].append(['a lo largo de', 'alrededor de, cerca de, por', 'alrededor de, en torno a, por', 'contra, en contra de', 'encima de, sobre, arriba de', 'en la base de, debajo de, en el fondo de', 'enfrente de', 'enfrente de, frente a', 'detrás, detrás de'])

	n = n+1
	lista.append([])
	lista[n].append(['preposiciones de lugar 4'])
	lista[n].append(['plug4'])
	lista[n].append(['beside', 'next to', 'within', 'beyond', 'between', 'among', 'amid', 'before', 'after', 'throughout'])
	lista[n].append(['al lado de, junto a', 'al lado de, junto a', 'dentro de, a menos de', 'más allá de', 'entre', 'entre, en medio de', 'entre, en medio de', 'delante de, ante', 'después de, tras', 'por todo, a través de todo'])

	n = n+1
	lista.append([])
	lista[n].append(['preposiciones de dirección 1'])
	lista[n].append(['pdir1'])
	lista[n].append(['up', 'down', 'into', 'out of', 'on', 'onto', 'off', 'over', 'under', 'to', 'from'])
	lista[n].append(['por, hacia arriba', 'por, hacia abajo', 'dentro de, al, hacia adentro', 'de, afuera de, fuera de', 'sobre, al', 'sobre, al', 'de, fuera de', 'sobre, por encima de', 'debajo de, bajo', 'a, hacia', 'de, desde'])

	n = n+1
	lista.append([])
	lista[n].append(['preposiciones de dirección 2'])
	lista[n].append(['pdir2'])
	lista[n].append(['toward', 'towards', 'away from', 'along', 'across', 'through', 'around', 'by', 'past', 'after'])
	lista[n].append(['hacia', 'hacia', 'fuera de, alejándose de', 'a lo largo de, por', 'a través de, cruzando', 'a través de', 'alrededor de, por', 'por, cerca de, junto a', 'más allá de, por delante de', 'después de, detrás de, tras'])
	
	n = n+1
	lista.append([])
	lista[n].append(['preposiciones de tiempo 1'])
	lista[n].append(['ptie1'])
	lista[n].append(['about', 'around', 'before', 'after', 'during', 'over', 'for', 'throughout'])
	lista[n].append(['aproximadamente, alrededor de', 'aproximadamente, alrededor de', 'antes de', 'después de', 'durante', 'durante', 'durante, por', 'durante todo'])
	
	n = n+1
	lista.append([])
	lista[n].append(['preposiciones de tiempo 2'])
	lista[n].append(['ptie2'])
	lista[n].append(['since', 'until', 'to', 'past', 'between...and...', 'within', 'from...to/till/until...', 'as from', 'as of'])
	lista[n].append(['desde', 'hasta', 'para, hacia', 'pasado', 'entre...y...', 'entre, en no más de', 'desde...hasta...', 'a partir de', 'a partir de'])

	n = n+1
	lista.append([])
	lista[n].append(['preposiciones de tiempo 3'])
	lista[n].append(['ptie3'])
	lista[n].append(['by', 'beyond', 'on', 'at', 'in'])
	lista[n].append(['para, antes de', 'más allá de', 'en, -para los días-', 'a, -para las horas-', 'en, -para meses/estaciones/años/partes del día-'])
	
	n = n+1
	lista.append([])
	lista[n].append(['at tiempo'])
	lista[n].append(['att'])
	lista[n].append(['at'])
	lista[n].append(['+ hora, + días festivo, + ciertas expresiones'])

	n = n+1
	lista.append([])
	lista[n].append(['on tiempo'])
	lista[n].append(['ont'])
	lista[n].append(['on'])
	lista[n].append(['+ días, + días + partes del día, + fechas'])

	n = n+1
	lista.append([])
	lista[n].append(['in tiempo'])
	lista[n].append(['int'])
	lista[n].append(['in'])
	lista[n].append(['+ partes del día, + meses, + años, + estaciones del año, + largos períodos, + referencias al futuro'])

	n = n+1
	lista.append([])
	lista[n].append(['at lugar'])
	lista[n].append(['atl'])
	lista[n].append(['at'])
	lista[n].append(['+ lugares comunes, + lugares específicos, + domicilios, + ciertas cosas, + posiciones'])

	n = n+1
	lista.append([])
	lista[n].append(['on lugar'])
	lista[n].append(['onl'])
	lista[n].append(['on'])
	lista[n].append(['+ superficies, + medios de transporte, + partes del cuerpo, + direcciones'])

	n = n+1
	lista.append([])
	lista[n].append(['in lugar'])
	lista[n].append(['inl'])
	lista[n].append(['in'])
	lista[n].append(['+ países, + ciudades, + habitaciones, + cuerpos de agua, + clima, + ciertos lugares'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos determinatvos 1'])
	lista[n].append(['adet1'])
	lista[n].append(['this', 'that', 'these', 'those'])
	lista[n].append(['este, esta, esto', 'ese, esa, eso, aquel, aquello/a', 'estos, estas', 'esos, esas, aquellos/as'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos determinatvos 2'])
	lista[n].append(['adet2'])
	lista[n].append(['all', 'every', 'each', 'both', 'either', 'neither'])
	lista[n].append(['todo/a, todos/as', 'cada, -todos-', 'cada, -particular-', 'ambos, los dos', 'cualquiera, ambos, ninguno, -de dos- -al negar-', 'ninguno de los dos, ni el uno ni el otro'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos determinatvos 3'])
	lista[n].append(['adet3'])
	lista[n].append(['another', 'other', 'the other'])
	lista[n].append(['otro/a', 'otro/a, otros/as', 'el otro, la otra, los otros, las otras'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos color 1'])
	lista[n].append(['acol1'])
	lista[n].append(['black', 'gray', 'violet', 'white', 'green', 'orange', 'red', 'brown'])
	lista[n].append(['negro', 'gris', 'violeta', 'blanco', 'verde', 'naranja', 'rojo', 'café'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos color 2'])
	lista[n].append(['acol2'])
	lista[n].append(['sky blue', 'blue', 'yellow', 'pink', 'purple', 'beige', 'turquoise'])
	lista[n].append(['celeste', 'azul', 'amarillo', 'rosa', 'morado', 'beige', 'turquesa'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos tamaño 1'])
	lista[n].append(['atam1'])
	lista[n].append(['big', 'large', 'huge', 'small', 'tiny', 'heavy', 'light', 'thick', 'thin', 'wide'])
	lista[n].append(['grande', 'grande', 'enorme', 'pequeño', 'diminuto', 'pesado', 'liviano', 'grueso', 'delgado', 'ancho'])	

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos tamaño 2'])
	lista[n].append(['atam2'])
	lista[n].append(['high', 'low', 'tall', 'short', 'long', 'medium', 'narrow', 'deep', 'shallow', 'broad'])
	lista[n].append(['elevado', 'bajo', 'alto', 'corto, bajo', 'largo', 'medio', 'angosto', 'profundo', 'plano', 'ancho'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos forma 1'])
	lista[n].append(['afor1'])
	lista[n].append(['square', 'round', 'rectangular', 'triangular', 'oval', 'conical', 'spherical', 'cubical'])
	lista[n].append(['cuadrado', 'redondo', 'rectangular', 'triangular', 'oval', 'cónico', 'esférico', 'cúbico'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos forma 2'])
	lista[n].append(['afor2'])
	lista[n].append(['cylindrical', 'straight', 'curved', 'crooked', 'broad', 'narrow', 'flat', 'steep', 'hollow', 'solid'])
	lista[n].append(['cilíndrico', 'recto', 'curvo', 'torcido', 'ancho', 'angosto', 'plano', 'empinado', 'hueco', 'sólido'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos color 2'])
	lista[n].append(['acol2'])
	lista[n].append(['sky blue', 'blue', 'yellow', 'pink', 'purple', 'beige', 'turquoise'])
	lista[n].append(['celeste', 'azul', 'amarillo', 'rosa', 'morado', 'beige', 'turquesa'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos edad/tiempo 1'])
	lista[n].append(['ae/t1'])
	lista[n].append(['old', 'young', 'new', 'modern', 'ancient', 'old fashioned', 'updated', 'outdated'])
	lista[n].append(['viejo', 'joven', 'nuevo', 'moderno', 'antiguo', 'anticuado', 'actualizado', 'desactualizado'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos edad/tiempo 2'])
	lista[n].append(['ae/t2'])
	lista[n].append(['fast', 'quick', 'slow', 'senior', 'junior', 'current', 'past', 'future'])
	lista[n].append(['rápido', 'rápido', 'lento', 'mayor', 'más joven', 'actual', 'pasado', 'futuro'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos clima 1'])
	lista[n].append(['acli1'])
	lista[n].append(['rainy', 'stormy', 'sunny', 'windy', 'snowy', 'damp', 'dry', 'icy'])
	lista[n].append(['lluvioso', 'tormentoso', 'soleado', 'ventoso', 'con nieve', 'húmedo', 'seco', 'con hielo'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos clima 2'])
	lista[n].append(['acli2'])
	lista[n].append(['foggy', 'overcast', 'cloudy', 'clear', 'mild', 'chilly'])
	lista[n].append(['con niebla', 'nublado', 'nuboso', 'despejado', 'templado', 'frío'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos temperatura 1'])
	lista[n].append(['atem1'])
	lista[n].append(['freezing', 'chilly', 'cold', 'cool'])
	lista[n].append(['helado', 'frío', 'frío', 'fresco'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos temperatura 2'])
	lista[n].append(['atem2'])
	lista[n].append(['lukewarm', 'boiling', 'muggy', 'hot', 'warm', 'pleasant'])
	lista[n].append(['tibio', 'hirviendo', 'caluroso', 'caluroso', 'cálido', 'agradable'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos textura/tacto 1'])
	lista[n].append(['at/t1'])
	lista[n].append(['hard', 'soft', 'rough', 'smooth', 'solid', 'liquid', 'wet', 'dry'])
	lista[n].append(['duro', 'blando', 'rugoso', 'suave, liso', 'sólido', 'líquido', 'mojado', 'seco'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos textura/tacto 2'])
	lista[n].append(['at/t2'])
	lista[n].append(['slippery', 'sticky', 'even', 'uneven', 'sharp', 'blunt', 'clean', 'dirty', 'tight', 'loose'])
	lista[n].append(['resbaladizo', 'pegajoso', 'llano, liso', 'desigual', 'afilado', 'desafilado', 'limpio', 'sucio', 'apretado', 'holgado'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos materiales 1'])
	lista[n].append(['amat1'])
	lista[n].append(['iron', 'steel', 'rubber', 'paper', 'woolen', 'plastic', 'stone', 'wooden'])
	lista[n].append(['de hierro', 'de acero', 'de goma', 'de papel', 'de lana', 'de plástico', 'de piedra', 'de madera'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos materiales 2'])
	lista[n].append(['amat2'])
	lista[n].append(['glass', 'leather', 'silver', 'gold', 'tin', 'cotton'])
	lista[n].append(['de vidrio', 'de cuero', 'de plata', 'de oro', 'de lata', 'de algodón'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos sonido 1'])
	lista[n].append(['ason1'])
	lista[n].append(['loud', 'soft', 'quiet', 'faint', 'audible', 'mute', 'hoarse', 'inaudible'])
	lista[n].append(['alto, fuerte', 'suave', 'suave', 'débil, bajo', 'audible', 'mudo', 'ronco', 'inaudible'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos sonido 2'])
	lista[n].append(['ason2'])
	lista[n].append(['silent', 'deafening', 'noisy', 'deaf', 'shrill', 'melodic'])
	lista[n].append(['silencioso', 'ensordecedor', 'ruidoso', 'sordo', 'agudo', 'melódico'])
	
	n = n+1
	lista.append([])
	lista[n].append(['adjetivos sabor 1'])
	lista[n].append(['asab1'])
	lista[n].append(['sweet', 'salty', 'sour', 'bitter', 'greasy', 'fresh', 'stale', 'tasty'])
	lista[n].append(['dulce', 'salado', 'agrio', 'amargo', 'grasiento', 'fresco', 'rancio', 'rico'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos sabor 2'])
	lista[n].append(['asab2'])
	lista[n].append(['delicious', 'tasteless', 'fatty', 'rotten', 'spicy', 'hot'])
	lista[n].append(['delicioso', 'insípido', 'graso', 'podrido', 'picante', 'picante'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos cocina 1'])
	lista[n].append(['acoc1'])
	lista[n].append(['cooked', 'baked', 'fried', 'boiled', 'peeled', 'sliced'])
	lista[n].append(['cocinado', 'horneado', 'frito', 'hervido', 'pelado', 'rebanado'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos cocina 2'])
	lista[n].append(['acoc2'])
	lista[n].append(['stewed', 'steamed', 'roast', 'broiled', 'cut', 'grated'])
	lista[n].append(['guisado', 'al vapor', 'asado al horno', 'asado a la parrilla', 'cortado', 'rallado'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos condición 1'])
	lista[n].append(['acon1'])
	lista[n].append(['crazy', 'sane', 'sick', 'healthy', 'drunk', 'sober', 'tired', 'broken'])
	lista[n].append(['loco', 'cuerdo', 'enfermo', 'sano', 'borracho', 'sobrio', 'cansado', 'roto'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos condición 2'])
	lista[n].append(['acon2'])
	lista[n].append(['full', 'empty', 'dead', 'alive', 'hungry', 'asleep', 'awake', 'busy'])
	lista[n].append(['lleno', 'vacío', 'muerto', 'vivo', 'hambriento', 'dormido', 'despierto', 'ocupado'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos condición 3'])
	lista[n].append(['acon3'])
	lista[n].append(['idle', 'open', 'closed', 'single', 'married', 'engaged', 'separated', 'divorced'])
	lista[n].append(['ocioso', 'abierto', 'cerrado', 'soltero', 'casado', 'comprometido', 'separado', 'divorciado'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos opinión 1'])
	lista[n].append(['aopi1'])
	lista[n].append(['good', 'bad', 'easy', 'difficult', 'true', 'false', 'careful', 'careless'])
	lista[n].append(['bueno', 'malo', 'fácil', 'difícil', 'verdadero', 'falso', 'cuidadoso', 'descuidado'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos opinión 2'])
	lista[n].append(['aopi2'])
	lista[n].append(['important', 'right', 'wrong', 'useful', 'useless', 'cheap', 'expensive', 'interesting', 'famous', 'unknown'])
	lista[n].append(['importante', 'correcto', 'equivocado', 'útil', 'inútil', 'barato', 'caro', 'interesante', 'famoso', 'desconocido'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos religión 1'])
	lista[n].append(['aopi2'])
	lista[n].append(['catholic', 'protestant', 'anglican', 'baptist', 'christian', 'hindu', 'buddhist', 'Muslin', 'jewish', 'lutheran'])
	lista[n].append(['católico', 'protestante', 'anglicano', 'bautista', 'cristiano', 'hindú', 'budista', 'musulmán', 'judio', 'luterano'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos personalidad positivo 1'])
	lista[n].append(['appo1'])
	lista[n].append(['honest', 'courageous','optimistic', 'intelligent', 'sincere', 'ambitious', 'modest', 'sensible'])
	lista[n].append(['honesto', 'valiente', 'optimista', 'inteligente', 'sincero', 'ambicioso', 'modesto', 'sensato'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos personalidad positivo 2'])
	lista[n].append(['appo2'])
	lista[n].append(['friendly', 'practical', 'considerate', 'tolerant', 'responsible', 'generous', 'patient', 'disciplined', 'humorous', 'sympathetic'])
	lista[n].append(['amistoso', 'práctico', 'considerado', 'tolerante', 'responsable', 'generoso', 'paciente', 'disciplinado', 'divertido', 'comprensivo'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos personalidad negativo 1'])
	lista[n].append(['apne2'])
	lista[n].append(['dishonest', 'pessimistic', 'miserly', 'coward', 'selfish', 'impatient', 'lazy', 'greedy'])
	lista[n].append(['deshonesto', 'pesimista', 'avaro', 'cobarde', 'egoísta', 'impaciente', 'haragán', 'codicioso'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos personalidad negativo 2'])
	lista[n].append(['apne2'])
	lista[n].append(['resentful', 'envious', 'jealous', 'possesive', 'conceited', 'arrogant', 'fussy', 'gullible', 'stubborn', 'careless'])
	lista[n].append(['resentido', 'envidioso', 'celoso', 'posesivo', 'engreído', 'arrogante', 'quisquilloso', 'ingenuo', 'terco', 'negligente'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos apariencia 1'])
	lista[n].append(['aapa1'])
	lista[n].append(['beautiful', 'ugly', 'clean', 'drity', 'full', 'empty', 'simple', 'complex', 'difficult', 'easy'])
	lista[n].append(['lindo', 'feo', 'limpio', 'sucio', 'lleno', 'vacío', 'simple', 'complejo', 'difícil', 'fácil'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos apariencia 2'])
	lista[n].append(['aapa2'])
	lista[n].append(['safe', 'dangerous', 'strong', 'weak', 'same', 'different', 'neat', 'messy', 'rich', 'poor'])
	lista[n].append(['seguro', 'peligroso', 'fuerte', 'débil', 'mismo', 'diferente', 'limpio, ordenado', 'desordenado', 'rico', 'pobre'])
	
	n = n+1
	lista.append([])
	lista[n].append(['adjetivos sentimientos positivo 1'])
	lista[n].append(['asep1'])
	lista[n].append(['amused', 'calm', 'cheerful', 'confident', 'content', 'eager', 'satisfied', 'ecstatic'])
	lista[n].append(['divertido', 'tranquilo', 'alegre', 'confiado', 'contento, satisfecho', 'ansioso', 'satisfecho', 'eufórico'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos sentimientos positivo 2'])
	lista[n].append(['asep2'])
	lista[n].append(['enthusiastic', 'inspired', 'elated', 'energetic', 'pleased', 'excited', 'grateful', 'happy', 'thrilled', 'hopeful'])
	lista[n].append(['entusiasmado', 'inspirado', 'exaltado', 'activo, dinámico', 'satisfecho', 'emocionado', 'agradecido', 'feliz', 'emocionado', 'optimista'])
	
	n = n+1
	lista.append([])
	lista[n].append(['adjetivos sentimientos negativo 1'])
	lista[n].append(['asen1'])
	lista[n].append(['afraid', 'angry', 'annoyed', 'ashamed', 'bored', 'confused', 'depressed', 'lonely'])
	lista[n].append(['con miedo', 'enfadado', 'disgustado', 'avergonzado', 'aburrido', 'confundido', 'deprimido', 'solo y triste'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos sentimientos negativo 2'])
	lista[n].append(['asen2'])
	lista[n].append(['upset', 'sad', 'tired', 'disappointed', 'distressed', 'embarrased', 'frightened', 'frustrated', 'jealous', 'worried'])
	lista[n].append(['molesto', 'triste', 'cansado', 'decepcionado', 'angustiado', 'avergonzado', 'asustado', 'frustrado', 'celoso, envidioso', 'preocupado'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos participios 1'])
	lista[n].append(['apar1'])
	lista[n].append(['alarmed', 'annoyed', 'bored', 'confused', 'depressed', 'excited', 'frustrated', 'interested', 'surprised', 'tired', 'worried'])
	lista[n].append(['alarmado', 'irritado', 'aburrido', 'confundido', 'deprimido', 'emocionado', 'frustrado', 'interesado', 'sorprendido', 'cansado', 'preocupado'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos participios 2'])
	lista[n].append(['apar2'])
	lista[n].append(['alarming', 'annoying', 'boring', 'confusing', 'depressing', 'exciting', 'frustrating', 'interesting', 'surprising', 'tiring', 'worrying'])
	lista[n].append(['alarmante', 'irritante', 'aburridor', 'confuso', 'deprimente', 'emocionante', 'frustrante', 'interesante', 'sorprendente', 'fatigoso', 'preocupante'])

	return lista

'''lista = lista()
num = 0

for x in lista:
	num = len(x[2]) + num

print(num)'''