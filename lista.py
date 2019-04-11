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
	lista[n].append(['arel'])
	lista[n].append(['catholic', 'protestant', 'anglican', 'baptist', 'christian', 'hindu', 'buddhist', 'muslin', 'jewish', 'lutheran'])
	lista[n].append(['católico', 'protestante', 'anglicano', 'bautista', 'cristiano', 'hindú', 'budista', 'musulmán', 'judío', 'luterano'])

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
	lista[n].append(['beautiful', 'ugly', 'clean', 'dirty', 'full', 'empty', 'simple', 'complex', 'difficult', 'easy'])
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

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos comparativos y superlativos (adjetivos)'])
	lista[n].append(['acsa'])
	lista[n].append(['good', 'well', 'bad', 'badly', 'much', 'many', 'little', 'far', 'far'])
	lista[n].append(['bueno', 'bien', 'malo', 'mal', 'mucho', 'muchos', 'poco', 'lejos', 'lejos'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos comparativos y superlativos (comparativo)'])
	lista[n].append(['acsc'])
	lista[n].append(['better', 'better', 'worse', 'worse', 'more', 'more', 'less', 'farther', 'further'])
	lista[n].append(['mejor', 'mejor', 'peor', 'peor', 'más', 'más', 'menos', 'más lejos', 'más lejos'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos comparativos y superlativos (superlativo)'])
	lista[n].append(['acss'])
	lista[n].append(['the best', 'the worst', 'the most', 'the least', 'the farthest', 'the furthest'])
	lista[n].append(['el mejor, de la mejor forma', 'el peor, de la peor forma', 'la mayoría, la mayor parte',  'el menos', 'el más lejano', 'el más lejano'])
	
	n = n+1
	lista.append([])
	lista[n].append(['intensificadores de adjetivos'])
	lista[n].append(['iadj'])
	lista[n].append(['very', 'so', 'too', 'quite', 'pretty', 'fairly', 'somewhat', 'rather', 'a little', 'enough', 'such'])
	lista[n].append(['muy', 'tan', 'demasiado', 'bastante, completamente', 'bastante', 'bastante', 'algo, un tanto', 'bastante, algo, un poco', 'un poco', 'suficiente', 'tal, tales, tan'])

	n = n+1
	lista.append([])
	lista[n].append(['realizando comparaciones igualdad'])
	lista[n].append(['rcig'])
	lista[n].append(['as...as', 'not so...as', 'not as...as', 'as much...as', 'as many...as', 'the same...as'])
	lista[n].append(['tan...como', 'no tan...como', 'no tan...como', 'tanto...como', 'tantos...como', 'la misma...que'])

	n = n+1
	lista.append([])
	lista[n].append(['realizando comparaciones cantidades'])
	lista[n].append(['rcca'])
	lista[n].append(['twice as much as', 'three times as many...as', 'half as much...as'])
	lista[n].append(['dos veces más que', 'tres veces más...que', 'la mitad...que'])
	
	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 1'])
	lista[n].append(['vreg1'])
	lista[n].append(['abandon', 'absolve', 'abuse', 'accelerate', 'accept', 'accustom', 'acquire', 'add'])
	lista[n].append(['abandonar', 'absolver', 'injuriar', 'acelerar', 'aceptar', 'acostumbrar', 'adquirir', 'sumar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 2'])
	lista[n].append(['vreg2'])
	lista[n].append(['admire', 'adore', 'advance', 'advise', 'agree', 'amount', 'announce', 'answer'])
	lista[n].append(['admirar', 'adorar', 'avanzar', 'aconsejar', 'acceder', 'ascender/cantidad', 'anunciar', 'contestar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 3'])
	lista[n].append(['vreg3'])
	lista[n].append(['appear', 'approach', 'arrange', 'ask', 'astonish', 'attempt', 'attract', 'bathe'])
	lista[n].append(['aparecer', 'acercarse', 'arreglar', 'preguntar', 'asombrar', 'intentar', 'atraer', 'bañarse'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 4'])
	lista[n].append(['vreg4'])
	lista[n].append(['believe', 'blame', 'call', 'cash', 'change', 'claim', 'clear', 'close'])
	lista[n].append(['creer', 'culpar', 'llamar', 'cobrar', 'cambiar', 'reclamar', 'aclarar, limpiar', 'cerrar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 5'])
	lista[n].append(['vreg5'])
	lista[n].append(['comb', 'command', 'compare', 'compose', 'consider', 'contain', 'copy', 'cough'])
	lista[n].append(['peinar', 'mandar', 'comparar', 'componer', 'considerar', 'contener', 'copiar', 'toser'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 6'])
	lista[n].append(['vreg6'])
	lista[n].append(['cover', 'crown', 'damage', 'dawn', 'decide', 'defend', 'desire', 'destroy'])
	lista[n].append(['cubrir', 'coronar', 'dañar', 'amanecer', 'decidir', 'defender', 'desear', 'destruir'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 7'])
	lista[n].append(['vreg7'])
	lista[n].append(['develop', 'devour', 'dislike', 'divide', 'drop', 'earn', 'employ', 'encourage'])
	lista[n].append(['desarrollar', 'devorar', 'desaprobar', 'dividir', 'dejar caer', 'ganar', 'emplear', 'animar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 8'])
	lista[n].append(['vreg8'])
	lista[n].append(['enjoy', 'establish', 'evoke', 'expect', 'explode', 'express', 'fail', 'fetch'])
	lista[n].append(['disfrutar', 'establecer', 'evocar', 'esperar', 'estallar', 'expresar', 'fallar', 'ir por'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 9'])
	lista[n].append(['vreg9'])
	lista[n].append(['finish', 'fit', 'float', 'follow', 'gain', 'gather', 'grant', 'guard'])
	lista[n].append(['acabar', 'ajustar', 'flotar', 'seguir', 'ganar', 'recoger', 'conceder', 'guardar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 10'])
	lista[n].append(['vreg10'])
	lista[n].append(['handle', 'happen', 'heat', 'hire', 'hunt', 'imagine', 'import', 'improve'])
	lista[n].append(['manejar', 'suceder', 'calentar', 'alquilar', 'cazar', 'imaginar', 'importar', 'mejorar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 11'])
	lista[n].append(['vreg11'])
	lista[n].append(['increase', 'intend', 'invite', 'join', 'jump', 'kick', 'kiss', 'land'])
	lista[n].append(['aumentar, incrementar', 'intentar', 'invitar', 'unir', 'saltar', 'patear', 'besar', 'aterrizar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 12'])
	lista[n].append(['vreg12'])
	lista[n].append(['laugh', 'like', 'live', 'love', 'maintain', 'measure', 'mention', 'name'])
	lista[n].append(['reír', 'gustar', 'vivir', 'amar', 'mantener', 'medir', 'mencionar', 'nombrar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 13'])
	lista[n].append(['vreg13'])
	lista[n].append(['notice', 'obey', 'oblige', 'offer', 'order', 'pack', 'pass', 'place'])
	lista[n].append(['notar, darse cuenta', 'obedecer', 'obligar', 'ofrecer', 'ordenar', 'empaquetar', 'pasar', 'colocar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos regulares 14'])
	lista[n].append(['vreg14'])
	lista[n].append(['please', 'practise', 'prepare', 'produce', 'propose', 'punish', 'rain', 'receive', 'refuse', 'remain'])
	lista[n].append(['agradar', 'practicar', 'preparar', 'producir', 'proponer', 'castigar', 'llover', 'recibir','rehusar', 'permanecer'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 1'])
	lista[n].append(['vireg1'])
	lista[n].append(['beat, beat, beaten', 'become, became, become', 'begin, began, begun', 'bend, bent, bent', 'bet, bet, bet'])
	lista[n].append(['golpear', 'convertir', 'comenzar', 'doblar', 'apostar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 2'])
	lista[n].append(['vireg2'])
	lista[n].append(['bite, bit, bitten', 'blow, blew, blown', 'break, broke, broken', 'bring, brought, brought', 'broadcast, broadcast, broadcast'])
	lista[n].append(['morder', 'soplar', 'romper', 'traer', 'retransmitir'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 3'])
	lista[n].append(['vireg3'])
	lista[n].append(['build, built, built', 'burst, burst, burst', 'buy, bought, bought', 'catch, caught, caught', 'choose, chose, chosen'])
	lista[n].append(['construir', 'reventar', 'comprar', 'agarrar, coger', 'escoger, elegir'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 4'])
	lista[n].append(['vireg4'])
	lista[n].append(['come, came, come', 'cost, cost, cost', 'creep, crept, crept', 'cut, cut, cut', 'deal, dealt, dealt'])
	lista[n].append(['venir', 'costar', 'reptar,arrastrarse', 'cortar', 'repartir'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 5'])
	lista[n].append(['vireg5'])
	lista[n].append(['dig, dug, dug', 'do, did, done', 'draw, drew, drawn', 'drink, drank, drunk', 'drive, drove, driven'])
	lista[n].append(['cavar', 'hacer', 'dibujar', 'beber', 'conducir'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 6'])
	lista[n].append(['vireg6'])
	lista[n].append(['eat, ate, eaten', 'fall, fell, fallen', 'feed, fed, fed', 'feel, felt, felt', 'fight, fought, fought'])
	lista[n].append(['comer', 'caer', 'alimentar', 'sentir', 'luchar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 7'])
	lista[n].append(['vireg7'])
	lista[n].append(['find, found, found', 'flee, fled, fled', 'fly, flew, flown', 'forbid, forbade, forbidden', 'forget, forgot, forgotten'])
	lista[n].append(['encontrar', 'escapar', 'volar', 'prohibir', 'olvidar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 8'])
	lista[n].append(['vireg8'])
	lista[n].append(['forgive, forgave, forgiven', 'freeze, froze, frozen', 'get, got, gotten', 'give, gave, given', 'go, went, gone'])
	lista[n].append(['perdonar', 'helar, congelar', 'conseguir, obtener', 'dar', 'ir'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 9'])
	lista[n].append(['vireg9'])
	lista[n].append(['grow, grew, grown', 'hang, hung, hung', 'have, had, had', 'hear, heard, heard', 'hide, hid, hidden'])
	lista[n].append(['crecer', 'colgar', 'tener', 'oír', 'esconder'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 10'])
	lista[n].append(['vireg10'])
	lista[n].append(['hit, hit, hit', 'hold, held, held', 'hurt, hurt, hurt', 'keep, kept, kept', 'kneel, knelt, knelt'])
	lista[n].append(['golpear, pegar', 'sostener', 'herir, lastimar', 'guardar, conservar', 'arrodillarse'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 11'])
	lista[n].append(['vireg11'])
	lista[n].append(['know, knew, known', 'lay, laid, laid', 'lead, led, led', 'leave, left, left', 'lend, lent, lent'])
	lista[n].append(['saber, conocer', 'poner, colocar, acostar (a alguien)', 'guiar', 'dejar', 'prestar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 12'])
	lista[n].append(['vireg12'])
	lista[n].append(['let, let, let', 'lie, lay, lain', 'light, lit, lit', 'lose, lost, lost', 'make, made, made'])
	lista[n].append(['permitir', 'tumbarse', 'iluminar, encender', 'perder', 'hacer'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 13'])
	lista[n].append(['vireg13'])
	lista[n].append(['mean, meant, meant', 'meet, met, met', 'pay, paid, paid', 'put, put, put', 'read, read, read'])
	lista[n].append(['significar', 'encontrar, conocer', 'pagar', 'poner', 'leer'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 14'])
	lista[n].append(['vireg14'])
	lista[n].append(['ride, rode, ridden', 'ring, rang, rung', 'rise, rose, risen', 'run, ran, run', 'say, said, said'])
	lista[n].append(['montar', 'sonar', 'surgir, levantarse', 'correr', 'decir'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 15'])
	lista[n].append(['vireg15'])
	lista[n].append(['see, saw, seen', 'seek, sought, sought', 'sell, sold, sold', 'send, sent, sent', 'set, set, set'])
	lista[n].append(['ver', 'rastrear, buscar a fondo', 'vender', 'enviar', 'poner, colocar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 16'])
	lista[n].append(['vireg16'])
	lista[n].append(['sew, sewed, sewn', 'shake, shook, shaken', 'shine, shone, shone', 'shoot, shot, shot', 'show, showed, shown'])
	lista[n].append(['coser', 'agitar', 'brillar', 'disparar, lanzar', 'mostrar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 17'])
	lista[n].append(['vireg17'])
	lista[n].append(['shrink, shrank, shrunk', 'shut, shut, shut', 'sing, sang, sung', 'sink, sank, sunk', 'sit, sat, sat'])
	lista[n].append(['encoger', 'cerrar', 'cantar', 'hundir', 'sentar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 18'])
	lista[n].append(['vireg18'])
	lista[n].append(['sleep, slept, slept', 'slide, slid, slid', 'speak, spoke, spoken', 'spend, spent, spent', 'spit, spat, spat'])
	lista[n].append(['dormir', 'deslizarse, resbalar', 'hablar', 'gastar, pasar, -tiempo-', 'escupir'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 19'])
	lista[n].append(['vireg19'])
	lista[n].append(['split, split, split', 'spread, spread, spread', 'spring, sprang, sprung', 'stand, stood, stood', 'steal, stole, stolen'])
	lista[n].append(['partir, dividir (algo)', 'extender', 'saltar, -de golpe-', 'permanecer parado', 'robar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 20'])
	lista[n].append(['vireg20'])
	lista[n].append(['stick, stuck, stuck', 'sting, stung, stung', 'strike, struck, struck', 'swear, swore, sworn', 'sweep, swept, swept'])
	lista[n].append(['pegar, -algo-', 'picar, escocer', 'golpear, pegar', 'jurar', 'barrer,deshollinar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 21'])
	lista[n].append(['vireg21'])
	lista[n].append(['swim, swam, swum', 'swing, swung, swung', 'take, took, taken', 'teach, taught, taught', 'tear, tore, torn'])
	lista[n].append(['nadar', 'balancearse', 'llevar, coger', 'enseñar', 'romper, rasgar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 22'])
	lista[n].append(['vireg22'])
	lista[n].append(['tell, told, told', 'think, thought, thought', 'throw, threw, thrown', 'understand, understood, understood', 'wake, woke, woken'])
	lista[n].append(['decir', 'pensar, creer', 'lanzar', 'entender', 'despertar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos iregulares 23'])
	lista[n].append(['vireg23'])
	lista[n].append(['wear, wore, worn', 'weep, wept, wept', 'win, won, won', 'write, wrote, written'])
	lista[n].append(['llevar puesto', 'llorar', 'ganar', 'escribir'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras para preguntar 1'])
	lista[n].append(['ppp1'])
	lista[n].append(['what', 'which', 'where', 'when', 'why', 'who', 'whom', 'whose', 'how'])
	lista[n].append(['qué, cuál, cuáles, -ilimitada-', 'qué, cuál, cuáles, -limitada-', 'dónde, adónde', 'cuándo', 'por qué', 'quién, quiénes', 'a quién, a quiénes', 'de quién, de quiénes', 'cómo, qué tan'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras para preguntar 2'])
	lista[n].append(['ppp2'])
	lista[n].append(['how much', 'how many', 'what time', 'what kind', 'how often', 'how long', 'how long ago', 'since when'])
	lista[n].append(['cuánto/a', 'cuántos/as', 'qué hora, a qué hora', 'qué clase, qué tipo', 'con qué frecuencia, cada cuánto', 'cuánto tiempo', 'hace cuánto tiempo', 'desde cuándo'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras para preguntar 3'])
	lista[n].append(['ppp3'])
	lista[n].append(['what...like', 'what...for', 'what...about', 'who...for', 'who...with', 'who...about', 'where...from'])
	lista[n].append(['cómo', 'para qué', 'sobre qué', 'para quién', 'con quién', 'acerca de quién', 'de dónde'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras para preguntar 4'])
	lista[n].append(['ppp4'])
	lista[n].append(['how old', 'how soon', 'how early', 'how late', 'how fast', 'how big', 'how far', 'how tall', 'how deep', 'how heavy'])
	lista[n].append(['qué edad, qué tan viejo', 'qué tan pronto', 'qué tan temprano', 'qué tan tarde', 'qué tan rápido, con qué velocidad, a qué velocidad', 'qué tamaño, qué tan grande', 'a qué distancia, qué tan lejos', 'qué estatura, qué tan alto', 'a qué profundidad, qué tan profundo', 'qué peso, qué tan pesado'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras para preguntar 5'])
	lista[n].append(['ppp5'])
	lista[n].append(['what else', 'where else', 'when else', 'how else', 'who else', 'why else'])
	lista[n].append(['qué más', 'dónde más', 'en qué otro momento', 'de qué otra manera', 'quién más', 'por qué otra razón'])

	n = n+1
	lista.append([])
	lista[n].append(['there be -haber- 1'])
	lista[n].append(['tbh1'])
	lista[n].append(['there is', 'there are', 'there was', 'there were'])
	lista[n].append(['hay, -singular-', 'hay, -plural-', 'hubo, había, -singular-', 'hubo, había, -plural-'])

	n = n+1
	lista.append([])
	lista[n].append(['there be -haber- 2'])
	lista[n].append(['tbh2'])
	lista[n].append(['there has been', 'there have been', 'there had been'])
	lista[n].append(['ha habido, -singular-', 'ha habido, -plural-', 'había habido'])

	n = n+1
	lista.append([])
	lista[n].append(['there be -haber- 3'])
	lista[n].append(['tbh3'])
	lista[n].append(['there will be', 'there will have been', 'there would be', 'there would have been', 'there can be'])
	lista[n].append(['habrá', 'habrá habido', 'habría', 'habría habido', 'puede haber'])

	n = n+1
	lista.append([])
	lista[n].append(['there be -haber- 4'])
	lista[n].append(['tbh4'])
	lista[n].append(['there can be', 'there could be', 'there may be', 'there might be', 'there should be', 'there must be'])
	lista[n].append(['puede haber', 'podría/pudo haber', 'puede haber', 'podría haber', 'debería haber', 'debe haber'])

	n = n+1
	lista.append([])
	lista[n].append(['there be -haber- 5'])
	lista[n].append(['tbh5'])
	lista[n].append(['there could have been', 'there might have been', 'there should have been', 'there must have been'])
	lista[n].append(['podría/pudo haber habido', 'podría haber habido', 'debería haber habido', 'debe haber habido'])

	n = n+1
	lista.append([])
	lista[n].append(['there be -haber- 6'])
	lista[n].append(['tbh6'])
	lista[n].append(['there has to be', 'there have to be', 'there had to be', 'there has to have been', 'there have to have been', 'there had to have been'])
	lista[n].append(['tiene que haber, -singular-', 'tiene que haber,  -plural-', 'tuvo/tenía que haber, -plural-', 'tiene que haber habido, -singular-', 'tiene que haber habido, -plural-', 'tuvo/tenía que haber habido'])

	n = n+1
	lista.append([])
	lista[n].append(['there be -haber- 7'])
	lista[n].append(['tbh7'])
	lista[n].append(['there is going to be', 'there are going to be', 'there was going to be', 'there were going to be'])
	lista[n].append(['va a haber, -singular-', 'va a haber, -plural-', 'íba a haber, -singular-', 'íba a haber, -plural-'])

	n = n+1
	lista.append([])
	lista[n].append(['get 1'])
	lista[n].append(['get1'])
	lista[n].append(['get 1', 'get 2', 'get 3', 'get 4', 'get 5', 'get 6', 'get + adjetive', 'get + past participle'])
	lista[n].append(['conseguir, obtener, comprar, lograr, ganar, sacar', 'recibir (una carta,dinero, una recompensa, una reprimenda)', 'ir a buscar, traer', 'agarrar, contagiarse, tener (una enfermedad)', 'contestar o atender (el teléfono, la puerta)', 'llegar', 'hacerse, volverse, ponerse', 'hacerse, volverse, ponerse'])

	n = n+1
	lista.append([])
	lista[n].append(['get + adjective 1'])
	lista[n].append(['geta1'])
	lista[n].append(['get angry', 'get old', 'get sleepy', 'get hungry', 'get better', 'get full', 'get late', 'get nervous'])
	lista[n].append(['enfadarse', 'envejecer', 'dar sueño', 'tener hambre', 'mejorar', 'llenarse', 'hacerse tarde', 'ponerse nervioso'])

	n = n+1
	lista.append([])
	lista[n].append(['get + adjective 2'])
	lista[n].append(['geta2'])
	lista[n].append(['get rich', 'get wet', 'get upset', 'get fat', 'get happy', 'get thirsty', 'get dark', 'get worse', 'get hot', 'get mad', 'get well'])
	lista[n].append(['enriquecerse', 'mojarse', 'disgustarse', 'engordar', 'ponerse contento, ponerse feliz', 'dar sed', 'oscurecer', 'empeorar', 'ponerse caluroso', 'enojarse', 'mejorar, ponerse bien'])

	n = n+1
	lista.append([])
	lista[n].append(['get + adjective 3'])
	lista[n].append(['geta3'])
	lista[n].append(['get hot', 'get mad', 'get well', 'get cold', 'get bald', 'get sick'])
	lista[n].append(['ponerse caluroso', 'enojarse', 'mejorar, ponerse bien', 'ponerse frío, enfriarse', 'quedarse calvo', 'enfermarse'])

	n = n+1
	lista.append([])
	lista[n].append(['to be able to 1'])
	lista[n].append(['tbat1'])
	lista[n].append(['to be able to', 'to be able to + infinitive', 'be able to, -presente simple-', 'be able to', 'was/were able to', 'could', '"could" y "was/were able to" en oraciones negativas'])
	lista[n].append(['ser capaz de, poder', 'saber, poder, ser capaz de, -capacidad/actitud-', 'poco frecuente', 'se usa en combinación de otros auxiliares', 'pude, indica una capacidad específica para realizar un acto que existió en el pasado en un momento determinado', 'podía, pude, se refiere a una aptitud o capacidad general que existía en el pasado pero que ya no existe más', 'no existe diferencia'])

	n = n+1
	lista.append([])
	lista[n].append(['to manage to + infinitive'])
	lista[n].append(['tmt+i1'])
	lista[n].append(['manage to'])
	lista[n].append(['lograr, poder, -no es un auxiliar modal-'])

	n = n+1
	lista.append([])
	lista[n].append(['used to 1'])
	lista[n].append(['ust1'])
	lista[n].append(['used to', 'would + adverbio de frecuencia + verbo infinitivo', 'used to'])
	lista[n].append(['soler, hábitos del pasado, de cosas que pasaban frecuentemente en el pasado pero que ya dejaron de suceder', 'soler, hábitos del pasado', 'hablar de cosas que eran verdaderas pero dejaron de serlas'])

	n = n+1
	lista.append([])
	lista[n].append(['to be/get used to 1'])
	lista[n].append(['tbgut1'])
	lista[n].append(['to be/get used to', 'to be used to', 'to get used to'])
	lista[n].append(['se refieren al presente y si va antes de un verbo este debe de estar en gerundio', 'estar acostumbrado a', 'acostumbrarse a'])

	n = n+1
	lista.append([])
	lista[n].append(['to have/get something done 1'])
	lista[n].append(['thgsd1'])
	lista[n].append(['to have/get something done', 'have + noun + past participle', 'get'])
	lista[n].append(['alguien hace algo por alguien, alguien hace hacer algo, se le hace algo a alguien', 'sujeto + have + a quién + verbo en participio', 'informal'])

	n = n+1
	lista.append([])
	lista[n].append(['to want somebody to do something 1'])
	lista[n].append(['twsbtdst1'])
	lista[n].append(['to want somebody to do something', 'sujeto + want (conjugado) + a alguien + to + verbo aplicado a alguien', 'want + object + to infinitive'])
	lista[n].append(['sujeto + want (somebody/pronombre acusativo) + to + (something)', 'you wanted me to go to the lake', 'en español es pretérito del subjuntivo'])

	n = n+1
	lista.append([])
	lista[n].append(['expresar acuerdo'])
	lista[n].append(['eacue'])
	lista[n].append(['so + verbo principal conjugado de quién también + quién tambien, -oraciones afirmativas-', 'neither/nor + verbo principal conjugado de quién tampoco + quién tampoco, -oraciones negativas-'])
	lista[n].append(['quién también + verbo principal conjugado de quién tambien + too, -oraciones afirmativas-', 'quién tampoco + verbo principal negativo conjugado de quién tampoco + either '])

	n = n+1
	lista.append([])
	lista[n].append(['gerundio'])
	lista[n].append(['gerun'])
	lista[n].append(['verbo + ing', 'preposiciones + gerundio, -siempre-', 'los verbos en gerundio pueden modificar sustantivos'])
	lista[n].append(['hace a un verbo sustantivo quedando en forma infinitiva en español', 'preposiciones + gerundio, -siempre-', 'verbo + ing + sustantivo'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario culinario 1'])
	lista[n].append(['vcul1'])
	lista[n].append(['add', 'bake', 'beat', 'blend', 'boil', 'bone', 'break', 'broil'])
	lista[n].append(['agregar', 'hornear', 'batir', 'combinar, mezclar', 'hervir', 'deshuesar', 'romper', 'asar a la parrilla'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario culinario 2'])
	lista[n].append(['vcul2'])
	lista[n].append(['chill', 'chop', 'coat', 'cook', 'cover', 'curdle', 'cut into strips', 'decorate'])
	lista[n].append(['refrigerar, enfriar', 'picar, cortar en trozos', 'rebozar', 'cocinar', 'cubrir', 'cuajar', 'cortar en tiras', 'decorar'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario culinario 3'])
	lista[n].append(['vcul3'])
	lista[n].append(['defrost', 'dice', 'dilute', 'dissolve', 'dry',  'empty', 'fill', 'flip'])
	lista[n].append(['descongelar', 'cortar en cubitos', 'diluir', 'disolver', 'secar', 'vaciar', 'llenar', 'dar vuelta'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario culinario 4'])
	lista[n].append(['vcul4'])
	lista[n].append(['fold', 'fry', 'glaze', 'grate', 'grease', 'grill', 'grind', 'halve'])
	lista[n].append(['doblar', 'freir', 'glasear', 'rallar', 'engrasar', 'asar a la parrilla', 'moler', 'partir en dos'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario culinario 5'])
	lista[n].append(['vcul5'])
	lista[n].append(['heat', 'knead', 'liquidize', 'melt', 'mince', 'mix', 'peel', 'pour'])
	lista[n].append(['calentar', 'amasar', 'licuar', 'derretir', 'picar carne', 'mezclar', 'pelar', 'volcar, verter'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario culinario 6'])
	lista[n].append(['vcul6'])
	lista[n].append(['press', 'put', 'remove', 'rinse', 'roast', 'roll out', 'scoop up', 'seal'])
	lista[n].append(['presionar, apretar', 'colocar, poner', 'quitar, sacar', 'enjuagar', 'asar', 'aplanar, extender', 'ahuecar (con cuchara)', 'sellar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos culinarios 7'])
	lista[n].append(['vcul7'])
	lista[n].append(['season', 'serve', 'shake', 'sharpen', 'sieve', 'simmer', 'slice', 'smoke'])
	lista[n].append(['aderezar', 'servir', 'agitar, sacudir', 'afilar', 'tamizar', 'hervir a fuego lento', 'rebanar', 'ahumar'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos culinarios 8'])
	lista[n].append(['vcul8'])
	lista[n].append(['soak', 'spill', 'sprinkle', 'squeeze', 'steam', 'stew', 'stir', 'stir-fry'])
	lista[n].append(['remojar', 'derramar', 'rociar, salpicar', 'exprimir', 'cocinar al vapor', 'guisar, estofar', 'freír', 'sofreír'])

	n = n+1
	lista.append([])
	lista[n].append(['verbos culinarios 9'])
	lista[n].append(['vcul9'])
	lista[n].append(['strain', 'stuff', 'thicken', 'trim', 'waste', 'whisk'])
	lista[n].append(['colar', 'rellenar', 'espesar', 'recortar', 'desperdiciar', 'batir'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario tragos y bebidas 1'])
	lista[n].append(['vtyb1'])
	lista[n].append(['apple juice', 'brown beer', 'can of Coke', 'champagne', 'cider', 'coffe', 'gin', 'hot chocolate'])
	lista[n].append(['jugo de manzana', 'cerveza negra', 'lata de Coca-Cola', 'champán', 'sidra', 'café', 'ginebra', 'chocolate caliente'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario tragos y bebidas 2'])
	lista[n].append(['vtyb2'])
	lista[n].append(['juice', 'lemonade', 'light soda', 'liqueur', 'milkshake', 'orange juice', 'pineapple juice', 'red wine'])
	lista[n].append(['jugo', 'limonada', 'refresco de dieta', 'licor', 'batido', 'jugo de naranja', 'jugo de piña', 'vino tinto'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario tragos y bebidas 3'])
	lista[n].append(['ctyb3'])
	lista[n].append(['rum', 'soda', 'soft drink', 'sparkling water', 'still water', 'tea', 'tomato juice', 'vodka'])
	lista[n].append(['ron', 'refresco', 'bebida sin alcohol', 'agua mineral con gas', 'agua mineral sin gas', 'té', 'jugo de tomate', 'vodka'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario tragos y bebidas 4'])
	lista[n].append(['vtyb4'])
	lista[n].append(['water', 'whisky', 'white wine', 'wine'])
	lista[n].append(['agua', 'whisky', 'vino blanco', 'vino'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario peces y mariscos 1'])
	lista[n].append(['vpym1'])
	lista[n].append(['clam', 'cockles', 'cod', 'crab', 'eel', 'fried shrimps', 'hake', 'halibut'])
	lista[n].append(['almeja', 'berbechos', 'bacalao', 'cangrejo de mar', 'anguila', 'camarones fritos', 'merluza', 'fletán, hipogloso, pez mantequilla'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario peces y mariscos 2'])
	lista[n].append(['vpym2'])
	lista[n].append(['herring', 'king prawn', 'lobster', 'mackerel', 'marinade', 'mussel', 'octopus', 'oyster'])
	lista[n].append(['arenque', 'langostino', 'langosta', 'caballa', 'escabeche', 'mejillón', 'pulpo', 'ostra'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario peces y mariscos 3'])
	lista[n].append(['vpym3'])
	lista[n].append(['plaice', 'pollack', 'prawn', 'salmon', 'sardines', 'scallop', 'shark', 'shellfish'])
	lista[n].append(['platija', 'abadejo', 'camarón', 'salmón', 'sardinas', 'vieira (tiene concha)', 'tiburón', 'mariscos'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario peces y mariscos 4'])
	lista[n].append(['vpym4'])
	lista[n].append(['shrimp', 'snail', 'sole', 'spider crab', 'squid', 'swordfish', 'trout', 'tuna'])
	lista[n].append(['camarón', 'caracol', 'lenguado', 'centolla', 'calamar', 'pez espada', 'trucha', 'atún'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario comidas 1'])
	lista[n].append(['vcom1'])
	lista[n].append(['bacon', 'baked potatoes', 'beef', 'beef steak', 'blood sausage', 'brains', 'canneloni', 'cheese'])
	lista[n].append(['tocino', 'papas al horno', 'carne de vaca', 'bistec', 'morcilla', 'sesos', 'canelones', 'queso'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario comidas 2'])
	lista[n].append(['vcom2'])
	lista[n].append(['cheeseburger', 'chicken', 'cold cuts', 'dessert', 'french fries', 'fried chicken', 'gnocchi', 'ground meat'])
	lista[n].append(['hamburguesa de queso', 'pollo', 'fiambres', 'postre', 'papas a la francesa', 'pollo frito', 'ñoquis', 'carne picada, carne molida'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario comidas 3'])
	lista[n].append(['vcom3'])
	lista[n].append(['ham', 'hamburger', 'hot dog', 'kidneys', 'lamb', 'lassagne', 'liver', 'macaroni'])
	lista[n].append(['jamón', 'hamburguesa', 'perro caliente', 'riñones', 'cordero', 'lasaña', 'hígado', 'macarrones'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario comidas 4'])
	lista[n].append(['vcom4'])
	lista[n].append(['mashed potatoes', 'mayonnaise', 'meatballs', 'noodles', 'omelet', 'pasta', 'pizza', 'pork'])
	lista[n].append(['puré de papas', 'mayonesa', 'albóndigas', 'tallarines, tipo de fideo', 'omelet', 'pasta', 'pizza', 'carne de puerco'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario comidas 5'])
	lista[n].append(['vcom5'])
	lista[n].append(['pork chops', 'potato chips', 'ravioli', 'ribs', 'roast beef', 'salad', 'salami', 'sauce'])
	lista[n].append(['costillas de puerco', 'papas fritas de bolsa', 'ravioles', 'costillas', 'rosbif, carne de res asada', 'ensalada', 'salami', 'salsa'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario comidas 6'])
	lista[n].append(['vcom6'])
	lista[n].append(['sausage', 'scrambled eggs', 'soup', 'spaghetti', 'steak', 'stew', 'tomato sauce', 'turkey', 'veal', 'vegetables'])
	lista[n].append(['salchicha, chorizo', 'huevos revueltos', 'sopa', 'espagueti', 'bistéc', 'guiso', 'salsa de tomate', 'pavo', 'carne de ternera', 'verduras'])
	
	n = n+1
	lista.append([])
	lista[n].append(['vocabulario carnes y aves 1'])
	lista[n].append(['vcya1'])
	lista[n].append(['bacon', 'beef', 'beef steak', 'black pudding', 'blood sausage', 'boneless', 'brains'])
	lista[n].append(['tocino', 'carne de vaca', 'bistéc', 'morcilla', 'morcilla', 'deshuesado', 'sesos'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulariocarnes y aves 2'])
	lista[n].append(['vcya2'])
	lista[n].append(['breast', 'sheeseburger', 'chicken', 'chop', 'cold meats', 'cooked', 'cutlet', 'fowl'])
	lista[n].append(['pechuga', 'hamburguesa de queso', 'pollo', 'chuleta', 'fiambres', 'cocida', 'chuleta', 'ave de corral'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario carnes y aves 3'])
	lista[n].append(['vcya3'])
	lista[n].append(['game', 'goat', 'gravy', 'grilled', 'ground meat', 'ham', 'hamburger', 'kidneys'])
	lista[n].append(['animales de caza', 'cabrito', 'jugo de carne', 'a la parrilla', 'carne picada, carne molida', 'jamón', 'hamburguesa', 'riñones'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario carnes y aves 4'])
	lista[n].append(['vcya4'])
	lista[n].append(['lamb', 'liver', 'marrow', 'meatballs', 'medium rare', 'mutton', 'pork', 'pork chops'])
	lista[n].append(['cordero', 'hígado', 'médula', 'albóndigas', 'medio hecho', 'carne de oveja', 'carne de cerdo', 'chuletas de cerdo'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario carnes y aves 5'])
	lista[n].append(['vcya5'])
	lista[n].append(['pork loin', 'pork sausage', 'poultry', 'rare', 'ribs', 'roast beef', 'roasted', 'salami'])
	lista[n].append(['lomo de cerdo', 'chorizo', 'carne de ave', 'poco cocida', 'costillas', 'carne asada', 'asada', 'salami'])

	n = n+1
	lista.append([])
	lista[n].append(['vocabulario carnes y aves 6'])
	lista[n].append(['vcya6'])
	lista[n].append(['sausage', 'sirloin steak', 'steak', 'suckling pig', 'tongue', 'tripe', 'turkey', 'veal', 'veal steak', 'venison', 'well done'])
	lista[n].append(['salchicha, chorizo', 'bife de lomo', 'bistéc', 'lechón', 'lengua', 'tripas', 'pavo', 'carne de ternera', 'bistéc de ternera', 'carne de venado', 'bien cocida'])
	
	n = n+1
	lista.append([])
	lista[n].append(['especias y condimentos 1'])
	lista[n].append(['eyc1'])
	lista[n].append(['aniseed', 'basil', 'bayleaf', 'brine', 'capers', 'celery', 'chilli', 'chives'])
	lista[n].append(['anís', 'albahaca', 'laurel', 'salmuera', 'alcaparras', 'apio', 'ají', 'cebolletas'])

	n = n+1
	lista.append([])
	lista[n].append(['especias y condimentos 2'])
	lista[n].append(['eyc2'])
	lista[n].append(['cinnamon', 'clove', 'coriander', 'cumin', 'curry', 'dill', 'dressing', 'fennel'])
	lista[n].append(['canela', 'clavo de olor', 'cilantro', 'comino', 'curry', 'eneldo', 'aliño', 'hinojo'])

	n = n+1
	lista.append([])
	lista[n].append(['especias y condimientos 3'])
	lista[n].append(['eyc3'])
	lista[n].append(['garlic', 'ginger', 'gravy', 'herbs', 'ketchup', 'mayonnaise', 'mint', 'mustard'])
	lista[n].append(['ajo', 'jengibre', 'salsa del jugo de la carne', 'hierbas aromáticas', 'kétchup, cátchup, cátsup', 'mayonesa', 'menta', 'mostaza'])

	n = n+1
	lista.append([])
	lista[n].append(['especias y condimentos 4'])
	lista[n].append(['eyc4'])
	lista[n].append(['nutmeg', 'oregano', 'paprika', 'parsley', 'pepper', 'pepper corn', 'pickled onions', 'rhubarb'])
	lista[n].append(['nuez moscada', 'orégano', 'pimentón dulce', 'perejil', 'pimienta', 'grano de pimienta', 'cebollas en vinagre', 'ruibardo'])

	n = n+1
	lista.append([])
	lista[n].append(['especias y condimentos 5'])
	lista[n].append(['eyc5'])
	lista[n].append(['rosemary', 'saffron', 'sage', 'salad dressing', 'salt', 'sauce', 'sesame', 'sorrel'])
	lista[n].append(['romero', 'azafrán', 'salvia', 'aderezo', 'sal', 'salsa', 'sésamo, ajonjolí', 'acedera'])

	n = n+1
	lista.append([])
	lista[n].append(['especias y condimentos 6'])
	lista[n].append(['eyc6'])
	lista[n].append(['sugar', 'syrup', 'tarragon', 'thyme', 'truffle', 'vanilla', 'vinegar'])
	lista[n].append(['azúcar', 'almíbar', 'estragón', 'tomillo', 'trufa', 'vainilla', 'vinagre'])

	n = n+1
	lista.append([])
	lista[n].append(['frutas 1'])
	lista[n].append(['fru1'])
	lista[n].append(['almonds', 'apple', 'apricot', 'avocado', 'banana', 'blackberry', 'cherry', 'chestnuts'])
	lista[n].append(['almendras', 'manzana', 'damasco, albaricoque', 'aguacate', 'platano', 'zarzamora', 'cereza', 'castañas'])

	n = n+1
	lista.append([])
	lista[n].append(['frutas 2'])
	lista[n].append(['fru2'])
	lista[n].append(['coconuts', 'date', 'fig', 'grapefruit', 'grapes', 'hazelnuts', 'lemon', 'lime'])
	lista[n].append(['cocos', 'dátil', 'higo', 'toronja', 'uvas', 'avellanas', 'limón', 'lima'])

	n = n+1
	lista.append([])
	lista[n].append(['frutas 3'])
	lista[n].append(['fru3'])
	lista[n].append(['mango', 'medlar', 'melon', 'mulberry', 'orange', 'peach', 'peanuts', 'pear'])
	lista[n].append(['mango', 'níspero', 'melón', 'mora', 'naranja', 'durazno', 'cacahuates', 'pera'])

	n = n+1
	lista.append([])
	lista[n].append(['frutas 4'])
	lista[n].append(['fru4'])
	lista[n].append(['pineapple', 'plum', 'pomegranate', 'quince', 'raspberry', 'seed', 'strawberry', 'tangerine', 'walnuts', 'watermelon'])
	lista[n].append(['piña', 'ciruela', 'granada', 'membrillo', 'frambuesa', 'semilla', 'fresa', 'mandarina', 'nueces', 'sandía'])

	n = n+1
	lista.append([])
	lista[n].append(['verduras y vegetales 1'])
	lista[n].append(['vyv1'])
	lista[n].append(['artichoke', 'asparagus', 'beans', 'beet', 'bell pepper', 'broad beans', 'broccoli', 'brussels sprouts'])
	lista[n].append(['alcachofa', 'espárragos', 'frijoles', 'remolacha', 'pimiento morrón', 'habas', 'brócoli', 'coles de bruselas'])

	n = n+1
	lista.append([])
	lista[n].append(['verduras y vegetales 2'])
	lista[n].append(['vyv2'])
	lista[n].append(['cabbage', 'carrot', 'cauliflower', 'celery', 'chard', 'chick peas', 'chilli', 'cucumber'])
	lista[n].append(['repollo, col', 'zanahoria', 'coliflor', 'apio', 'acelga', 'garbanzos', 'ají picante', 'pepino'])

	n = n+1
	lista.append([])
	lista[n].append(['verduras y vegetales 3'])
	lista[n].append(['vyv3'])
	lista[n].append(['eggplant', 'fennel', 'garlic', 'green onion', 'leek', 'lentils', 'lettuce', 'mushromms'])
	lista[n].append(['berenjena', 'hinojo', 'ajo', 'cebolleta', 'puerro', 'lentejas', 'lechuga', 'hongos'])

	n = n+1
	lista.append([])
	lista[n].append(['verduras y vegetales 4'])
	lista[n].append(['vyv4'])
	lista[n].append(['onion', 'parsley', 'peas', 'pepper', 'potato', 'pumpkin', 'spinach', 'squash'])
	lista[n].append(['cebolla', 'perejil', 'chicharos', 'pimiento', 'papa', 'calabaza', 'espinaca', 'chayote'])

	n = n+1
	lista.append([])
	lista[n].append(['verduras y vegetales 5'])
	lista[n].append(['vyv5'])
	lista[n].append(['string beans', 'sweet corn', 'sweet potato', 'tomato', 'turnip', 'watercress', 'zucchini'])
	lista[n].append(['ejotes', 'maíz tierno', 'camote', 'tomate', 'nabo', 'berro', 'calabazita, calabacin'])

	n = n+1
	lista.append([])
	lista[n].append(['playa y el mar 1'])
	lista[n].append(['pyem1'])
	lista[n].append(['bathers', 'bay', 'beach ball', 'binoculars', 'breaker', 'breeze', 'clam', 'cliff'])
	lista[n].append(['bañistas', 'bahía', 'pelota de playa', 'binoculares', 'ola grande', 'briza', 'almeja', 'acantilado'])

	n = n+1
	lista.append([])
	lista[n].append(['playa y mar 2'])
	lista[n].append(['pym2'])
	lista[n].append(['coast', 'cooler', 'coral', 'crab', 'current', 'dressing rooms', 'dune', 'folding chair'])
	lista[n].append(['costa', 'hielera', 'coral', 'cangrejo', 'corriente', 'vestuarios', 'duna', 'silla plegable'])

	n = n+1
	lista.append([])
	lista[n].append(['playa y mar 3'])
	lista[n].append(['pym3'])
	lista[n].append(['goggles', 'horizon', 'island', 'kite', 'life preserver', 'lifeguard', 'motorboat', 'ocean'])
	lista[n].append(['lentes de protección, lentes de natación ', 'horizonte', 'isla', 'papalote', 'salvavidas', 'salvavidas, -persona-', 'lancha', 'océano'])

	n = n+1
	lista.append([])
	lista[n].append(['playa y mar 4'])
	lista[n].append(['pym4'])
	lista[n].append(['pail', 'sailboat', 'sand', 'sandals', 'sandcastle', 'sea', 'seaweed', 'shark'])
	lista[n].append(['cubeta', 'velero', 'arena', 'sandalias', 'castillo de arena', 'mar', 'alga marina', 'tiburón'])

	n = n+1
	lista.append([])
	lista[n].append(['playa y mar 5'])
	lista[n].append(['pym5'])
	lista[n].append(['shell', 'shore', 'shovel', 'snail', 'starfish', 'sunburn', 'sunglasses', 'sunscreen'])
	lista[n].append(['concha', 'orilla', 'pala', 'caracol', 'estrella de mar', 'quemadura de sol, requemada', 'lentes para el sol', 'protector solar, bloqueador solar'])

	n = n+1
	lista.append([])
	lista[n].append(['playa y mar 6'])
	lista[n].append(['pym6'])
	lista[n].append(['suntan lotion', 'surfboard', 'surfers', 'swimmer', 'swimming pool', 'swimming trunks', 'swimsuit', 'tide'])
	lista[n].append(['loción bronceadora', 'tabla de surf', 'surfistas', 'nadador', 'piscina', 'pantalón de baño', 'traje de baño', 'marea'])

	n = n+1
	lista.append([])
	lista[n].append(['playa y mar 7'])
	lista[n].append(['pym7'])
	lista[n].append(['towel', 'umbrella', 'wave'])
	lista[n].append(['toalla', 'sombrilla', 'ola'])

	n = n+1
	lista.append([])
	lista[n].append(['campamento y pesca 1'])
	lista[n].append(['cyp1'])
	lista[n].append(['backpack', 'bait', 'barbecue', 'basket', 'binoculars', 'blanket', 'camp fire', 'camp stove'])
	lista[n].append(['mochila', 'cebo, carnada', 'parrilla', 'canasta', 'binoculares', 'manta', 'fogata', 'estufa de campaña'])

	n = n+1
	lista.append([])
	lista[n].append(['campamento y pesca 2'])
	lista[n].append(['cyp2'])
	lista[n].append(['camper', 'campsite', 'canoe', 'caravan', 'cascade', 'compass', 'cooler', 'facilities'])
	lista[n].append(['campista', 'sitio de camping', 'canoa, piragua', 'remolque', 'cascada', 'brújula', 'nevera, hielera', 'instalaciones'])

	n = n+1
	lista.append([])
	lista[n].append(['campamento y pesca 3'])
	lista[n].append(['cyp3'])
	lista[n].append(['firewood', 'first-aid kit', 'fishing line', 'fishing net', 'fishing rod', 'flashlight', 'forest', 'forest ranger'])
	lista[n].append(['leña', 'botiquín de primeros auxilios', 'línea de pesca', 'red de pesca', 'caña de pescar', 'linterna', 'bosque, selva', 'guardabosques'])

	n = n+1
	lista.append([])
	lista[n].append(['campamento y pesca 4'])
	lista[n].append(['cyp4'])
	lista[n].append(['hiking boots', 'hill', 'hook', 'insect repellent', 'lake', 'lantern', 'logs', 'map'])
	lista[n].append(['botas de excursionismo', 'colina, sierra', 'anzuelo, gancho', 'repelente de insectos', 'lago', 'farol', 'leños, troncos', 'mapa'])

	n = n+1
	lista.append([])
	lista[n].append(['campamento y pesca 5'])
	lista[n].append(['cyp5'])
	lista[n].append(['matches', 'mountain', 'penknife', 'raft', 'raincoat', 'rapids', 'rifle', 'rope'])
	lista[n].append(['fósforos', 'montaña', 'navaja, cortaplumas', 'balsa', 'impermeable', 'rápidos', 'rifle', 'soga, cuerda'])

	n = n+1
	lista.append([])
	lista[n].append(['campamento y pesca 6'])
	lista[n].append(['cyp6'])
	lista[n].append(['shotgun', 'sleeping bag', 'stream', 'tent', 'thermos', 'toilet paper', 'toilet', 'trail'])
	lista[n].append(['escopeta', 'bolsa de dormir', 'arroyo', 'carpa, tienda de lona, casa de campaña', 'termo', 'papel higiénico, papel de baño', 'retrete, aseo, baño, taza de baño', 'senda, sendero'])

	n = n+1
	lista.append([])
	lista[n].append(['campamento y pesca 7'])
	lista[n].append(['cyp7'])
	lista[n].append(['trailer', 'trap', 'valley', 'water bottle', 'waterfall', 'wilderness', 'wildlife', 'wood'])
	lista[n].append(['remolque', 'trampa', 'valle', 'cantimplora', 'catarata', 'tierra salvaje', 'flora y fauna', 'bosque'])

	n = n+1
	lista.append([])
	lista[n].append(['instrumentos musicales 1'])
	lista[n].append(['imus1'])
	lista[n].append(['accordion', 'bagpipes', 'banjo', 'bass guitar', 'bassoon', 'baton', 'bongo', 'bugle'])
	lista[n].append(['acordeón', 'gaita', 'banjo', 'bajo', 'fagot', 'batuta', 'bongó', 'clarín'])

	n = n+1
	lista.append([])
	lista[n].append(['instrumentos musicales 2'])
	lista[n].append(['imus2'])
	lista[n].append(['castanets', 'cello', 'clarinet', 'cymbals', 'double bass', 'drum', 'drums', 'drumsticks'])
	lista[n].append(['castañuelas', 'violoncelo', 'clarinete', 'platillos', 'contrabajo', 'tambor', 'batería', 'palillos'])

	n = n+1
	lista.append([])
	lista[n].append(['instrumentos musicales 3'])
	lista[n].append(['imus3'])
	lista[n].append(['fiddle', 'flute', 'french horn', 'gong', 'grand piano', 'guitar', 'harmonica', 'harp'])
	lista[n].append(['violín', 'flauta', 'trompa', 'gong', 'piano de cola', 'guitarra', 'armónica', 'harpa'])

	n = n+1
	lista.append([])
	lista[n].append(['instrumentos musicales 4'])
	lista[n].append(['imus4'])
	lista[n].append(['kettledrum', 'keyboard', 'keys', 'lute', 'mandoline', 'maraca', 'oboe', 'organ'])
	lista[n].append(['timbal', 'teclado', 'teclas', 'laúd', 'mandolina', 'maraca', 'oboe', 'órgano'])

	n = n+1
	lista.append([])
	lista[n].append(['instrumentos musicales 5'])
	lista[n].append(['imus5'])
	lista[n].append(['piano', 'piccolo', 'saxophone', 'snare drum','string', 'synthesizer', 'tambourine', 'trombone'])
	lista[n].append(['piano', 'flautín', 'saxofón', 'redoblante', 'cuerda', 'sintetizador', 'pandereta', 'trombón'])

	n = n+1
	lista.append([])
	lista[n].append(['instrumentos musicales 6'])
	lista[n].append(['imus6'])
	lista[n].append(['trumpet', 'tuba', 'violin', 'xylophone'])
	lista[n].append(['trompeta', 'tuba', 'violín', 'xilofón'])

	n = n+1
	lista.append([])
	lista[n].append(['esparcimiento y pasatiempos 1'])
	lista[n].append(['eyp1'])
	lista[n].append(['billiards', 'bowling', 'brainteasers', 'camping', 'canoeing', 'card games', 'carpentry', 'checkers'])
	lista[n].append(['billar', 'juego de bolos, boliche', 'adivinanzas, acertijos', 'campamento', 'piragüismo', 'juegos de cartas', 'carpintería', 'juego de damas'])

	n = n+1
	lista.append([])
	lista[n].append(['esparcimiento y pasatiempos 2'])
	lista[n].append(['eyp2'])
	lista[n].append(['chess', 'computing', 'cooking', 'crossword puzzle', 'cycling', 'dancing', 'darts', 'dice'])
	lista[n].append(['ajedrez', 'informática', 'cocina', 'crucigrama', 'ciclismo', 'baile', 'juego de dardos', 'dados'])

	n = n+1
	lista.append([])
	lista[n].append(['esparcimiento y pasatiempos 3'])
	lista[n].append(['eyp3'])
	lista[n].append(['dominoes', 'drawing', 'embroidery', 'engraving', 'fishing', 'gambling', 'gardening', 'hang-gliding'])
	lista[n].append(['dominó', 'dibujo', 'bordado', 'grabado', 'pesca', 'juegos de apuestas', 'jardinería', 'ala delta'])

	n = n+1
	lista.append([])
	lista[n].append(['esparcimiento y pasatiempos 4'])
	lista[n].append(['eyp4'])
	lista[n].append(['hiking', 'horseback riding', 'hunting', 'jigsaw puzzle', 'jogging', 'knitting', 'marbles', 'mountaineering'])
	lista[n].append(['excursionismo', 'equitación', 'caza', 'rompecabezas', 'trote, footing', 'labor, tejido de punto', 'juego de bolitas', 'alpinismo, montañismo'])

	n = n+1
	lista.append([])
	lista[n].append(['esparcimiento y pasatiempos 5'])
	lista[n].append(['eyp5'])
	lista[n].append(['painting', 'parachuting', 'photography', 'pool', 'pot-holing', 'pottery', 'reading', 'riddles'])
	lista[n].append(['pintura', 'paracaidismo', 'fotografía', 'billar americano', 'espeleología', 'cerámica, alfarería', 'lectura', 'adivinanzas'])

	n = n+1
	lista.append([])
	lista[n].append(['esparcimiento y pasatiempos 6'])
	lista[n].append(['eyp6'])
	lista[n].append(['sculpting', 'sewing', 'singing', 'skating', 'skiing', 'stamp collecting', 'surfing', 'video games', 'yoga'])
	lista[n].append(['esculpido', 'costura', 'canto', 'patinaje', 'esquí', 'filatelia', 'surf', 'videojuegos', 'yoga'])

	n = n+1
	lista.append([])
	lista[n].append(['actividades deportivas 1'])
	lista[n].append(['adep1'])
	lista[n].append(['aerobics', 'archery', 'athletics', 'badminton', 'baseball', 'basketball', 'bicycling', 'billiards'])
	lista[n].append(['ejercicios aeróbicos', 'arquería', 'atletismo', 'bádminton', 'béisbol', 'básquet', 'ciclismo', 'billar'])

	n = n+1
	lista.append([])
	lista[n].append(['actividades deportivas 2'])
	lista[n].append(['adep2'])
	lista[n].append(['bowling', 'boxing', 'canoeing', 'car racing', 'diving', 'fencing', 'fishing', 'football'])
	lista[n].append(['bolos', 'boxeo', 'canotaje', 'automovilismo', 'buceo', 'esgrima', 'pesca', 'fútbol americano'])

	n = n+1
	lista.append([])
	lista[n].append(['actividades deportivas 3'])
	lista[n].append(['adep3'])
	lista[n].append(['golf', 'gymnastics', 'hang gliding', 'hockey', 'horse racing', 'horse riding', 'hunting', 'ice hockey'])
	lista[n].append(['golf', 'gimnasia', 'aladeltismo', 'hockey', 'carrera de caballos', 'equitación', 'caza', 'hockey sobre hielo'])

	n = n+1
	lista.append([])
	lista[n].append(['actividades deportivas 4'])
	lista[n].append(['adep4'])
	lista[n].append(['ice skating', 'jogging', 'karate', 'martial arts', 'motorboat racing', 'mountaineering', 'parachuting', 'ping-pong'])
	lista[n].append(['patinaje sobre hielo', 'trote', 'karate', 'artes marciales', 'carrera de lanchas', 'montañismo', 'paracaidismo', 'tenis de mesa'])

	n = n+1
	lista.append([])
	lista[n].append(['actividades deportivas 5'])
	lista[n].append(['adep5'])
	lista[n].append(['polo', 'pool', 'rowing', 'sailing', 'skating', 'skiing', 'skydiving', 'soccer'])
	lista[n].append(['polo', 'pool, billar americano', 'remo', 'navegación a vela', 'patinaje', 'esquí', 'paracaidismo acrobático', 'fútbol'])

	n = n+1
	lista.append([])
	lista[n].append(['actividades deportivas 6'])
	lista[n].append(['adep6'])
	lista[n].append(['surfing', 'swimming', 'target shooting', 'tennis', 'volleyball', 'water skiing', 'weight lifting', 'windsurfing', 'wrestling'])
	lista[n].append(['surf', 'natación', 'tiro al blanco', 'tenis', 'vóleibol', 'esquí acuático', 'pesas', 'windsurf', 'lucha libre'])

	n = n+1
	lista.append([])
	lista[n].append(['aves 1'])
	lista[n].append(['aves1'])
	lista[n].append(['blackbird', 'canary', 'cardinal', 'chick', 'chicken', 'cock', 'cockatoo', 'condor'])
	lista[n].append(['mirlo', 'canario', 'cardenal', 'pollito', 'pollo', 'gallo', 'cacatúa', 'cóndor'])

	n = n+1
	lista.append([])
	lista[n].append(['aves 2'])
	lista[n].append(['aves2'])
	lista[n].append(['crane', 'crow', 'duck', 'eagle', 'falcon', 'feather', 'flamingo', 'goldfinch'])
	lista[n].append(['grulla', 'cuervo', 'pato', 'águila', 'halcón', 'pluma', 'flamenco', 'jilguero'])

	n = n+1
	lista.append([])
	lista[n].append(['aves 3'])
	lista[n].append(['aves3'])
	lista[n].append(['goose', 'hawk', 'hen', 'heron', 'hummingbird', 'kingfisher', 'lark', 'magpie'])
	lista[n].append(['ganso', 'halcón', 'gallina', 'garza', 'colibrí', 'martín pescador', 'alondra', 'hurraca'])

	n = n+1
	lista.append([])
	lista[n].append(['aves 4'])
	lista[n].append(['aves4'])
	lista[n].append(['nest', 'nightingale', 'ostrich', 'owl', 'parakeet', 'parrot', 'partridge', 'peacock'])
	lista[n].append(['nido', 'ruiseñor', 'avestruz', 'búho, lechuza', 'periquito', 'loro, cotorra', 'perdiz', 'pavo real'])

	n = n+1
	lista.append([])
	lista[n].append(['aves 5'])
	lista[n].append(['aves5'])
	lista[n].append(['pelican', 'penguin', 'pheasan', 'pigeon', 'quail', 'roadrunner', 'robin', 'rooster'])
	lista[n].append(['pelícano', 'pinguino', 'faisán', 'paloma', 'codorniz', 'correcaminos', 'petirrojo', 'gallo'])

	n = n+1
	lista.append([])
	lista[n].append(['aves 6'])
	lista[n].append(['aves6'])
	lista[n].append(['sea gull', 'sparrow', 'stork', 'swallow', 'swan', 'thrush', 'turkey', 'vulture', 'woodpecker'])
	lista[n].append(['gaviota', 'gorrión', 'cigüeña', 'golondrina', 'cisne', 'tordo', 'pavo', 'buitre', 'pájaro carpintero'])

	n = n+1
	lista.append([])
	lista[n].append(['insectos y reptiles 1'])
	lista[n].append(['iyr1'])
	lista[n].append(['alligator', 'ant', 'bedbug', 'bee', 'beetle', 'butterfly', 'caterpillar', 'centipede'])
	lista[n].append(['caimán', 'hormiga', 'chinche', 'abeja', 'escarabajo', 'mariposa', 'oruga', 'ciempiés'])

	n = n+1
	lista.append([])
	lista[n].append(['insectos y reptiles 2'])
	lista[n].append(['iyr2'])
	lista[n].append(['chameleon', 'cicada', 'cricket', 'crocodile', 'dragonfly', 'earthworm', 'eel', 'firefly'])
	lista[n].append(['camaleón', 'cigarra', 'grillo', 'cocodrilo', 'libélula', 'lombriz', 'anguila', 'luciérnaga'])

	n = n+1
	lista.append([])
	lista[n].append(['insectos y reptiles 3'])
	lista[n].append(['iyr3'])
	lista[n].append(['flea', 'fly', 'frog', 'grasshopper', 'horsefly', 'iguana', 'ladybird', 'ladybug'])
	lista[n].append(['pulga', 'mosca', 'rana', 'saltamontes', 'tábano', 'iguana', 'mariquita', 'mariquita'])

	n = n+1
	lista.append([])
	lista[n].append(['insectos y reptiles 4'])
	lista[n].append(['iyr4'])
	lista[n].append(['leech', 'lice', 'lizard', 'locust', 'louse', 'mantis', 'mosquito', 'moth'])
	lista[n].append(['sanguijuela', 'piojos', 'lagartija', 'langosta', 'piojo', 'mantis', 'mosquito', 'polilla'])

	n = n+1
	lista.append([])
	lista[n].append(['insectos y reptiles 5'])
	lista[n].append(['iyr5'])
	lista[n].append(['rattlesnake', 'roach', 'salamander', 'scorpion', 'snake', 'spider', 'tarantula', 'termite'])
	lista[n].append(['vívora de cascabel', 'cucaracha', 'salamandra', 'escorpión', 'vívora', 'araña', 'tarántula', 'termita'])

	n = n+1
	lista.append([])
	lista[n].append(['insectos y reptiles 6'])
	lista[n].append(['iyr6'])
	lista[n].append(['tick', 'toad', 'tortoise', 'turtle', 'viper', 'wasp', 'worm, -l-', 'worm, -g-'])
	lista[n].append(['garrapata', 'sapo', 'tortuga de tierra', 'tortuga', 'vívora', 'avispa', 'lombriz', 'gusano'])

	n = n+1
	lista.append([])
	lista[n].append(['mamíferos 1'])
	lista[n].append(['mam1'])
	lista[n].append(['anteater', 'antelope', 'bat', 'bear', 'beaver', 'boar', 'buffalo', 'bull'])
	lista[n].append(['oso hormiguero', 'antílope', 'murciélago', 'oso', 'castor', 'jabalí', 'búfalo', 'toro'])

	n = n+1
	lista.append([])
	lista[n].append(['mamíferos 2'])
	lista[n].append(['mam2'])
	lista[n].append(['calf', 'camel', 'cat', 'cheetah', 'chimpanzee', 'cow', 'deer', 'dog'])
	lista[n].append(['ternero', 'camello', 'gato', 'guepardo', 'chimpancé', 'vaca', 'venado', 'perro'])

	n = n+1
	lista.append([])
	lista[n].append(['mamíferos 3'])
	lista[n].append(['mam3'])
	lista[n].append(['donkey', 'dromedary', 'elephant', 'elk', 'foal', 'fox', 'gazelle', 'giraffe'])
	lista[n].append(['burro', 'dromedario', 'elefante', 'alce', 'potro', 'zorro', 'gacela', 'jirafa'])

	n = n+1
	lista.append([])
	lista[n].append(['mamíferos 4'])
	lista[n].append(['mam4'])
	lista[n].append(['goat', 'gorilla', 'hippopotamus', 'hog', 'horse', 'hyena', 'kangaroo', 'lamb'])
	lista[n].append(['cabra', 'gorila', 'hipopótamo', 'cerdo', 'caballo', 'hiena', 'canguro', 'cordero'])

	n = n+1
	lista.append([])
	lista[n].append(['mamíferos 5'])
	lista[n].append(['mam5'])
	lista[n].append(['leopard', 'lion', 'monkey', 'moose', 'mouse', 'otter', 'ox', 'pig'])
	lista[n].append(['leopardo', 'león', 'mono', 'alce', 'laucha, ratón', 'nutria', 'buey', 'cerdo'])

	n = n+1
	lista.append([])
	lista[n].append(['mamíferos 6'])
	lista[n].append(['mam6'])
	lista[n].append(['porcupine', 'rabbit', 'raccoon', 'rat', 'rhinoceros', 'seal', 'sheep', 'skunk'])
	lista[n].append(['puerco espín', 'conejo', 'mapache', 'rata', 'rinoceronte', 'foca', 'oveja', 'zorrillo'])

	n = n+1
	lista.append([])
	lista[n].append(['mamíferos 7'])
	lista[n].append(['mam7'])
	lista[n].append(['squirrel', 'tiger', 'wolf', 'zebra'])
	lista[n].append(['ardilla', 'tigre', 'lobo', 'cebra'])

	n = n+1
	lista.append([])
	lista[n].append(['animales acuáticos 1'])
	lista[n].append(['aacu1'])
	lista[n].append(['alligator', 'anchovy', 'catfish', 'cod', 'crab', 'crayfish', 'crocodile', 'dolphin'])
	lista[n].append(['caimán', 'anchoa', 'bagre', 'bacalao', 'cangrejo', 'cangrejo de río', 'cocodrilo', 'delfín'])

	n = n+1
	lista.append([])
	lista[n].append(['animales acuáticos 2'])
	lista[n].append(['aacu2'])
	lista[n].append(['eel', 'frog', 'herring', 'jellyfish', 'killerwhale', 'lobster', 'mackerel', 'octopus'])
	lista[n].append(['anguila', 'rana', 'arenque', 'medusa', 'orca', 'langosta', 'caballa', 'pulpo'])

	n = n+1
	lista.append([])
	lista[n].append(['animales acuáticos 3'])
	lista[n].append(['aacu3'])
	lista[n].append(['oyster', 'ray', 'salmon', 'sardine', 'seahorse', 'seal', 'shark', 'shell'])
	lista[n].append(['ostra', 'raya', 'salmón', 'sardina', 'caballito de mar', 'foca', 'tiburón', 'concha'])

	n = n+1
	lista.append([])
	lista[n].append(['animales acuáticos 4'])
	lista[n].append(['aacu4'])
	lista[n].append(['shrimp', 'slug', 'snail', 'sole', 'squid', 'starfish', 'swordfish', 'toad'])
	lista[n].append(['camarón', 'babosa', 'caracol', 'lenguado', 'calamar', 'estrella de mar', 'pez espada', 'sapo'])

	n = n+1
	lista.append([])
	lista[n].append(['animales acuáticos 5'])
	lista[n].append(['aacu5'])
	lista[n].append(['trout', 'tuna', 'turtle', 'walrus', 'whale'])
	lista[n].append(['trucha', 'atún', 'tortuga', 'morsa', 'ballena'])

	n = n+1
	lista.append([])
	lista[n].append(['construcciones y viviendas 1'])
	lista[n].append(['cyv1'])
	lista[n].append(['anphitheater', 'apartment', 'asylum', 'bar', 'barn', 'barracks', 'boarding house', 'brothel'])
	lista[n].append(['anfiteatro', 'apartamento', 'manicomio', 'bar', 'granero, establo', 'cuartel militar', 'casa de pensión', 'burdel'])

	n = n+1
	lista.append([])
	lista[n].append(['construcciones y viviendas 2'])
	lista[n].append(['cyv2'])
	lista[n].append(['bunker', 'cabin', 'casino', 'castle', 'cathedral', 'cave', 'church', 'concert hall'])
	lista[n].append(['búnker', 'cabaña', 'casíno', 'castillo', 'catedral', 'cueva', 'iglesia', 'sala de conciertos'])

	n = n+1
	lista.append([])
	lista[n].append(['construcciones y viviendas 3'])
	lista[n].append(['cyv3'])
	lista[n].append(['condominium', 'cottage', 'dormitory', 'factory', 'farm', 'fort', 'gas station', 'greenhouse'])
	lista[n].append(['condominio', 'casa de campo', 'residencia universitaria', 'fábrica', 'granja', 'fuerte', 'gasolinera', 'invernadero'])

	n = n+1
	lista.append([])
	lista[n].append(['construcciones y viviendas 4'])
	lista[n].append(['cyv4'])
	lista[n].append(['hospital', 'hostel', 'hotel', 'house', 'houseboat', 'hut', 'igloo', 'inn'])
	lista[n].append(['hospital', 'hostal', 'hotel', 'casa', 'casa flotante', 'choza', 'iglú', 'posada'])

	n = n+1
	lista.append([])
	lista[n].append(['construcciones y viviendas 5'])
	lista[n].append(['cyv5'])
	lista[n].append(['library', 'lighthouse', 'mansion', 'mobile home', 'mosque', 'motel', 'museum', 'nightclub'])
	lista[n].append(['biblioteca', 'faro', 'mansión', 'casa rodante', 'mezquita', 'hotel de carretera', 'museo', 'club nocturno, discoteca'])

	n = n+1
	lista.append([])
	lista[n].append(['construcciones y viviendas 6'])
	lista[n].append(['cyv6'])
	lista[n].append(['nursing home', 'palace', 'parliament', 'power plant', 'prison', 'pub', 'pyramid', 'ranch'])
	lista[n].append(['residencia para ancianos', 'palacio', 'parlamento', 'central eléctrica', 'cárcel, prisión', 'pub', 'pirámide', 'rancho, hacienda'])

	n = n+1
	lista.append([])
	lista[n].append(['construcciones y viviendas 7'])
	lista[n].append(['cyv7'])
	lista[n].append(['restaurant', 'shrine', 'skyscraper', 'stadium', 'store', 'synagogue', 'temple', 'tent'])
	lista[n].append(['restaurante', 'santuario', 'rascacielos', 'estadio', 'tienda, almacén', 'sinagoga', 'templo', 'carpa'])

	n = n+1
	lista.append([])
	lista[n].append(['construcciones y viviendas 8'])
	lista[n].append(['cyv8'])
	lista[n].append(['tepee', 'tower', 'warehouse', 'windmill'])
	lista[n].append(['choza de indios', 'torre', 'almacén', 'molino de viento'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 1'])
	lista[n].append(['pdlc1'])
	lista[n].append(['airport', 'art gallery', 'arts center', 'avenue', 'bank', 'bar', 'bicycle', 'boarding house'])
	lista[n].append(['aeropuerto', 'galería de arte', 'centro cultural', 'avenida', 'banco', 'bar', 'bicicleta', 'pensión, casa de huéspedes'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 2'])
	lista[n].append(['pdlc2'])
	lista[n].append(['bookstall', 'botanical garden', 'boulevard', 'bridge', 'building site', 'buildings', 'bus', 'bus station'])
	lista[n].append(['kiosco, puesto de libros', 'jardín botánico', 'bulevar', 'puente', 'obra en construcción', 'edificios', 'autobús', 'estación de autobuses'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 3'])
	lista[n].append(['pdlc3'])
	lista[n].append(['bus stop', 'castle', 'cathedral', 'cemetery', 'church', 'circus', 'city hall', 'clock'])
	lista[n].append(['parada de autobús', 'castillo', 'catedral', 'cementerio', 'iglesia', 'circo', 'ayuntamiento, municipalidad', 'reloj'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 4'])
	lista[n].append(['pdlc4'])
	lista[n].append(['consulate', 'corner', 'crossroads', 'crosswalk', 'cul-de-sac', 'curb', 'department store', 'district'])
	lista[n].append(['consulado', 'esquina', 'cruce', 'cruce peatonal, paso de peatones', 'callejón sin salida', 'bordillo de la acera', 'grandes almacenes', 'barrio, distrito'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 5'])
	lista[n].append(['pdlc5'])
	lista[n].append(['ditch', 'downtown', 'drugstore', 'embassy', 'fire brigade', 'fountain', 'gutter', "hairdresser's"])
	lista[n].append(['zanja', 'centro de la ciudad', 'farmacia', 'embajada', 'cuerpo de bomberos', 'fuente', 'alcantarilla, cuneta', 'peluquería'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 6'])
	lista[n].append(['pdlc6'])
	lista[n].append(['highway', 'hospital', 'hostel', 'hotel', 'house', 'information office', 'inhabitant', 'lane'])
	lista[n].append(['autopista', 'hospital', 'hostal', 'hotel', 'casa', 'oficina de información', 'habitante', 'callejón'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 7'])
	lista[n].append(['pdlc7'])
	lista[n].append(['laundromat', 'lawcourt', 'library', 'litter', 'mail box', 'market', 'monument', 'mosque'])
	lista[n].append(['lavadero automático', 'tribunal', 'biblioteca', 'basura', 'buzón de correos', 'mercado', 'monumento', 'mezquita'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 8'])
	lista[n].append(['pdlc8'])
	lista[n].append(['motorcycle', 'motorists', 'movie theater', 'museum', 'neighborhood', 'neon signs', 'newspaper stand', 'night club'])
	lista[n].append(['motocicleta', 'automovilistas', 'cine', 'museo', 'barrio, distrito', 'letreros luminosos', 'quiosco de periódicos', 'club nocturno'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 9'])
	lista[n].append(['pdlc9'])
	lista[n].append(["old people's home", 'orphanage', 'outskirts', 'palace', 'park', 'parking lot', 'passage', 'passer-by'])
	lista[n].append(['asilo de ancianos', 'orfanato', 'afueras de la ciudad', 'palacio', 'parque', 'aparcamiento', 'pasaje', 'transeúnte'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 10'])
	lista[n].append(['pdlc10'])
	lista[n].append(['pedestrian', 'pedestrian zone', 'phone booth', 'police station', 'port', 'post office', 'prison', 'promenade'])
	lista[n].append(['peatón', 'zona peatonal', 'cabina telefónica', 'comisaría', 'puerto', 'oficina de correos', 'cárcel', 'paseo'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 11'])
	lista[n].append(['pdlc11'])
	lista[n].append(['railroad station', 'restaurant', 'ring road', 'road', 'school', 'sewers', 'shop', 'shop windows'])
	lista[n].append(['estación de ferrocarril', 'restaurante', 'carretera de circunvalación', 'camino, carretera', 'escuela, colegio', 'cloacas', 'tienda', 'escaparates'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 12'])
	lista[n].append(['pdlc12'])
	lista[n].append(['shopping mall', 'sidewalk', 'skyscraper', 'slums', 'square', 'stadium', 'statue', 'stock exchange'])
	lista[n].append(['centro comercial', 'acera', 'rascacielos', 'barrio bajo', 'plaza', 'estadio', 'estatua', 'la bolsa de valores'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 13'])
	lista[n].append(['pdlc13'])
	lista[n].append(['street', 'streetcar', 'streetlamps', 'suburbs', 'subway', 'subway station', 'synagogue', 'taxi cab'])
	lista[n].append(['calle', 'tranvía', 'faroles de calle', 'suburbios, las afueras de la ciudad', 'metro, tren subterráneo', 'estación de metro', 'sinagoga', 'taxi'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 14'])
	lista[n].append(['pdlc14'])
	lista[n].append(['telephones', 'theatre', 'tourist', 'tourist office', 'townspeople', 'traffic', 'traffic light', 'traffic policeman'])
	lista[n].append(['teléfonos', 'teatro', 'turista', 'oficina de turismo', 'habitantes de la ciudad', 'tráfico, circulación', 'semáforo', 'oficial de tránsito, policía de tránsito'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la ciudad 15'])
	lista[n].append(['pdlc15'])
	lista[n].append(['tramp', 'trashcan', 'travel agency', 'trees', 'truck', 'tunnel', 'university', 'zoo'])
	lista[n].append(['vagabundo, mendigo', 'papelera', 'agencia de viajes', 'árboles', 'camión', 'túnel', 'universidad', 'zoológico'])

	n = n+1
	lista.append([])
	lista[n].append(['tiendas y comercios 1'])
	lista[n].append(['tyc1'])
	lista[n].append(['bakery', "barber's", 'bookstore', "butcher's", 'cake shop', 'candy store', "children's wear", 'clothing store'])
	lista[n].append(['panadería', 'barbería', 'librería', 'carnicería', 'pastelería', 'tienda de golosinas', 'ropa de niño', 'tienda de ropas'])

	n = n+1
	lista.append([])
	lista[n].append(['tiendas y comercios 2'])
	lista[n].append(['tyc2'])
	lista[n].append(['coffee shop', "confectioner's", 'dairy store', 'delicatessen', 'drugstore', "dry cleaner's", 'estate agency', "fishmonger's"])
	lista[n].append(['cafetería', 'pastelería', 'lechería', 'fiambrería', 'farmacia', 'tintorería', 'agencia inmobiliaria', 'pescadería'])

	n = n+1
	lista.append([])
	lista[n].append(['tiendas y comercios 3'])
	lista[n].append(['tyc3'])
	lista[n].append(["florist's", 'fruit shop', 'furniture store', 'gas station', "greengrocer's", 'grocery store', "hairdresser's", 'hardware shop'])
	lista[n].append(['floristería', 'frutería', 'mueblería', 'gasolinería', 'verdulería', 'almacén', 'peluquería', 'ferretería'])

	n = n+1
	lista.append([])
	lista[n].append(['tiendas y comercios 4'])
	lista[n].append(['tyc4'])
	lista[n].append(["herbalist's shop", 'ice-cream parlour', "ironmonger's", "jeweller's", 'jewellery store', 'kiosk', "ladies' wear", 'laundromat'])
	lista[n].append(['herboristería', 'heladería', 'ferretería', 'joyería', 'joyería', 'quiosco', 'ropa de señora', 'lavandería automática'])

	n = n+1
	lista.append([])
	lista[n].append(['tiendas y comercios 5'])
	lista[n].append(['tyc5'])
	lista[n].append(['leather goods shop', 'mall', 'market', "men's wear", 'music store', 'newsstand', "optician's", 'perfumery'])
	lista[n].append(['marroquinería', 'centro comercial', 'mercado', 'ropa de caballero', 'tienda de música', 'quiosco de periódicos', 'optica', 'perfumería'])

	n = n+1
	lista.append([])
	lista[n].append(['tiendas y comercios 6'])
	lista[n].append(['tyc6'])
	lista[n].append(['pet shop', 'pharmacy', 'shoe shop', 'shopping center', 'shops', 'souvenir shop', 'sports store', 'stationery store'])
	lista[n].append(['tienda de animales', 'farmacia', 'zapatería', 'centro comercial', 'tiendas', 'tienda de souvenirs', 'tienda de deportes', 'papelería'])

	n = n+1
	lista.append([])
	lista[n].append(['tiendas y comercios 7'])
	lista[n].append(['tyc7'])
	lista[n].append(['stores', 'supermarket', 'toy store', 'travel agency', 'vegetable store', 'video store'])
	lista[n].append(['tiendas', 'supermercado', 'juguetería', 'agencia de viajes', 'verdulería', 'tienda de videos'])

	n = n+1
	lista.append([])
	lista[n].append(['problemas de salud y enfermedades 1'])
	lista[n].append(['pdsye1'])
	lista[n].append(['acne', 'Aids', 'allergy', 'anemia', 'appendicitis', 'asthma', 'backache', 'bleeding'])
	lista[n].append(['acné', 'sida', 'alergia', 'anemia', 'apendicitis', 'asma', 'dolor de espalda', 'pérdida de sangre'])

	n = n+1
	lista.append([])
	lista[n].append(['problemas de salud y enfermedades 2'])
	lista[n].append(['pdsye2'])
	lista[n].append(['blister', 'broken leg', 'bruise', 'bump', 'burn', 'cancer', 'chickenpox', 'cold'])
	lista[n].append(['ampolla', 'pierna rota', 'moretón', 'chichón', 'quemadura', 'cáncer', 'varicela', 'resfrío'])

	n = n+1
	lista.append([])
	lista[n].append(['problemas de salud y enfermedades 3'])
	lista[n].append(['pdsye3'])
	lista[n].append(['concussion', 'constipation', 'corn', 'cough', 'cut', 'depression', 'diarrhea', 'disease'])
	lista[n].append(['conmoción cerebral', 'estreñimiento', 'callo', 'tos', 'corte', 'depresión', 'diarrea', 'enfermedad'])

	n = n+1
	lista.append([])
	lista[n].append(['problemas de salud y enfermedades 4'])
	lista[n].append(['pdsye4'])
	lista[n].append(['dry skin', 'earache', 'epidemic', 'fever', 'fracture', 'headache', 'heart attack', 'hemorrhage'])
	lista[n].append(['piel reseca', 'dolor de oído', 'epidemia', 'fiebre', 'fractura', 'dolor de cabeza', 'ataque cardíaco', 'hemorragia'])

	n = n+1
	lista.append([])
	lista[n].append(['problemas de salud y enfermedades 5'])
	lista[n].append(['pdsye5'])
	lista[n].append(['hiccups', 'illness', 'infection', 'inflammation', 'injury', 'insect bite', 'insomnia', 'itch'])
	lista[n].append(['hipo', 'enfermedad', 'infección, contagio', 'inflamación', 'herida', 'picadura de insecto', 'insomnio', 'picazón'])

	n = n+1
	lista.append([])
	lista[n].append(['problemas de salud y enfermedades 6'])
	lista[n].append(['pdsye6'])
	lista[n].append(['jaundice', 'leprosy', 'leukemia', 'measles', 'miscarriage', 'mumps', 'rabies', 'rash'])
	lista[n].append(['ictericia', 'lepra', 'leucemia', 'sarampión', 'aborto espontáneo', 'paperas', 'rabia', 'sarpullido'])

	n = n+1
	lista.append([])
	lista[n].append(['problemas de salud y enfermedades 7'])
	lista[n].append(['pdsye7'])
	lista[n].append(['scar', 'scratch', 'smallpox', 'sore throat', 'sprain', 'stomachache', 'stress', 'stroke'])
	lista[n].append(['cicatriz', 'rasguño', 'viruela', 'garganta inflamada', 'torcedura', 'dolor de estómago', 'estrés', 'ataque, apoplejía'])

	n = n+1
	lista.append([])
	lista[n].append(['problemas de salud y enfermedades 8'])
	lista[n].append(['pdsye8'])
	lista[n].append(['sunburn', 'sunstroke', 'swelling', 'the flu', 'toothache', 'ulcer', 'vomit', 'wound'])
	lista[n].append(['quemadura de sol', 'insolación', 'hinchazón', 'gripe', 'dolor de dientes', 'úlcera', 'vómito', 'herida'])

	n = n+1
	lista.append([])
	lista[n].append(['medicinas y remedios 1'])
	lista[n].append(['myr1'])
	lista[n].append(['alcohol', 'analgesic', 'antacid tablets', 'anti-inflammatory', 'anti-itch cream', 'antibiotic', 'antiseptic', 'Band-Aid'])
	lista[n].append(['alcohol', 'analgésico', 'pastillas antiácidas', 'antiinflamatorio', 'crema contra la picazón', 'antibiótico', 'antiséptico', 'Curita'])

	n = n+1
	lista.append([])
	lista[n].append(['medicinas y remedios 2'])
	lista[n].append(['myr2'])
	lista[n].append(['bandage', 'barbiturate', 'bottle of aspirin', 'calcium', 'cold tablets', 'compound', 'cotton wool', 'cough drops'])
	lista[n].append(['venda', 'barbitúrico', 'frasco de aspirinas', 'calcio', 'comprimidos para el resfrío', 'compuesto', 'algodón', 'comprimidos para la tos'])

	n = n+1
	lista.append([])
	lista[n].append(['medicinas y remedios 3'])
	lista[n].append(['myr3'])
	lista[n].append(['disinfectant', 'dose', 'drugstore', 'eye drops', 'first-aid box', 'gauze', 'hormone', 'injection'])
	lista[n].append(['desinfectante', 'dósis', 'farmacia', 'gotas para los ojos', 'botiquín de primeros auxilios', 'gasa', 'hormona', 'inyección'])

	n = n+1
	lista.append([])
	lista[n].append(['medicinas y remedios 4'])
	lista[n].append(['myr4'])
	lista[n].append(['insulin', 'iodine', 'lab', 'laxative', 'medicine', 'needle', 'ointment', 'painkiller'])
	lista[n].append(['insulina', 'yodo', 'laboratorio', 'laxante', 'medicamento', 'aguja', 'pomada', 'calmante para el dolor'])

	n = n+1
	lista.append([])
	lista[n].append(['medicinas y remedios 5'])
	lista[n].append(['myr5'])
	lista[n].append(['peroxide', 'prescription', 'remedy', 'sedative', 'skin cream', 'sleeping pills', 'sunburn cream', 'suppository'])
	lista[n].append(['agua oxigenada', 'receta', 'remedio', 'sedante, calmante', 'crema para la piel', 'pastillas para dormir', 'crema para quemaduras de sol', 'supositorio'])

	n = n+1
	lista.append([])
	lista[n].append(['medicinas y remedios 6'])
	lista[n].append(['myr6'])
	lista[n].append(['syringe', 'syrup', 'thermometer', 'throat spray', 'tissues', 'toothbrush', 'tube of ointment', 'vitamin C'])
	lista[n].append(['jeringa', 'jarabe', 'termómetro', 'spray para la garganta', 'pañuelos de papel', 'cepillo de dientes', 'tubo de pomada', 'vitamina C'])

	n = n+1
	lista.append([])
	lista[n].append(['el hospital 1'])
	lista[n].append(['eh1'])
	lista[n].append(['ambulance', 'anaesthesia', 'appointments book', 'blood pressure', 'blood test', 'breathing apparatus', 'capsule', 'car accident'])
	lista[n].append(['ambulancia', 'anestesia', 'libro de citas', 'presión sanguínea', 'prueba de sangre', 'respirador artificial', 'cápsula', 'accidente de carro'])

	n = n+1
	lista.append([])
	lista[n].append(['el hospital 2'])
	lista[n].append(['eh2'])
	lista[n].append(['check-up', 'doctor', 'dressing gown', 'emergency room', 'examination couch', 'first aid', 'gauze', 'health insurance'])
	lista[n].append(['chequeo médico', 'doctor', 'bata', 'sala de emergencias', 'diván de reconocimiento', 'primeros auxilios', 'gasa', 'seguro médico'])

	n = n+1
	lista.append([])
	lista[n].append(['el hospital 3'])
	lista[n].append(['eh3'])
	lista[n].append(['injection', 'intensive care unit', 'laboratory', 'mask', 'medical record', 'medicine cabinet', 'microscope', 'nurse'])
	lista[n].append(['inyección', 'unidad de cuidados intensivos', 'laboratorio', 'mascarilla', 'historia clínica', 'armario de remedios', 'microscopio', 'enfermera'])

	n = n+1
	lista.append([])
	lista[n].append(['el hospital 4'])
	lista[n].append(['eh4'])
	lista[n].append(['operating table', 'operation', 'oxygen', 'painkiller', 'paramedics', 'patient', 'physician', 'plaster'])
	lista[n].append(['mesa de operaciones', 'operación', 'oxigeno', 'calmante para el dolor', 'paramédicos', 'paciente', 'médico clínico', 'yeso'])

	n = n+1
	lista.append([])
	lista[n].append(['el hospital 5'])
	lista[n].append(['eh5'])
	lista[n].append(['prescription', 'pyjamas', 'sleeping pills', 'slippers', 'stitches', 'stretcher', 'surgeon', 'surgical instruments'])
	lista[n].append(['receta', 'piyama', 'pastillas para dormir', 'pantuflas', 'puntos de sutura', 'camilla', 'cirujano', 'instrumentos quirúrgicos'])

	n = n+1
	lista.append([])
	lista[n].append(['el hospital 6'])
	lista[n].append(['eh6'])
	lista[n].append(['syringes', 'therapy', 'treatment', 'waiting room', 'wheelchair', 'x-ray plate'])
	lista[n].append(['jeringas', 'terapia', 'tratamiento', 'sala de espera', 'silla de ruedas', 'radiografía'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuerpo humano 1'])
	lista[n].append(['ech1'])
	lista[n].append(['abdomen', 'ankle', 'appendix', 'arm', 'armpit', 'artery', 'back', 'beard'])
	lista[n].append(['vientre', 'tobillo', 'apéndice', 'brazo', 'axila', 'arteria', 'espalda', 'barba'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuerpo humano 2'])
	lista[n].append(['ech2'])
	lista[n].append(['belly', 'bladder', 'blood', 'bones', 'bottom', 'bowels', 'brain', 'breasts'])
	lista[n].append(['panza', 'vejiga', 'sangre', 'huesos', 'trasero', 'entrañas', 'cerebro', 'mamas'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuerpo humano 3'])
	lista[n].append(['ech3'])
	lista[n].append(['bust', 'buttocks', 'calf', 'cheekbones', 'cheeks', 'chest', 'chin', 'ears'])
	lista[n].append(['busto', 'nalgas', 'pantorrilla', 'pómulos', 'mejillas', 'pecho', 'mentón', 'orejas'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuerpo humano 4'])
	lista[n].append(['ech4'])
	lista[n].append(['elbow', 'eyebrows', 'eyelashes', 'eyelids', 'eyes', 'face', 'feet', 'fingers'])
	lista[n].append(['codo', 'cejas', 'pestañas', 'párpados', 'ojos', 'cara, rostro', 'pies', 'dedos'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuerpo humano 5'])
	lista[n].append(['ech5'])
	lista[n].append(['fist', 'flesh', 'foot', 'forearm', 'forehead', 'genitals', 'hair', 'hand'])
	lista[n].append(['puño', 'carne', 'pie', 'antebrazo', 'frente', 'genitales', 'cabello', 'mano'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuerpo humano 6'])
	lista[n].append(['ech6'])
	lista[n].append(['head', 'heart', 'heel', 'hips', 'instep', 'intestines', 'jaw', 'kidneys'])
	lista[n].append(['cabeza', 'corazón', 'talón', 'caderas', 'empeine', 'intestinos', 'mandíbula', 'riñones'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuerpo humano 7'])
	lista[n].append(['ech7'])
	lista[n].append(['knee', 'knuckles', 'leg', 'limbs', 'lips', 'liver', 'lungs', 'moustache'])
	lista[n].append(['rodilla', 'nudillos', 'pierna', 'extremidades', 'labios', 'hígado', 'pulmones', 'bigote'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuerpo humano 8'])
	lista[n].append(['ech8'])
	lista[n].append(['mouth', 'muscles', 'nails', 'nape', 'navel', 'neck', 'nipples', 'organs'])
	lista[n].append(['boca', 'músculos', 'uñas', 'nuca', 'ombligo', 'cuello', 'pezones, tetillas', 'órganos'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuerpo humano 9'])
	lista[n].append(['ech9'])
	lista[n].append(['palm', 'pancreas', 'pelvis', 'penis', 'rib', 'shin', 'shoulder', 'sideburns'])
	lista[n].append(['palma', 'páncreas', 'pélvis', 'pene', 'costilla', 'espinilla, canilla', 'hombro', 'patillas'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuerpo humano 10'])
	lista[n].append(['ech10'])
	lista[n].append(['skeleton', 'skin', 'skull', 'sole', 'spine', 'stomach', 'teeth', 'temples'])
	lista[n].append(['esqueleto', 'piel', 'cráneo', 'planta', 'columna vertebral', 'estómago', 'dientes', 'sienes'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuerpo humano 11'])
	lista[n].append(['ech11'])
	lista[n].append(['thigh', 'thorax', 'throat', 'toes', 'tongue', 'tooth', 'torso', 'trunk'])
	lista[n].append(['muslo', 'tórax', 'garganta', 'dedos (del pie)', 'lengua', 'diente', 'torso', 'tronco'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuerpo humano 12'])
	lista[n].append(['ech12'])
	lista[n].append(['vagina', 'vein', 'waist', 'wrinkles', 'wrist'])
	lista[n].append(['vagina', 'vena', 'cintura', 'arrugas', 'muñeca'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la casa 1'])
	lista[n].append(['pdlc1'])
	lista[n].append(['antenna', 'attic', 'back yard', 'balcony', 'basement', 'bathroom', 'bedroom', 'ceiling'])
	lista[n].append(['antena', 'desván', 'patio trasero', 'balcón', 'sótano', 'baño', 'dormitorio', 'cielorraso'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la casa 2'])
	lista[n].append(['pdlc2'])
	lista[n].append(['cellar', 'chimney', 'deck', 'dining room', 'door', 'door handle', 'doorbell', 'driveway'])
	lista[n].append(['sótano, bodega', 'chimenea', 'balcón terraza', 'comedor', 'puerta', 'picaporte', 'timbre', 'entrada par el auto'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la casa 3'])
	lista[n].append(['pdlc3'])
	lista[n].append(['fence', 'fence gate', 'floor', 'front yard', 'garage', 'garden', 'garden shed', 'ground floor'])
	lista[n].append(['cerca', 'puerta de la cerca', 'piso', 'patio frontal', 'garage', 'jardín', 'cobertizo', 'planta baja'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la casa 4'])
	lista[n].append(['pdlc4'])
	lista[n].append(['hall', 'hallway', 'hedge', 'key', 'kitchen', 'laundry room', 'lawn', 'living room'])
	lista[n].append(['vestíbulo', 'pasillo', 'seto', 'llave', 'cocina', 'lavadero', 'césped', 'sala'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la casa 5'])
	lista[n].append(['pdlc5'])
	lista[n].append(['lock', 'mailbox', 'pantry', 'patio', 'peephole', 'pool', 'porch', 'roof'])
	lista[n].append(['cerradura', 'buzón', 'despensa', 'patio', 'mirilla de la puerta', 'piscina', 'pórtico', 'techo'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la casa 6'])
	lista[n].append(['pdlc6'])
	lista[n].append(['room', 'skylight', 'staircase', 'steps', 'study', 'utility room', 'veranda', 'wall'])
	lista[n].append(['habitación', 'tragaluz, claraboya', 'escalera', 'escalones', 'despacho, estudio', 'cuarto de servicio', 'galería, veranda', 'pared'])

	n = n+1
	lista.append([])
	lista[n].append(['partes de la casa 7'])
	lista[n].append(['pdlc7'])
	lista[n].append(['window'])
	lista[n].append(['ventana'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuarto del bebé 1'])
	lista[n].append(['ecdb1'])
	lista[n].append(['bib', 'blocks', 'bottle', 'cradle', 'crib', 'diaper', 'doll', 'doll house'])
	lista[n].append(['babero', 'bloques, cubos', 'biberón', 'cuna mecedora', 'cuna', 'pañal', 'muñeca', 'casa de muñecas'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuarto del bebé 2'])
	lista[n].append(['ecdb2'])
	lista[n].append(['nipple', 'pacifier', 'playpen', 'potty', 'puzzle', 'rattle', 'stroller', 'swing'])
	lista[n].append(['tetilla', 'chupete', 'corral de juego', 'orinal, escupidera', 'rompecabezas', 'sonajero', 'cochecito de bebé', 'columpio, hamaca'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuarto del bebé 3'])
	lista[n].append(['ecdb3'])
	lista[n].append(['teddy bear', 'toy', 'toy chest', 'walker'])
	lista[n].append(['osito de peluche', 'juguete', 'arcón de juguetes', 'andador'])

	n = n+1
	lista.append([])
	lista[n].append(['el baño 1'])
	lista[n].append(['eb1'])
	lista[n].append(['basket', 'bath mat', 'bath salts', 'bathtub', 'bidet', 'brush', 'bubble', 'cold water'])
	lista[n].append(['canasto', 'alfombra de baño', 'sales de baño', 'bañera, tina', 'bidé', 'cepillo', 'burbuja', 'agua fría'])

	n = n+1
	lista.append([])
	lista[n].append(['el baño 2'])
	lista[n].append(['eb2'])
	lista[n].append(['comb', 'curtain', 'deodorant', 'drain', 'electric razor', 'faucet', 'floss', 'foam'])
	lista[n].append(['peine', 'cortina', 'desodorante', 'desague', 'afeitadora eléctrica', 'canilla, grifo', 'hilo dental', 'espuma'])

	n = n+1
	lista.append([])
	lista[n].append(['el baño 3'])
	lista[n].append(['eb3'])
	lista[n].append(['hair dryer', 'hair gel', 'hairbrush', 'hand towel', 'hot water', 'lipstick', 'lotion', 'medicine chest'])
	lista[n].append(['secador de pelo', 'gomina, gel', 'cepillo de pelo', 'toallita de mano', 'agua caliente', 'lápiz de labios', 'loción', 'botiquín'])

	n = n+1
	lista.append([])
	lista[n].append(['el baño 4'])
	lista[n].append(['eb4'])
	lista[n].append(['nail clippers', 'nail polish', 'nailbrush', 'perfume', 'razor', 'razor blade', 'scale', 'shampoo'])
	lista[n].append(['cortaúñas', 'esmalte de uñas', 'cepillo de uñas', 'perfume', 'afeitadora, rasuradora', 'hoja de afeitar', 'balanza, báscula', 'champú'])

	n = n+1
	lista.append([])
	lista[n].append(['el baño 5'])
	lista[n].append(['eb5'])
	lista[n].append(['shaving cream', 'shelf', 'shower', 'sink', 'soap', 'soap dish', 'sponge', 'stopper'])
	lista[n].append(['crema de afeitar', 'repisa', 'ducha', 'pileta, lavabo', 'jabón', 'jabonera', 'esponja', 'tapón'])

	n = n+1
	lista.append([])
	lista[n].append(['el baño 6'])
	lista[n].append(['eb6'])
	lista[n].append(['tile', 'toilet', 'toilet paper', 'toothbrush', 'toothpaste', 'towel', 'towel rack', 'tweezers'])
	lista[n].append(['azulejo', 'inodoro, retrete', 'papel higiénico', 'cepillo de dientes', 'pasta dentífrica', 'toalla', 'toallero', 'pinzas depiladoras'])

	n = n+1
	lista.append([])
	lista[n].append(['el baño 7'])
	lista[n].append(['eb7'])
	lista[n].append(['washcloth'])
	lista[n].append(['toallita de ducha'])

	n = n+1
	lista.append([])
	lista[n].append(['el dormitorio 1'])
	lista[n].append(['ed1'])
	lista[n].append(['air conditioner', 'alarm clock', 'bed', 'bedding', 'bedspread', 'blanket', 'blinds', 'bunk bed'])
	lista[n].append(['aire acondicionado', 'reloj despertador', 'cama', 'ropa de cama', 'colcha, cubrecama', 'cobija, frazada', 'persianas', 'litera, cucheta'])

	n = n+1
	lista.append([])
	lista[n].append(['el dormitorio 2'])
	lista[n].append(['ed2'])
	lista[n].append(['chest of drawers', 'closet', 'comforter', 'curtain', 'double bed', 'dresser', 'footboard', 'hanger'])
	lista[n].append(['cómoda', 'placárd', 'cobertor acolchado', 'cortina', 'cama matrimonial', 'tocador', 'pie de la cama', 'percha'])

	n = n+1
	lista.append([])
	lista[n].append(['el dormitorio 3'])
	lista[n].append(['ed3'])
	lista[n].append(['headboard', 'lamp', 'mattres', 'mirror', 'night table', 'phone', 'pillow', 'pillowcase'])
	lista[n].append(['cabecera de la cama', 'lámpara', 'colchón', 'espejo', 'mesita de noche', 'teléfono', 'almohada', 'funda de almohada'])

	n = n+1
	lista.append([])
	lista[n].append(['el dormitorio 4'])
	lista[n].append(['ed4'])
	lista[n].append(['plug', 'rug', 'sheets', 'single bed', 'socket', 'switch', 'trunk', 'wardrobe'])
	lista[n].append(['enchufe', 'alfombra', 'sábanas', 'cama individual', 'tomacorriente', 'interruptor de luz', 'baúl', 'armario, ropero'])

	n = n+1
	lista.append([])
	lista[n].append(['el comedor 1'])
	lista[n].append(['ec1'])
	lista[n].append(['beer', 'bottle', 'bottle opener', 'bread', 'candle', 'candlestick', 'chair', 'champagne'])
	lista[n].append(['cerveza', 'botella', 'destapador', 'pan', 'vela', 'candelabro', 'silla', 'champaña'])

	n = n+1
	lista.append([])
	lista[n].append(['el comedor 2'])
	lista[n].append(['ec2'])
	lista[n].append(['chandelier', 'china', 'coffeepot', 'corkscrew', 'cup', 'dessert spoon', 'dish', 'fork'])
	lista[n].append(['araña de techo', 'vajilla de porcelana', 'cafetera', 'sacacorchos, tirabuzón', 'taza', 'cuchara de postre', 'plato, comida', 'tenedor'])

	n = n+1
	lista.append([])
	lista[n].append(['el comedor 3'])
	lista[n].append(['ec3'])
	lista[n].append(['glass', 'jug', 'knife', 'ladle', 'mineral water', 'mug', 'mustard', 'napkin'])
	lista[n].append(['vaso', 'jarro', 'cuchillo', 'cucharón', 'agua mineral', 'taza grande, jarra', 'mostaza', 'servilleta'])

	n = n+1
	lista.append([])
	lista[n].append(['el comedor 4'])
	lista[n].append(['ec4'])
	lista[n].append(['oil', 'pepper', 'pepper shaker', 'pitcher', 'plate', 'regular water', 'rolls', 'salad bowl'])
	lista[n].append(['aceite', 'pimienta', 'pimentero', 'jarra para servir', 'plato -recipiente-', 'agua mineral sin gas', 'panecillos', 'ensaladera'])

	n = n+1
	lista.append([])
	lista[n].append(['el comedor 5'])
	lista[n].append(['ec5'])
	lista[n].append(['salt', 'salt shaker', 'saucer', 'silverware', 'sparkling water', 'spoon', 'sugar bowl', 'table'])
	lista[n].append(['sal', 'salero', 'platillo', 'juego de cubiertos', 'agua con gas', 'cuchara', 'azucarera', 'mesa'])

	n = n+1
	lista.append([])
	lista[n].append(['el comedor 6'])
	lista[n].append(['ec6'])
	lista[n].append(['tablecloth', 'teapot', 'teaspoon', 'toothpicks', 'tray', 'vinegar', 'water', 'water glass'])
	lista[n].append(['mantel', 'tetera', 'cucharita', 'mondadientes', 'bandeja', 'vinagre', 'agua', 'copa de agua'])

	n = n+1
	lista.append([])
	lista[n].append(['el comedor 7'])
	lista[n].append(['ec7'])
	lista[n].append(['wine', 'wine glass'])
	lista[n].append(['vino', 'copa de vino'])

	n = n+1
	lista.append([])
	lista[n].append(['el jardín 1'])
	lista[n].append(['ej1'])
	lista[n].append(['barbecue grill', 'bucket', 'bush', 'chain saw', 'charcoal', 'deck chair', 'fence', 'flower bed'])
	lista[n].append(['parrilla para barbacoa', 'cubo, balde', 'arbusto', 'motosierra', 'carbón', 'tumbona, reposera', 'cerca', 'arriate, parterre'])

	n = n+1
	lista.append([])
	lista[n].append(['el jardín 2'])
	lista[n].append(['ej2'])
	lista[n].append(['flowers', 'fork', 'fountain', 'gate', 'grass', 'greenhouse', 'grill', 'hammock'])
	lista[n].append(['flores', 'horquilla', 'fuente', 'verja', 'pasto', 'invernadero', 'parrilla', 'hamaca'])

	n = n+1
	lista.append([])
	lista[n].append(['el jardín 3'])
	lista[n].append(['ej3'])
	lista[n].append(['hedge', 'hoe', 'hose', 'ladder', 'lawn', 'lawnmower', 'path', 'pond'])
	lista[n].append(['seto', 'azadón', 'manguera', 'escalera de mano', 'césped', 'cortadora de césped', 'sendero, caminito', 'estanque'])

	n = n+1
	lista.append([])
	lista[n].append(['el jardín 4'])
	lista[n].append(['ej4'])
	lista[n].append(['pruning shears', 'rake', 'rose bush', 'shed', 'shovel', 'shrub', 'sickle', 'spade'])
	lista[n].append(['tijeras podaderas', 'rastrillo', 'rosal', 'cobertizo', 'pala', 'arbusto', 'hoz', 'pala'])

	n = n+1
	lista.append([])
	lista[n].append(['el jardín 5'])
	lista[n].append(['ej5'])
	lista[n].append(['sprinkler', 'sunbed', 'sunshade', 'swimming pool', 'trowel', 'watering can', 'weeds', 'wheelbarrow'])
	lista[n].append(['regador automático', 'tumbona, reposera', 'sombrilla', 'piscina', 'desplantador', 'regadera', 'malas hierbas', 'carretilla'])

	n = n+1
	lista.append([])
	lista[n].append(['la cocina 1'])
	lista[n].append(['lc1'])
	lista[n].append(['blender', 'bottle opener', 'bowl', 'broom', 'cake mold', 'can opener', 'canister', 'carving knife'])
	lista[n].append(['licuadora', 'destapador de botellas', 'bol, taza grande', 'escoba', 'molde para repostería', 'abrelatas', 'bote, lata', 'cuchillo para trinchar'])

	n = n+1
	lista.append([])
	lista[n].append(['la cocina 2'])
	lista[n].append(['lc2'])
	lista[n].append(['casserole', 'ceramic ware', 'cheese cutter', 'chopping board', 'cleaver', 'coffee maker', 'colander', 'corkscrew'])
	lista[n].append(['cazuelera', 'vajilla de cerámica', 'cortador de queso', 'tabla para cortar', 'cuchilla para picar', 'cafetera', 'colador de verduras', 'destapador'])

	n = n+1
	lista.append([])
	lista[n].append(['la cocina 3'])
	lista[n].append(['lc3'])
	lista[n].append(['counter', 'crokery', 'cup', 'cupboard', 'cutlery', 'dish drainer', 'dish towel', 'dishwasher'])
	lista[n].append(['mesada', 'loza, vajilla', 'taza', 'alacena', 'cubiertos', 'escurridor de platos', 'repasador', 'lavaplatos'])

	n = n+1
	lista.append([])
	lista[n].append(['la cocina 4'])
	lista[n].append(['lc4'])
	lista[n].append(['drawers', 'faucet', 'food processor', 'forks', 'freezer', 'fridge', 'frying pan', 'funnel'])
	lista[n].append(['cajones', 'canilla, grifo', 'procesadora de alimentos', 'tenedores', 'congelador', 'heladera', 'sartén', 'embudo'])

	n = n+1
	lista.append([])
	lista[n].append(['la cocina 5'])
	lista[n].append(['lc5'])
	lista[n].append(['garbage', 'gloves', 'grater', 'ice tray', 'juicer', 'kettle', 'kitchen apron', 'knives'])
	lista[n].append(['basura', 'guantes', 'rallador', 'cubetera', 'juguera', 'pava', 'delantal de cocina', 'cuchillos'])

	n = n+1
	lista.append([])
	lista[n].append(['la cocina 6'])
	lista[n].append(['lc6'])
	lista[n].append(['ladle', 'lighter', 'masher', 'microwave oven', 'mincer', 'mixer', 'oven', 'oven burner'])
	lista[n].append(['cucharón', 'encendedor', 'pisapuré', 'horno microondas', 'picador, picadora', 'batidora', 'horno', 'quemador del horno'])

	n = n+1
	lista.append([])
	lista[n].append(['la cocina 7'])
	lista[n].append(['lc7'])
	lista[n].append(['oven mitts', 'pans', 'pepper mill', 'pot', 'pot holder', 'potato peeler', 'pressure cooker', 'recipe'])
	lista[n].append(['guantes para horno', 'ollas, caserolas y sartenes', 'molinillo de pimienta', 'olla', 'agarradera', 'pelapapas', 'olla a presión', 'receta'])

	n = n+1
	lista.append([])
	lista[n].append(['la cocina 8'])
	lista[n].append(['lc8'])
	lista[n].append(['refrigerator', 'roasting pan', 'rolling pin', 'salt shaker', 'saucepan', 'scouring pad', 'sharpener', 'shelves'])
	lista[n].append(['heladera', 'asadera', 'palo de amasar', 'salero', 'cacerola', 'esponja limpiadora', 'afilador de cuchillos', 'anaqueles, estantes'])

	n = n+1
	lista.append([])
	lista[n].append(['la cocina 9'])
	lista[n].append(['lc9'])
	lista[n].append(['sieve', 'sink', 'soap', 'spatula', 'spoons', 'squeezer', 'steamer', 'stove'])
	lista[n].append(['tamiz', 'pileta de lavar', 'jabón', 'espátula', 'cucharas', 'exprimidor', 'vaporera', 'cocina (aparato)'])

	n = n+1
	lista.append([])
	lista[n].append(['la cocina 10'])
	lista[n].append(['lc10'])
	lista[n].append(['stove burners', 'strainer', 'teapot', 'teaspoons', 'toaster', 'trash can', 'washing', 'water heater'])
	lista[n].append(['quemadores de cocina', 'colador chico', 'tetera', 'cucharitas', 'tostadora', 'tacho de la basura', 'up liquid  - detergente', 'calefón'])

	n = n+1
	lista.append([])
	lista[n].append(['la cocina 11'])
	lista[n].append(['lc11'])
	lista[n].append(['whisk', 'wok'])
	lista[n].append(['batidor de alambre', 'sartén china'])

	n = n+1
	lista.append([])
	lista[n].append(['la sala 1'])
	lista[n].append(['ls1'])
	lista[n].append(['armchair', 'ashtray', 'bookcase', 'carpet', 'ceiling fan', 'chandelier', 'clock', 'coffee table'])
	lista[n].append(['sillón', 'cenicero', 'biblioteca', 'alfombra fija', 'ventilador de techo', 'araña', 'reloj de pared', 'mesita central'])

	n = n+1
	lista.append([])
	lista[n].append(['la sala 2'])
	lista[n].append(['ls2'])
	lista[n].append(['couch', 'curtain', 'cushion', 'drapes', 'fireplace', 'firewood', 'furniture', 'heating'])
	lista[n].append(['sofá', 'cortina', 'almohadón, cojín', 'cortinados', 'hogar, chimenea', 'leña', 'muebles', 'calefacción'])

	n = n+1
	lista.append([])
	lista[n].append(['la sala 3'])
	lista[n].append(['ls3'])
	lista[n].append(['lamp', 'light', 'light bulb', 'painting', 'picture', 'plant', 'radiator', 'recliner'])
	lista[n].append(['lámpara', 'luz', 'bombilla, foco', 'pintura, cuadro', 'cuadro', 'planta', 'radiador', 'sillón reclinador'])

	n = n+1
	lista.append([])
	lista[n].append(['la sala 4'])
	lista[n].append(['ls4'])
	lista[n].append(['rocking chair', 'rug', 'sideboard', 'sofa', 'staircase', 'stereo', 'switch', 'telephone'])
	lista[n].append(['mecedora', 'alfombra', 'aparador', 'sofá', 'escalera', 'estéreo', 'interruptor', 'teléfono'])

	n = n+1
	lista.append([])
	lista[n].append(['la sala 5'])
	lista[n].append(['ls5'])
	lista[n].append(['television', 'vase', 'video'])
	lista[n].append(['televisor', 'florero', 'video'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuarto de servicio 1'])
	lista[n].append(['ecds1'])
	lista[n].append(['bleach', 'broom', 'brush', 'bucket', 'clean laundry', 'cleanser', 'clothes line', 'clothes pins'])
	lista[n].append(['blanqueador', 'escoba', 'cepillo', 'balde, cubo', 'ropa limpia', 'producto de limpieza', 'tendedoro', 'broches para ropa'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuarto de servicio 2'])
	lista[n].append(['ecds2'])
	lista[n].append(['dryer', 'dustpan', 'electric bulbs', 'fabric softener', 'feather duster', 'garbage', 'hanger', 'insecticide'])
	lista[n].append(['secadora', 'palita recogedora', 'lamparitas, focos', 'suavizante para la ropa', 'plumero', 'basura', 'percha', 'insecticida'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuarto de servicio 3'])
	lista[n].append(['ecds3'])
	lista[n].append(['iron', 'ironing board', 'laundry', 'laundry basket', 'laundry detergent', 'mop', 'mousetrap', 'plunger'])
	lista[n].append(['plancha', 'tabla de planchar', 'ropa para lavar', 'canasto de ropa', 'detergente para la ropa', 'fregasuelos, fregona', 'trampa ratonera', 'sopapa, desatascador'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuarto de servicio 4'])
	lista[n].append(['ecds4'])
	lista[n].append(['rag', 'rubber gloves', 'sewing machine', 'shelf', 'soap', 'sponge', 'stain remover', 'trash'])
	lista[n].append(['trapo', 'guantes de goma', 'máquina de coser', 'estante', 'jabón', 'esponja', 'quitamanchas', 'basura'])

	n = n+1
	lista.append([])
	lista[n].append(['el cuarto de servicio 5'])
	lista[n].append(['ecds5'])
	lista[n].append(['trash bag', 'trash can', 'vacuum cleaner', 'washing machine', 'wastebasket'])
	lista[n].append(['bolsa de la basura', 'bote de basura', 'aspiradora', 'lavarropas, lavadora', 'cesto de basura'])

	n = n+1
	lista.append([])
	lista[n].append(['taller y herramientas 1'])
	lista[n].append(['tyh1'])
	lista[n].append(['adhesive tape', 'anvil', 'awl', 'bolt', 'brace', 'chain saw', 'chisel', 'drill bit'])
	lista[n].append(['cinta adhesiva', 'yunque', 'punzón', 'bulón', 'taladro de mano', 'motosierra', 'cincel, formón', 'mecha del taladro'])

	n = n+1
	lista.append([])
	lista[n].append(['taller y herramientas 2'])
	lista[n].append(['tyh2'])
	lista[n].append(['electric drill', 'extension cord', 'file', 'folding ruler', 'gadget', 'glue', 'hammer', 'mallet'])
	lista[n].append(['taladro eléctrico', 'cable prolongador', 'lima', 'metro plegable', 'aparato', 'pegamento', 'martillo', 'mazo'])

	n = n+1
	lista.append([])
	lista[n].append(['taller y herramientas 3'])
	lista[n].append(['tyh3'])
	lista[n].append(['masking tape', 'monkey wrench', 'nail', 'nail puller', 'nut', 'paint', 'paint brush', 'peg'])
	lista[n].append(['cinta protectora', 'llave inglesa ajustable', 'clavo', 'sacaclavos', 'tuerca', 'pintura', 'brocha', 'clavija'])

	n = n+1
	lista.append([])
	lista[n].append(['taller y herramientas 4'])
	lista[n].append(['tyh4'])
	lista[n].append(['plane', 'pliers', 'rag', 'rake', 'ruler', 'sandpaper', 'saw', 'scissors'])
	lista[n].append(['cepillo', 'tenazas, pinzas', 'trapo', 'rastrillo', 'regla', 'papel de lijar', 'serrucho', 'tijeras'])

	n = n+1
	lista.append([])
	lista[n].append(['taller y herramientas 5'])
	lista[n].append(['tyh5'])
	lista[n].append(['scraper', 'screw', 'screwdriver', 'shears', 'shovel', 'solder', 'square', 'tack'])
	lista[n].append(['raspador', 'tornillo', 'destornillador', 'tijeras de podar', 'pala', 'soldador', 'escuadra', 'tachuela'])

	n = n+1
	lista.append([])
	lista[n].append(['taller y herramientas 6'])
	lista[n].append(['tyh6'])
	lista[n].append(['tape measure', 'tool box', 'tools', 'vise', 'washer', 'wire', 'workbench', 'workshop'])
	lista[n].append(['cinta métrica', 'caja de herramientas', 'herramientas', 'torno de banco', 'arandela', 'cable', 'mesa de trabajo', 'taller'])

	n = n+1
	lista.append([])
	lista[n].append(['taller y herramientas 7'])
	lista[n].append(['tyh7'])
	lista[n].append(['wrench'])
	lista[n].append(['llave inglesa'])

	n = n+1
	lista.append([])
	lista[n].append(['las flores 1'])
	lista[n].append(['lf1'])
	lista[n].append(['azalea', 'bouquet', 'bud', 'bulb', 'cactus', 'calla lily', 'camellia', 'carnation'])
	lista[n].append(['azalea', 'ramo de flores', 'capullo', 'bulbo', 'cactos', 'cala', 'camelia', 'clavel'])

	n = n+1
	lista.append([])
	lista[n].append(['las flores 2'])
	lista[n].append(['lf2'])
	lista[n].append(['chrysantemum', 'daffodil', 'dahlia', 'daisy', 'fern', 'flower stall', 'flowerpot', 'gardenia'])
	lista[n].append(['crisantemo', 'narciso', 'dalia', 'margarita', 'helecho', 'puesto de flores', 'maceta', 'gardenia'])

	n = n+1
	lista.append([])
	lista[n].append(['las flores 3'])
	lista[n].append(['lf3'])
	lista[n].append(['geranium', 'gladiola', 'hortensia', 'hyacinth', 'iris', 'jasmin', 'leaf', 'lilac'])
	lista[n].append(['malvón', 'gladiolo', 'hortensia', 'jacinto', 'lirio', 'jazmín', 'hoja', 'lila'])

	n = n+1
	lista.append([])
	lista[n].append(['las flores 4'])
	lista[n].append(['lf4'])
	lista[n].append(['magnolia', 'marigold', 'morning glory', 'orchid', 'pansy', 'petal', 'petunia', 'pink'])
	lista[n].append(['magnolia', 'caléndula', 'campanilla azul', 'orquídea', 'pensamiento', 'pétalo', 'petunia', 'clavelina'])

	n = n+1
	lista.append([])
	lista[n].append(['las flores 5'])
	lista[n].append(['lf5'])
	lista[n].append(['poppy', 'root', 'rose', 'stem', 'sunflower', 'thorn', 'tulip', 'vase'])
	lista[n].append(['amapola', 'raíz', 'rosa', 'tallo', 'girasol', 'espina', 'tulipán', 'florero, jarrón'])

	n = n+1
	lista.append([])
	lista[n].append(['las flores 6'])
	lista[n].append(['lf6'])
	lista[n].append(['violet', 'wallflower', 'water lily', 'white lily'])
	lista[n].append(['violeta', 'alhelí', 'nenúfar', 'azucena'])

	n = n+1
	lista.append([])
	lista[n].append(['geografía 1'])
	lista[n].append(['g1'])
	lista[n].append(['bay', 'brook', 'canyon', 'channel', 'cliff', 'coast', 'creek', 'crevice'])
	lista[n].append(['bahía', 'arroyo', 'cañón', 'canal', 'acantilado', 'costa', 'riachuelo', 'falla, grieta'])

	n = n+1
	lista.append([])
	lista[n].append(['geografía 2'])
	lista[n].append(['g2'])
	lista[n].append(['desert', 'dunes', 'forest', 'glacier', 'gorge', 'grove', 'gulf', 'hills'])
	lista[n].append(['desierto', 'dunas', 'bosque, selva', 'glaciar', 'cañón, desfiladero', 'bosquecillo, arboleda', 'golfo', 'sierras, colinas'])

	n = n+1
	lista.append([])
	lista[n].append(['geografía 3'])
	lista[n].append(['g3'])
	lista[n].append(['ice floe', 'iceberg', 'island', 'lagoon', 'lake', 'marsh', 'meadow', 'mountain'])
	lista[n].append(['témpano chico', 'iceberg', 'isla', 'laguna', 'lago', 'pantano', 'prado', 'montaña'])

	n = n+1
	lista.append([])
	lista[n].append(['geografía 4'])
	lista[n].append(['g4'])
	lista[n].append(['mountain range', 'narrow pass', 'oasis', 'ocean', 'path', 'peak', 'peninsula', 'plain'])
	lista[n].append(['cordillera', 'desfiladero', 'oasis', 'océano', 'sendero, camino', 'pico, cima', 'península', 'llanura'])

	n = n+1
	lista.append([])
	lista[n].append(['geografía 5'])
	lista[n].append(['g5'])
	lista[n].append(['plateau', 'pond', 'prairie', 'precipice', 'rapids', 'ravine', 'reef', 'reservoir'])
	lista[n].append(['meseta', 'estanque', 'llanura, pradera', 'precipicio', 'rápidos', 'barranco', 'arrecife', 'embalse'])

	n = n+1
	lista.append([])
	lista[n].append(['geografía 6'])
	lista[n].append(['g6'])
	lista[n].append(['river', 'sea', 'shore', 'spring', 'strait', 'stream', 'summit', 'swamp'])
	lista[n].append(['río', 'mar', 'orilla, costa', 'manantial', 'estrecho', 'arroyo', 'cumbre', 'pantano, ciénaga'])

	n = n+1
	lista.append([])
	lista[n].append(['geografía 7'])
	lista[n].append(['g7'])
	lista[n].append(['tributary', 'valley', 'volcano', 'waterfall', 'wood'])
	lista[n].append(['afluente', 'valle', 'volcán', 'catarata', 'bosque'])

	n = n+1
	lista.append([])
	lista[n].append(['plantas y árboles 1'])
	lista[n].append(['pyá1'])
	lista[n].append(['apple tree', 'ash tree', 'bark', 'beech tree', 'birch', 'branch', 'branches', 'bush'])
	lista[n].append(['manzano', 'fresno', 'corteza', 'haya', 'abedul', 'rama', 'ramas', 'arbusto'])

	n = n+1
	lista.append([])
	lista[n].append(['plantas y árboles 2'])
	lista[n].append(['pyá2'])
	lista[n].append(['cactus', 'cedar', 'clover', 'coconut tree', 'creeper', 'cypress', 'elm', 'fir tree'])
	lista[n].append(['cactus', 'cedro', 'trébol', 'cocotero', 'enredadera', 'ciprés', 'olmo', 'abeto'])

	n = n+1
	lista.append([])
	lista[n].append(['plantas y árboles 3'])
	lista[n].append(['pyá3'])
	lista[n].append(['foliage', 'ivy', 'leaf', 'leaves', 'lemon tree', 'mahogany', 'maple', 'oak'])
	lista[n].append(['foliage', 'hiedra', 'hoja', 'hojas', 'limonero', 'caoba', 'arce', 'roble'])

	n = n+1
	lista.append([])
	lista[n].append(['plantas y árboles 4'])
	lista[n].append(['pyá4'])
	lista[n].append(['olive tree', 'orange tree', 'palm tree', 'pine', 'plane tree', 'poplar', 'roots', 'shrub'])
	lista[n].append(['olivo', 'naranjo', 'palmera', 'pino', 'plátano', 'álamo', 'raíces', 'arbusto'])

	n = n+1
	lista.append([])
	lista[n].append(['plantas y árboles 5'])
	lista[n].append(['pyá5'])
	lista[n].append(['trunk', 'twig', 'vine', 'vineyard', 'walnut tree', 'weeds', 'weeping willow', 'willow'])
	lista[n].append(['tronco', 'ramita', 'vid, parra', 'viñedo', 'nogal', 'malezas', 'sauce llorón', 'sauce'])

	n = n+1
	lista.append([])
	lista[n].append(['el universo y el cosmos 1'])
	lista[n].append(['euyec1'])
	lista[n].append(['alien', 'asteroid', 'atmosphere', 'cosmos', 'east', 'eclipse', 'galaxy', 'globe'])
	lista[n].append(['extraterrestre', 'asteroide', 'atmósfera', 'cosmos', 'este', 'eclipse', 'galaxia', 'globo, esfera'])

	n = n+1
	lista.append([])
	lista[n].append(['el universo y el cosmos 2'])
	lista[n].append(['euyec2'])
	lista[n].append(['gravity', 'Jupiter', 'light year', 'Mars', 'Mercury', 'meteor', 'meteorite', 'morning star'])
	lista[n].append(['gravedad', 'Júpiter', 'año luz', 'Marte', 'Mercurio', 'meteoro', 'meteorito', 'lucero del alba'])

	n = n+1
	lista.append([])
	lista[n].append(['el universo y el cosmos 3'])
	lista[n].append(['euyec3'])
	lista[n].append(['Neptune', 'north', 'orbit', 'outer space', 'planet', 'Satellite', 'Saturn', 'shooting star'])
	lista[n].append(['Neptuno', 'norte', 'órbita', 'espacio exterior', 'planeta', 'satélite', 'Saturno', 'estrella fugaz'])

	n = n+1
	lista.append([])
	lista[n].append(['el universo y el cosmos 4'])
	lista[n].append(['euyec4'])
	lista[n].append(['solar system', 'south', 'space', 'star', 'telescope', 'The Earth', 'The Milky Way', 'The moon'])
	lista[n].append(['sistema solar', 'sur', 'espacio', 'estrella', 'telescopio', 'La Tierra', 'La Vía Láctea', 'La Luna'])

	n = n+1
	lista.append([])
	lista[n].append(['el universo y el cosmos 5'])
	lista[n].append(['euyec5'])
	lista[n].append(['The sun', 'UFO', 'universe', 'Uranus', 'Venus', 'west'])
	lista[n].append(['El Sol', 'Ovni', 'El Universo', 'Urano', 'Venus', 'oeste'])

	n = n+1
	lista.append([])
	lista[n].append(['el tiempo 1'])
	lista[n].append(['et1'])
	lista[n].append(['blizzard', 'breeze', 'chilly', 'clear', 'cloudless', 'cloudy', 'cold', 'cool'])
	lista[n].append(['tormenta de nieve', 'brisa', 'frío, fresquito', 'despejado', 'despejado', 'nublado', 'frío', 'fresco'])

	n = n+1
	lista.append([])
	lista[n].append(['el tiempo 2'])
	lista[n].append(['et2'])
	lista[n].append(['damp', 'degrees', 'dew', 'downpour', 'drizzle', 'drought', 'dry', 'flood'])
	lista[n].append(['húmedo', 'grados', 'rocío', 'aguacero', 'llovizna', 'sequía', 'seco', 'inundación'])

	n = n+1
	lista.append([])
	lista[n].append(['el tiempo 3'])
	lista[n].append(['et3'])
	lista[n].append(['fog', 'foggy', 'freezing', 'frost', 'gale', 'hail', 'hailstones', 'hailstorm'])
	lista[n].append(['niebla', 'con niebla', 'helado', 'escarcha', 'vendaval', 'ganizo', 'piedras de granizo', 'tormenta de granizo'])

	n = n+1
	lista.append([])
	lista[n].append(['el tiempo 4'])
	lista[n].append(['et4'])
	lista[n].append(['hot', 'humid', 'hurricane', 'ice', 'lightning', 'mild', 'mist', 'overcast'])
	lista[n].append(['caluroso', 'húmedo', 'huracán', 'hielo', 'relámpago, rayo', 'templado', 'neblina', 'encapotado, cubierto'])

	n = n+1
	lista.append([])
	lista[n].append(['el tiempo 5'])
	lista[n].append(['et5'])
	lista[n].append(['rain', 'rainbow', 'raining', 'rainy', 'shower', 'sky', 'sleet', 'snow'])
	lista[n].append(['lluvia', 'arco iris', 'lloviendo', 'lluvioso', 'aguacero', 'cielo', 'aguanieve, nevizca', 'nieve'])

	n = n+1
	lista.append([])
	lista[n].append(['el tiempo 6'])
	lista[n].append(['et6'])
	lista[n].append(['snowing', 'storm', 'stormy', 'stuffy', 'sunny', 'thunder', 'thunderstorm', 'tornado'])
	lista[n].append(['nevando', 'tormenta', 'tormentoso', 'sofocante', 'soleado', 'trueno', 'tormenta eléctrica', 'tornado'])

	n = n+1
	lista.append([])
	lista[n].append(['el tiempo 7'])
	lista[n].append(['et7'])
	lista[n].append(['warm', 'wet', 'wind', 'windy'])
	lista[n].append(['cálido', 'mojado', 'viento', 'ventoso'])

	n = n+1
	lista.append([])
	lista[n].append(['familia y parientes 1'])
	lista[n].append(['fyp1'])
	lista[n].append(['aunt', 'brother', 'brother', 'children', 'cousin', 'dad, daddy', 'daughter', 'daughter'])
	lista[n].append(['tía', 'hermano', 'in-law  - cuñado', 'hijos', 'primo/a', 'papi, papito', 'hija', 'in-law  - nuera'])

	n = n+1
	lista.append([])
	lista[n].append(['familia y parientes 2'])
	lista[n].append(['fyp2'])
	lista[n].append(['father', 'father', 'first', 'goddaughter', 'godfather', 'godmother', 'godson', 'grandchildren'])
	lista[n].append(['padre', 'in-law  - suegro', 'born  - primogénito', 'ahijada', 'padrino', 'madrina', 'ahijado', 'nietos'])

	n = n+1
	lista.append([])
	lista[n].append(['familia y parientes 3'])
	lista[n].append(['fyp3'])
	lista[n].append(['granddaughter', 'grandfather', 'grandmother', 'grandparents', 'grandson', 'great', 'great', 'great'])
	lista[n].append(['nieta', 'abuelo', 'abuela', 'abuelos', 'nieto', 'grandfather  - bisabuelo', 'grandmother  - bisabuela', 'grandparents  - bisabuelos'])

	n = n+1
	lista.append([])
	lista[n].append(['familia y parientes 4'])
	lista[n].append(['fyp4'])
	lista[n].append(['husband', 'mom, mommy', 'mother', 'mother', 'nephew', 'niece', 'only child', 'orphan'])
	lista[n].append(['esposo', 'mami, mamita', 'madre', 'in-law  - suegra', 'sobrino', 'sobrina', 'hijo/a único/a', 'huérfano'])

	n = n+1
	lista.append([])
	lista[n].append(['familia y parientes 5'])
	lista[n].append(['fyp5'])
	lista[n].append(['parents', 'sister', 'sister', 'son', 'son', 'stepdaughter', 'stepfather', 'stepmother'])
	lista[n].append(['padres', 'hermana', 'in-law  - cuñada', 'hijo', 'in-law  - yerno', 'hijastra', 'padrastro', 'madrastra'])

	n = n+1
	lista.append([])
	lista[n].append(['familia y parientes 6'])
	lista[n].append(['fyp6'])
	lista[n].append(['stepson', 'uncle', 'wife'])
	lista[n].append(['hijastro', 'tío', 'esposa'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 1'])
	lista[n].append(['typ1'])
	lista[n].append(['accountant', 'actor', 'actress', 'announcer', 'archaeologist', 'architect', 'artist', 'astrologer'])
	lista[n].append(['contador', 'actor', 'actriz', 'locutor', 'arqueólogo', 'arquitecto', 'artista', 'astrólogo'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 2'])
	lista[n].append(['typ2'])
	lista[n].append(['astronaut', 'astronomer', 'athlete', 'attorney', 'auctioneer', 'auditor', 'author', 'baby'])
	lista[n].append(['astronauta', 'astrónomo', 'atleta', 'abogado', 'subastador', 'auditor', 'autor', 'sitter  - niñera'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 3'])
	lista[n].append(['typ3'])
	lista[n].append(['baker', 'bank teller', 'banker', 'barman', 'beautician', 'bell boy', 'biologist', 'blacksmith'])
	lista[n].append(['panadero', 'cajero de banco', 'banquero', 'barman, mozo', 'esteticista', 'botones de hotel', 'biólogo', 'herrero'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 4'])
	lista[n].append(['typ4'])
	lista[n].append(['bookkeeper', 'bricklayer', 'broker', 'builder', 'bullfighter', 'bus driver', 'businessman', 'butcher'])
	lista[n].append(['perito mercantil', 'albañil', 'agente de bolsa', 'constructor', 'torero', 'conductor de bus', 'empresario', 'carnicero'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 5'])
	lista[n].append(['typ5'])
	lista[n].append(['butler', 'cameraman', 'carpenter', 'cartoonist', 'cashier', 'chef', 'chemist', 'clerk'])
	lista[n].append(['mayordomo', 'camarógrafo', 'carpintero', 'dibujante, caricaturista', 'cajero', 'chef', 'químico, farmacéutico', 'oficinista'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 6'])
	lista[n].append(['typ6'])
	lista[n].append(['coach', 'college professor', 'company director', 'composer', 'computer programmer', 'conductor', 'consultant', 'cook'])
	lista[n].append(['entrenador', 'profesor universitario', 'director de empresa', 'compositor', 'programador', 'director de orquesta', 'consultor', 'cocinero'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 7'])
	lista[n].append(['typ7'])
	lista[n].append(['counselor', 'cowboy', 'craftsman', 'cyclist', 'dancer', 'decorator', 'dentist', 'designer'])
	lista[n].append(['asesor, consultor', 'vaquero', 'artesano', 'ciclista', 'bailarín', 'decorador', 'dentista', 'diseñador'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 8'])
	lista[n].append(['typ8'])
	lista[n].append(['detective', 'doctor', 'dog walker', 'dressmaker', 'driver', 'economist', 'electrician', 'employee'])
	lista[n].append(['detective', 'doctor', 'paseador de perros', 'modista', 'chofer', 'economista', 'electricista', 'empleado'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 9'])
	lista[n].append(['typ9'])
	lista[n].append(['engineer', 'farmer', 'fireman', 'fisherman', 'fishmonger', 'flight attendant', 'florist', 'fortune teller'])
	lista[n].append(['ingeniero', 'agricultor', 'bombero', 'pescador', 'vendedor de pescado', 'azafata', 'florista', 'adivino'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 10'])
	lista[n].append(['typ10'])
	lista[n].append(['garbage collector', 'gardener', 'greengrocer', 'grocer', 'hairdresser', 'historian', 'house painter', 'housekeeper'])
	lista[n].append(['basurero', 'jardinero', 'verdulero', 'almacenero', 'peluquero', 'historiador', 'pintor de casas', 'ama de llaves'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 11'])
	lista[n].append(['typ11'])
	lista[n].append(['housewife', 'hunter', 'instructor', 'insurance agent', 'interpreter', 'ironmonger', 'janitor', 'jeweller'])
	lista[n].append(['ama de casa', 'cazador', 'instructor', 'agente de seguros', 'intérprete', 'ferretero', 'conserje', 'joyero'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 12'])
	lista[n].append(['typ12'])
	lista[n].append(['journalist', 'judge', 'lawyer', 'lifeguard', 'locksmith', 'magician', 'maid', 'mailman'])
	lista[n].append(['periodista', 'juez', 'abogado', 'bañero', 'cerrajero', 'mago', 'empleada doméstica', 'cartero'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 13'])
	lista[n].append(['typ13'])
	lista[n].append(['manager', 'manicurist', 'manufacturer', 'masseur', 'masseuse', 'mathematician', 'mechanic', 'milkman'])
	lista[n].append(['gerente', 'manicuro', 'fabricante, industrial', 'masajista hombre', 'masajista mujer', 'matemático', 'mecánico', 'lechero'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 14'])
	lista[n].append(['typ14'])
	lista[n].append(['miner', 'model', 'musician', 'newspaper boy', 'nun', 'nurse', 'ophthalmologist', 'optician'])
	lista[n].append(['minero', 'modelo', 'músico', 'repartidor de diarios', 'monja', 'enfermero/a', 'oftalmólogo', 'óptico'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 15'])
	lista[n].append(['typ15'])
	lista[n].append(['orator', 'paediatrician', 'painter', 'park ranger', 'peasant', 'pharmacist', 'philosopher', 'photographer'])
	lista[n].append(['orador', 'pediatra', 'pintor', 'guardaparques', 'campesino', 'farmacéutico', 'filósofo', 'fotógrafo'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 16'])
	lista[n].append(['typ16'])
	lista[n].append(['physician', 'physicist', 'pianist', 'pilot', 'plumber', 'poet', 'police officer', 'policeman'])
	lista[n].append(['médico', 'físico', 'pianista', 'piloto', 'plomero, fontanero', 'poet', 'agente de policía', 'policía'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 17'])
	lista[n].append(['typ17'])
	lista[n].append(['politician', 'postman', 'presenter', 'president', 'priest', 'printer', 'programmer', 'psychiatrist'])
	lista[n].append(['político', 'cartero', 'presentador', 'presidente', 'sacerdote', 'imprentero', 'programador', 'psiquiatra'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 18'])
	lista[n].append(['typ18'])
	lista[n].append(['psychologist', 'psychoterapist', 'publisher', 'receptionist', 'reporter', 'researcher', 'sailor', 'salesclerk'])
	lista[n].append(['psicólogo', 'psicoterapeuta', 'editor', 'recepcionista', 'reportero', 'investigador', 'marinero', 'vendedor'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 19'])
	lista[n].append(['typ19'])
	lista[n].append(['salesman', 'saleswoman', 'scientist', 'sculptor', 'seamstress', 'secret agent', 'secretary', 'security guard'])
	lista[n].append(['vendedor', 'vendedora', 'científico', 'escultor', 'costurera', 'agente secreto', 'secretario/a', 'guardia de seguridad'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 20'])
	lista[n].append(['typ20'])
	lista[n].append(['servant', 'shepherd', 'shoemaker', 'shopkeeper', 'singer', 'soccer player', 'social worker', 'soldier'])
	lista[n].append(['criado', 'pastor', 'zapatero', 'comerciante, tendero', 'cantante', 'futbolista', 'trabajadora social', 'soldado'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 21'])
	lista[n].append(['typ21'])
	lista[n].append(['sportsman', 'state agent', 'stationer', 'statistician', 'stenographer', 'stewardess', 'stockbrocker', 'street sweeper'])
	lista[n].append(['deportista', 'agente inmobiliario', 'librero', 'estadístico', 'taquígrafo', 'azafata', 'corredor de bolsa', 'barrendero'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 22'])
	lista[n].append(['typ22'])
	lista[n].append(['student', 'supervisor', 'surgeon', 'tailor', 'tax inspector', 'taxi driver', 'taylor', 'teacher'])
	lista[n].append(['estudiante', 'supervisor', 'cirujano', 'sastre', 'inspector de impuestos', 'taxista', 'sastre', 'maestro'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 23'])
	lista[n].append(['typ23'])
	lista[n].append(['technician', 'telephone operator', 'tourist guide', 'translator', 'travel agent', 'truck driver', 'typist', 'undertaker'])
	lista[n].append(['técnico', 'telefonista', 'guía de turistas', 'traductor', 'agente de viajes', 'camionero', 'mecanógrafa', 'funebrero'])

	n = n+1
	lista.append([])
	lista[n].append(['trabajos y profesiones 24'])
	lista[n].append(['typ24'])
	lista[n].append(['veterinarian', 'waiter', 'waitress', 'watchmaker', 'welder', 'worker', 'writer'])
	lista[n].append(['veterinario', 'camarero', 'camarera', 'relojero', 'soldador', 'obrero', 'escritor'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 1'])
	lista[n].append(['sye1'])
	lista[n].append(['adoration', 'affection', 'agitation', 'agony', 'alarm', 'amazement', 'amusement', 'anger'])
	lista[n].append(['adoración', 'afecto', 'agitación', 'agonía', 'alarma', 'asombro', 'divesión', 'cólera, ira'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 2'])
	lista[n].append(['sye2'])
	lista[n].append(['anguish', 'annoyance', 'anxiety', 'apprehension', 'arousal', 'astonishment', 'attraction', 'bitterness'])
	lista[n].append(['angustia', 'molestia', 'ansiedad', 'aprehensión', 'excitatión', 'asombro', 'atracción', 'amargura'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 3'])
	lista[n].append(['sye3'])
	lista[n].append(['bliss', 'caring', 'cheerfulness', 'compassion', 'contempt', 'contentment', 'defeat', 'dejection'])
	lista[n].append(['felicidad', 'preocupación', 'alegría', 'compasión', 'desprecio', 'alegría', 'fracaso', 'desánimo'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 4'])
	lista[n].append(['sye4'])
	lista[n].append(['delight', 'depression', 'desire', 'despair', 'disappointment', 'disgust', 'dislike', 'dismay'])
	lista[n].append(['placer', 'depresión', 'deseo', 'desesperación', 'desilusión', 'repugnancia', 'aversión', 'consternación'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 5'])
	lista[n].append(['sye5'])
	lista[n].append(['distress', 'dread', 'eagerness', 'ecstasy', 'elation', 'embarrassment', 'enjoyment', 'enthusiasm'])
	lista[n].append(['angustia', 'temor', 'afán', 'éxtasis', 'euforía', 'vergüenza, bochorno', 'placer', 'entusiasmo'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 6'])
	lista[n].append(['sye6'])
	lista[n].append(['envy', 'euphoria', 'exasperation', 'excitement', 'exhilaration', 'fear', 'ferocity', 'fondness'])
	lista[n].append(['envidia', 'euforia', 'exasperación', 'entusiasmo', 'regocijo', 'miedo', 'ferocidad', 'cariño'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 7'])
	lista[n].append(['sye7'])
	lista[n].append(['fright', 'frustration', 'fury', 'gaiety', 'glee', 'gloom', 'greed', 'grief'])
	lista[n].append(['susto', 'frustración', 'furia', 'alegría', 'regocijo', 'tristeza', 'avaricia', 'pena'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 8'])
	lista[n].append(['sye8'])
	lista[n].append(['guilt', 'happiness', 'hate', 'homesickness', 'hope', 'hopelessness', 'horror', 'hostility'])
	lista[n].append(['culpa', 'felicidad', 'odio', 'nostalgia', 'esperanza', 'desesperación', 'horror', 'hostilidad'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 9'])
	lista[n].append(['sye9'])
	lista[n].append(['humiliation', 'hurt', 'hysteria', 'infatuation', 'insecurity', 'insult', 'irritation', 'isolation'])
	lista[n].append(['humillación', 'daño', 'histeria', 'encaprichamiento', 'inseguridad', 'insulto', 'irritación', 'aislamiento'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 10'])
	lista[n].append(['sye10'])
	lista[n].append(['jealousy', 'joy', 'jubilation', 'liking', 'loathing', 'loneliness', 'longing', 'love'])
	lista[n].append(['celos', 'alegría', 'júbilo', 'gusto', 'odio, aversion', 'soledad', 'anhelo', 'amor'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 11'])
	lista[n].append(['sye11'])
	lista[n].append(['lust', 'melancholy', 'misery', 'mortification', 'nervousness', 'optimism', 'outrage', 'pain'])
	lista[n].append(['lujuria', 'melancolía', 'aflicción, sufrimiento', 'mortificación', 'nerviosismo', 'optimismo', 'indignación', 'dolor'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 12'])
	lista[n].append(['sye12'])
	lista[n].append(['panic', 'passion', 'pity', 'pleasure', 'pride', 'rage', 'rapture', 'regret'])
	lista[n].append(['pánico', 'pasión', 'compasión, lástima', 'placer', 'orgullo', 'rabia', 'éxtasis', 'remordimiento, lamento'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 13'])
	lista[n].append(['sye13'])
	lista[n].append(['rejection', 'relief', 'remorse', 'repentance', 'resentment', 'revulsion', 'sadness', 'satisfaction'])
	lista[n].append(['rechazo', 'alivio', 'remordimiento', 'arrepentimiento', 'resentimiento', 'asco, repulsión', 'tristeza', 'satisfacción'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 14'])
	lista[n].append(['sye14'])
	lista[n].append(['scorn', 'shame', 'shock', 'sorrow', 'spite', 'suffering', 'surprise', 'sympathy'])
	lista[n].append(['desprecio', 'vergüenza', 'conmoción', 'pena', 'rencor, despecho', 'sufrimiento', 'sorpresa', 'compasión'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 15'])
	lista[n].append(['sye15'])
	lista[n].append(['tenderness', 'tenseness', 'terror', 'thrill', 'torment', 'triumph', 'uneasiness', 'unhappiness'])
	lista[n].append(['ternura', 'tensión', 'terror', 'emoción', 'tormento', 'triunfo', 'inquietud', 'infelicidad'])

	n = n+1
	lista.append([])
	lista[n].append(['sentimientos y emociones 16'])
	lista[n].append(['sye16'])
	lista[n].append(['woe', 'worry', 'wrath', 'zeal', 'zest'])
	lista[n].append(['aflicción', 'preocupación', 'ira', 'celo', 'entusiasmo'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 1'])
	lista[n].append(['edá1'])
	lista[n].append(['afraid', 'alarmed', 'alert', 'amazed', 'angry', 'annoyed', 'ashamed', 'astonished'])
	lista[n].append(['temeroso, con miedo', 'alarmado', 'alerta', 'asombrado', 'enojado', 'molesto', 'avergonzado', 'asombrado'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 2'])
	lista[n].append(['edá2'])
	lista[n].append(['bored', 'calm', 'cheerful', 'complacent', 'confident', 'confused', 'content', 'content'])
	lista[n].append(['aburrido', 'calm', 'alegre', 'satisfecho consigo mismo', 'confiado', 'confundido', 'satisfecho', 'contento'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 3'])
	lista[n].append(['edá3'])
	lista[n].append(['contented', 'curious', 'dejected', 'delighted', 'depressed', 'disappointed', 'disheartened', 'disillusioned'])
	lista[n].append(['contento, satisfecho', 'curioso', 'desanimado', 'encantado', 'deprimido', 'defraudado', 'descorazonado', 'desilusionado'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 4'])
	lista[n].append(['edá4'])
	lista[n].append(['distressed', 'dizzy', 'drunk', 'eager', 'edgy', 'elated', 'embarrassed', 'emotional'])
	lista[n].append(['angustiado', 'mareado', 'borracho', 'ansioso, deseoso', 'nervioso, inquieto', 'regocijado', 'avergonzado, abochornado', 'emocionado, sensible'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 5'])
	lista[n].append(['edá5'])
	lista[n].append(['enthusiastic', 'envious', 'excited', 'frustrated', 'furious', 'glad', 'gloomy', 'grateful'])
	lista[n].append(['entusiasmado', 'envidioso', 'excitado', 'frustrado', 'furioso', 'contento', 'triste, pesimista', 'agradecido'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 6'])
	lista[n].append(['edá6'])
	lista[n].append(['groggy', 'grumpy', 'guilty', 'happy', 'homesick', 'hopeful', 'horny', 'hostile'])
	lista[n].append(['aturdido', 'malhumorado', 'culpable', 'feliz, contento', 'nostálgico', 'esperanzado', 'caliente, cachondo', 'hostil'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 7'])
	lista[n].append(['edá7'])
	lista[n].append(['humiliated', 'hungry', 'hurt', 'impressed', 'in love', 'indifferent', 'indignant', 'insecure'])
	lista[n].append(['humillado', 'hambriento, con hambre', 'herido', 'impresionado', 'enamorado', 'indiferente', 'indignado', 'inseguro'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 8'])
	lista[n].append(['edá8'])
	lista[n].append(['irritable', 'jealous', 'jubilant', 'lazy', 'listless', 'lonely', 'merry', 'mischievous'])
	lista[n].append(['irritable', 'celoso', 'jubiloso', 'perezoso', 'indiferente, desganado', 'solitario, solo', 'alegre', 'travieso'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 9'])
	lista[n].append(['edá9'])
	lista[n].append(['miserable', 'nervous', 'nostalgic', 'offended', 'optimistic', 'overwhelmed', 'playful', 'pleased'])
	lista[n].append(['triste, desgraciado', 'nervioso', 'nostálgico', 'ofendido', 'optimista', 'agobiado', 'juguetón', 'complacido, satisfecho'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 10'])
	lista[n].append(['edá10'])
	lista[n].append(['positive', 'proud', 'puzzled', 'rejected', 'relaxed', 'relieved', 'resentful', 'restless'])
	lista[n].append(['positivo', 'orgulloso', 'confundido', 'rechazado', 'relajado', 'aliviado', 'resentido', 'inquieto'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 11'])
	lista[n].append(['edá11'])
	lista[n].append(['sad', 'satisfied', 'scared', 'sentimental', 'shocked', 'sick', 'sleepy', 'surprised'])
	lista[n].append(['triste', 'satisfecho', 'asustado', 'sentimental', 'impresionado, conmovido', 'enfermo', 'soñoliento', 'sorprendido'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 12'])
	lista[n].append(['edá12'])
	lista[n].append(['terrified', 'thankful', 'thirsty', 'thoughtful', 'thrilled', 'tired', 'touched', 'touchy'])
	lista[n].append(['aterrorizado', 'agradecido', 'sediento, con sed', 'pensativo', 'estremecido', 'cansado, fatigado', 'emocionado', 'susceptible'])

	n = n+1
	lista.append([])
	lista[n].append(['estados de ánimo 13'])
	lista[n].append(['edá13'])
	lista[n].append(['uncomfortable', 'unhappy', 'upset', 'wary', 'weary', 'worried'])
	lista[n].append(['incómodo, molesto', 'desdichado', 'molesto', 'cauteloso', 'cansado', 'preocupado'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de hombre 1'])
	lista[n].append(['rdh1'])
	lista[n].append(['anorak', 'belt', 'boots', 'bow', 'briefs', 'cap', 'cardigan', 'coat'])
	lista[n].append(['campera de esquiar', 'cinturón', 'botas', 'tie  - moño', 'calzoncillos', 'gorra', 'pulóver abierto', 'abrigo'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de hombre 2'])
	lista[n].append(['rdh2'])
	lista[n].append(['collar', 'cuff', 'denim jacket', 'gloves', 'handkerchief', 'hat', 'jacket', 'jeans'])
	lista[n].append(['cuello de camisa', 'puño de camisa', 'campera de jean', 'guantes', 'pañuelo de bolsillo', 'sombrero', 'saco sport, chaqueta', 'pantalón vaquero'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de hombre 3'])
	lista[n].append(['rdh3'])
	lista[n].append(['leather jacket', 'neckerchief', 'overalls', 'overcoat', 'pajamas', 'pants', 'pullover', 'raincoat'])
	lista[n].append(['campera de cuero', 'pañuelo de cuello', 'mameluco, overol', 'abrigo, sobretodo', 'piyama', 'pantalones', 'pulóver', 'impermeable'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de hombre 4'])
	lista[n].append(['rdh4'])
	lista[n].append(['scarf', 'shirt', 'shoes', 'shorts', 'slacks', 'slippers', 'sneakers', 'socks'])
	lista[n].append(['bufanda', 'camisa', 'zapatos', 'pantalón corto', 'pantalones informales', 'pantuflas', 'zapatillas', 'calcetines, medias'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de hombre 5'])
	lista[n].append(['rdh5'])
	lista[n].append(['sportswear', 'suit', 'suspenders', 'sweater', 'sweatshirt', 'swimming trunks', 'T', 'tennis shoes'])
	lista[n].append(['ropa deportiva', 'traje de vestir', 'tiradores', 'pulóver', 'sudadera, buzo', 'traje de baño, malla', 'shirt  - camiseta, remera', 'zapatillas deportivas'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de hombre 6'])
	lista[n].append(['rdh6'])
	lista[n].append(['tie', 'trousers', 'tuxedo', 'umbrella', 'underpants', 'undershirt', 'underwear', 'vest'])
	lista[n].append(['corbata', 'pantalones', 'esmoquin', 'paraguas', 'calzoncillos', 'camiseta', 'ropa interior', 'chaleco'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de hombre 7'])
	lista[n].append(['rdh7'])
	lista[n].append(['wallet'])
	lista[n].append(['billetera'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de mujer 1'])
	lista[n].append(['rdm1'])
	lista[n].append(['bag', 'bathrobe', 'belt', 'beret', 'bikini', 'blouse', 'boots', 'bra'])
	lista[n].append(['bolso', 'bata de baño', 'cinturón', 'boina', 'bikini', 'blusa', 'botas', 'corpiño, sostén'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de mujer 2'])
	lista[n].append(['rdm2'])
	lista[n].append(['bracelet', 'cloak', 'coat', 'corset', 'dress', 'earring', 'fan', 'flip'])
	lista[n].append(['pulcera, brazalete', 'capa', 'abrigo', 'faja, corsé', 'vestido', 'aro, pendiente', 'abanico', 'flops  - ojotas, chancletas'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de mujer 3'])
	lista[n].append(['rdm3'])
	lista[n].append(['fur coat', 'garter belt', 'gloves', 'handkerchief', 'jeans', 'knickers', 'lapel', 'leggings'])
	lista[n].append(['saco de piel', 'liguero', 'guantes', 'pañuelo de bolsillo', 'pantalones vaqueros', 'bragas, bombacha', 'solapa', 'calzas deportivas'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de mujer 4'])
	lista[n].append(['rdm4'])
	lista[n].append(['miniskirt', 'neckerchief', 'necklace', 'nightgown', 'pajamas', 'panties', 'pullover', 'purse'])
	lista[n].append(['minifalda', 'pañuelo de cuello', 'collar', 'camisón', 'piyama', 'bragas, bombacha', 'pullover', 'cartera'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de mujer 5'])
	lista[n].append(['rdm5'])
	lista[n].append(['raincoat', 'sandals', 'scarf', 'shawl', 'shoes', 'shorts', 'skirt', 'slip'])
	lista[n].append(['impermeable, gabardina', 'sandalias', 'bufanda', 'chal', 'zapatos', 'pantalón corto', 'falda', 'combinación, enagua'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de mujer 6'])
	lista[n].append(['rdm6'])
	lista[n].append(['slippers', 'socks', 'stockings', 'sunglasses', 'sweater', 'tennis shoes', 'tights', 'trousers'])
	lista[n].append(['pantuflas', 'calcetines, medias', 'medias', 'gafas de sol', 'suéter', 'zapatillas', 'medias bombacha', 'pantalón'])

	n = n+1
	lista.append([])
	lista[n].append(['ropa de mujer 7'])
	lista[n].append(['rdm7'])
	lista[n].append(['umbrella', 'vest'])
	lista[n].append(['paraguas', 'chaleco'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos positivos) 1'])
	lista[n].append(['p(p1'])
	lista[n].append(['adventurous', 'ambitious', 'amusing', 'attentive', 'audacious', 'brave', 'broad', 'calm'])
	lista[n].append(['aventurero', 'ambicioso', 'divertido', 'atento, cortés', 'audaz', 'valiente', 'minded  - liberal, tolerante', 'calmo'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos positivos) 2'])
	lista[n].append(['p(p2'])
	lista[n].append(['carefree', 'careful', 'cautious', 'charming', 'cheerful', 'considerate', 'courageous', 'creative'])
	lista[n].append(['despreocupado', 'prudente', 'cauteloso, prudente', 'encantador', 'alegre', 'considerado', 'valeroso, valiente', 'creativo'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos positivos) 3'])
	lista[n].append(['p(p3'])
	lista[n].append(['curious', 'dependable', 'determined', 'discreet', 'easy', 'energetic', 'enthusiastic', 'extrovert'])
	lista[n].append(['curioso', 'fiable, confiable', 'decidido, resuelto', 'discreto', 'going  - relajado, tranquilo', 'energético', 'entusiasta', 'extrovertido'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos positivos) 4'])
	lista[n].append(['p(p4'])
	lista[n].append(['faithful', 'frank', 'friendly', 'generous', 'gentle', 'grateful', 'hard', 'honest'])
	lista[n].append(['fiel', 'franco', 'amigable', 'generoso', 'suave, tierno', 'agradecido', 'working  - trabajador', 'honesto'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos positivos) 5'])
	lista[n].append(['p(p5'])
	lista[n].append(['humble', 'imaginative', 'ingenious', 'intelligent', 'kind', 'light', 'likable', 'lively'])
	lista[n].append(['humilde', 'imaginativo', 'ingenioso', 'inteligente', 'amable', 'hearted  - alegre', 'agradable, simpático', 'vivaz'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos positivos) 6'])
	lista[n].append(['p(p6'])
	lista[n].append(['loyal', 'mature', 'methodical', 'meticulous', 'modest', 'obedient', 'optimistic', 'organized'])
	lista[n].append(['leal', 'maduro', 'metódico', 'meticuloso', 'modesto', 'obediente', 'optimista', 'organizado'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos positivos) 7'])
	lista[n].append(['p(p7'])
	lista[n].append(['outgoing', 'passionate', 'patient', 'polite', 'practical', 'quiet', 'realistic', 'reliable'])
	lista[n].append(['sociable, extrovertido', 'apasionado', 'paciente', 'cortés, atento', 'práctico', 'callado, reservado', 'realista', 'confiable'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos positivos) 8'])
	lista[n].append(['p(p8'])
	lista[n].append(['resourceful', 'respectful', 'responsible', 'self', 'sensible', 'sensitive', 'serious', 'sincere'])
	lista[n].append(['habilidoso, ingenioso', 'respetuoso', 'responsable', 'confident  - seguro', 'sensato', 'sensible', 'serio, formal', 'sincero'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos positivos) 9'])
	lista[n].append(['p(p9'])
	lista[n].append(['smart', 'sociable', 'strong', 'sympathetic', 'systematic', 'talkative', 'thankful', 'thrifty'])
	lista[n].append(['listo, inteligente', 'sociable', 'willed  - tenaz', 'compasivo, comprensivo', 'sistemático', 'hablador', 'agradecido', 'ahorrativo'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos positivos) 10'])
	lista[n].append(['p(p10'])
	lista[n].append(['tolerant', 'trustworthy', 'truthful', 'understanding', 'wise', 'zealous'])
	lista[n].append(['tolerante', 'confiable', 'veraz, sincero', 'comprensivo', 'sabio', 'entusiasta, ferviente'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos negativos) 1'])
	lista[n].append(['p(n1'])
	lista[n].append(['absent', 'aggressive', 'annoying', 'arrogant', 'arrogant', 'bad', 'boastful', 'boring'])
	lista[n].append(['minded  - distraído', 'agresivo', 'molesto', 'arrogante, prepotente', 'arrogante', 'tempered  - malhumorado', 'fanfarrón', 'aburrido'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos negativos) 2'])
	lista[n].append(['p(n2'])
	lista[n].append(['bossy', 'cheeky', 'clumsy', 'competitive', 'conceited', 'cowardly', 'credulous', 'cruel'])
	lista[n].append(['mandón', 'atrevido', 'torpe', 'competitivo', 'vanidoso', 'cobarde', 'crédulo', 'cruel'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos negativos) 3'])
	lista[n].append(['p(n3'])
	lista[n].append(['dishonest', 'disrespectful', 'dominant', 'eccentric', 'envious', 'fiend', 'forgetful', 'frivolous'])
	lista[n].append(['deshonesto', 'irrespetuoso', 'dominante', 'excéntrico', 'envidioso', 'desalmado', 'olvidadizo', 'frívolo'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos negativos) 4'])
	lista[n].append(['p(n4'])
	lista[n].append(['fussy', 'gullible', 'hypocritical', 'impatient', 'impulsive', 'indifferent', 'insecure', 'insensitive'])
	lista[n].append(['quisquilloso, exigente', 'crédulo', 'hipócrita', 'impaciente', 'impulsivo', 'indiferente', 'inseguro', 'insensible'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos negativos) 5'])
	lista[n].append(['p(n5'])
	lista[n].append(['insolent', 'introverted', 'irascible', 'irresponsible', 'jealous', 'lazy', 'lonely', 'materialistic'])
	lista[n].append(['insolente', 'introvertido', 'irascible', 'irresponsable', 'celoso', 'haragán', 'solitario', 'materialista'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos negativos) 6'])
	lista[n].append(['p(n6'])
	lista[n].append(['mean', 'moody', 'naive', 'nosy', 'obsessive', 'obstinate', 'passive', 'pessimistic'])
	lista[n].append(['mezquino, malo', 'malhumorado', 'ingenuo', 'metido, fisgón', 'obsesivo', 'obstinado, testarudo', 'pasivo', 'pesimista'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos negativos) 7'])
	lista[n].append(['p(n7'])
	lista[n].append(['petty', 'pretentious', 'proud', 'rash', 'rebellious', 'restless', 'rude', 'ruthless'])
	lista[n].append(['mezquino', 'presuntuoso, pretencioso', 'orgulloso', 'imprudente, precipitado', 'rebelde', 'inquieto', 'descortés, grosero', 'despiadado'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos negativos) 8'])
	lista[n].append(['p(n8'])
	lista[n].append(['selfish', 'shy', 'spiteful', 'stingy', 'strict', 'stubborn', 'sullen', 'talkative'])
	lista[n].append(['egoísta', 'tímido', 'rencoroso', 'tacaño', 'estricto', 'terco', 'hosco', 'charlatán'])

	n = n+1
	lista.append([])
	lista[n].append(['personalidad (rasgos negativos) 9'])
	lista[n].append(['p(n9'])
	lista[n].append(['unpredictable', 'unreliable', 'vain', 'vicious', 'vindictive'])
	lista[n].append(['impredecible', 'desconfiable', 'presumido', 'despiadado, cruel', 'vengativo'])

	n = n+1
	lista.append([])
	lista[n].append(['países 1'])
	lista[n].append(['p1'])
	lista[n].append(['Afghanistan', 'Argentina', 'Australia', 'Austria', 'Belgium', 'Bolivia', 'Brazil', 'Bulgaria'])
	lista[n].append(['Afganistán', 'Argentina', 'Australia', 'Austria', 'Bélgica', 'Bolivia', 'Brasil', 'Bulgaria'])

	n = n+1
	lista.append([])
	lista[n].append(['países 2'])
	lista[n].append(['p2'])
	lista[n].append(['Canada', 'Chile', 'China', 'Colombia', 'Costa Rica', 'Cuba', 'Czech Republic', 'Denmark'])
	lista[n].append(['Canadá', 'Chile', 'China', 'Colombia', 'Costa Rica', 'Cuba', 'República Checa', 'Dinamarca'])

	n = n+1
	lista.append([])
	lista[n].append(['países 3'])
	lista[n].append(['p3'])
	lista[n].append(['Dominican Republic', 'Ecuador', 'Egypt', 'Englan', 'Finland', 'France', 'Germany', 'Greece'])
	lista[n].append(['República dominicana', 'Ecuador', 'Egipto', 'Englan', 'Finlandia', 'Francia', 'Alemania', 'Grecia'])

	n = n+1
	lista.append([])
	lista[n].append(['países 4'])
	lista[n].append(['p4'])
	lista[n].append(['Greenland', 'Guatemala', 'Haiti', 'Hawaii', 'Honduras', 'Hungary', 'Iceland', 'India'])
	lista[n].append(['Groenlandia', 'Guatemala', 'Haití', 'Hawai', 'Honduras', 'Hungría', 'Islandia', 'India'])

	n = n+1
	lista.append([])
	lista[n].append(['países 5'])
	lista[n].append(['p5'])
	lista[n].append(['Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan'])
	lista[n].append(['Indonesia', 'Irán', 'Iraq', 'Irlanda', 'Israel', 'Italia', 'Jamaica', 'Japón'])

	n = n+1
	lista.append([])
	lista[n].append(['países 6'])
	lista[n].append(['p6'])
	lista[n].append(['Korea', 'Lebanon', 'Malaysia', 'Malta', 'Mexico', 'Morocco', 'Nepal', 'Netherlands'])
	lista[n].append(['Corea', 'Líbano', 'Malasia', 'Malta', 'México', 'Marruecos', 'Nepal', 'Países Bajos'])

	n = n+1
	lista.append([])
	lista[n].append(['países 7'])
	lista[n].append(['p7'])
	lista[n].append(['New Zealand', 'Nicaragua', 'Nigeria', 'Norway', 'Pakistan', 'Palestine', 'Panama', 'Paraguay'])
	lista[n].append(['Nueva Zelanda', 'Nicaragua', 'Nigeria', 'Noruega', 'Paquistán', 'Palestina', 'Panamá', 'Paraguay'])

	n = n+1
	lista.append([])
	lista[n].append(['países 8'])
	lista[n].append(['p8'])
	lista[n].append(['Peru', 'Philipines', 'Poland', 'Portugal', 'Puerto Rico', 'Rumania', 'Russia', 'Saudi Arabia'])
	lista[n].append(['Perú', 'Philipines', 'Polonia', 'Portugal', 'Puerto Rico', 'Rumania', 'Rusia', 'Arabia Saudí'])

	n = n+1
	lista.append([])
	lista[n].append(['países 9'])
	lista[n].append(['p9'])
	lista[n].append(['Scotland', 'Singapore', 'Spain', 'Sweden', 'Switzerland', 'Syria', 'Tahiti', 'Thailand'])
	lista[n].append(['Escocia', 'Singapur', 'España', 'Suecia', 'Suiza', 'Siria', 'Tahití', 'Tailandia'])

	n = n+1
	lista.append([])
	lista[n].append(['países 10'])
	lista[n].append(['p10'])
	lista[n].append(['Tunisia', 'Turkey', 'Ukraine', 'United Kingdom', 'United States', 'Uruguay', 'Venezuela', 'Vietnam'])
	lista[n].append(['Túnez', 'Turquía', 'Ucrania', 'Reino Unido', 'Estados Unidos', 'Uruguay', 'Venezuela', 'Vietnam'])

	n = n+1
	lista.append([])
	lista[n].append(['países 11'])
	lista[n].append(['p11'])
	lista[n].append(['Wales', 'Yugoslavia'])
	lista[n].append(['País de Gales', 'Yugoslavia'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 1'])
	lista[n].append(['dyj1'])
	lista[n].append(['accesory', 'acquittal', 'alibi', 'appeal', 'arson', 'arsonist', 'assailant', 'assassin'])
	lista[n].append(['cómplice', 'absolución', 'coartada', 'apelación', 'incendio premeditado', 'incendiario', 'agresor', 'asesino (de un político)'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 2'])
	lista[n].append(['dyj2'])
	lista[n].append(['assassination', 'assault', 'attorney', 'bail', 'blackmail', 'blackmailer', 'briber', 'bribery'])
	lista[n].append(['asesinato (de un político)', 'agresión', 'abogado', 'fianza', 'chantaje', 'chantajista', 'sobornador', 'soborno'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 3'])
	lista[n].append(['dyj3'])
	lista[n].append(['burglar', 'burglary', 'convict', 'court', 'court case', 'court order', 'crime', 'custody'])
	lista[n].append(['ladrón (de casas)', 'hurto (de casas)', 'presidiario', 'corte', 'pleito', 'orden judicial', 'delito', 'custodia'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 4'])
	lista[n].append(['dyj4'])
	lista[n].append(['death penalty', 'defendant', 'drug dealer', 'evidence', 'felony', 'fine', 'forger', 'forgery'])
	lista[n].append(['pena de muerte', 'acusado', 'vendedor de drogas', 'evidencia', 'crimen', 'multa', 'falsificador', 'falsificación'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 5'])
	lista[n].append(['dyj5'])
	lista[n].append(['fraud', 'guilty', 'heir', 'hijacking', 'hostage', 'indictment', 'innocent', 'jail'])
	lista[n].append(['fraude', 'culpable, inocente', 'heredero', 'secuestro de avión', 'rehén', 'acusación', 'inocente', 'cárcel'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 6'])
	lista[n].append(['dyj6'])
	lista[n].append(['judge', 'jury', 'kidnapper', 'kidnapping', 'lawyer', 'life sentence', 'misdemeanor', 'mugger'])
	lista[n].append(['juez', 'jurado', 'secuestrador', 'secuestro', 'abogado', 'cadena perpetua', 'delito menor', 'atracador'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 7'])
	lista[n].append(['dyj7'])
	lista[n].append(['mugging', 'murder', 'murderer', 'narco', 'narco', 'not guilty', 'oath', 'on parole'])
	lista[n].append(['atraco', 'asesinato', 'asesino', 'trafficker  - narcotraficante', 'trafficking  - narcotráfico', 'no culpable', 'juramento', 'en libertad condicional'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 8'])
	lista[n].append(['dyj8'])
	lista[n].append(['on probation', 'pickpocket', 'pimp', 'prison', 'proof', 'prostitute', 'prostitution', 'punishment'])
	lista[n].append(['en libertad condicional', 'carterista', 'proxeneta', 'prisión', 'prueba', 'prostituta', 'prostitución', 'castigo'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 9'])
	lista[n].append(['dyj9'])
	lista[n].append(['ransom', 'rape', 'rapist', 'robber', 'robbery', 'shoplifter', 'shoplifting', 'smuggler'])
	lista[n].append(['dinero de rescate', 'violación sexual', 'violador', 'ladrón', 'hurto', 'ladrón de tiendas', 'hurto en tiendas', 'contrabandista'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 10'])
	lista[n].append(['dyj10'])
	lista[n].append(['smuggling', 'statement', 'Supreme Court', 'suspect', 'swindle', 'swindler', 'terrorism', 'terrorist'])
	lista[n].append(['contrabando', 'declaración', 'Suprema Corte', 'sospechoso', 'estafa', 'estafador', 'terrorismo', 'terrorista'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 11'])
	lista[n].append(['dyj11'])
	lista[n].append(['testimony', 'theft', 'thief', 'threat', 'to abduct', 'to accuse', 'to acquit', 'to arrest'])
	lista[n].append(['testimonio', 'robo', 'ladrón', 'amenaza', 'raptar, secuestrar', 'acusar', 'absolver', 'arrestar'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 12'])
	lista[n].append(['dyj12'])
	lista[n].append(['to assassinate', 'to assault', 'to be tried', 'to beat up', 'to blackmail', 'to bribe', 'to burgle', 'to convict'])
	lista[n].append(['asesinar (a un político)', 'agredir', 'ser juzgado', 'dar una paliza', 'chantajear', 'sobornar', 'hurtar', 'declarar culpable'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 13'])
	lista[n].append(['dyj13'])
	lista[n].append(['to defend', 'to drug', 'to fine', 'to forge', 'to imprison', 'to interrogate', 'to kidnap', 'to kill'])
	lista[n].append(['defender', 'drogar', 'multar', 'falsificar', 'encarcelar', 'interrogar', 'secuestrar', 'matar'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 14'])
	lista[n].append(['dyj14'])
	lista[n].append(['to lock up', 'to mug', 'to murder', 'to plead guilty', 'to poison', 'to prosecute', 'to rape', 'to release'])
	lista[n].append(['encerrar', 'atracar', 'asesinar', 'confesarse culpable', 'envenenar', 'procesar, enjuiciar', 'violar', 'poner en libertad'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 15'])
	lista[n].append(['dyj15'])
	lista[n].append(['to rob', 'to search', 'to sentence', 'to serve a sentence', 'to set fire', 'to shoot', 'to shoplift', 'to smuggle'])
	lista[n].append(['robar', 'registrar', 'sentenciar', 'cumplir una condena', 'incendiar', 'disparar', 'hurtar en tiendas', 'contrabandear'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 16'])
	lista[n].append(['dyj16'])
	lista[n].append(['to spy', 'to stab', 'to steal', 'to strangle', 'to surround', 'to swindle', 'to threaten', 'to vandalize'])
	lista[n].append(['espiar', 'apuñalar', 'robar', 'estrangular', 'rodear', 'estafar', 'amenazar', 'destrozar propiedad'])

	n = n+1
	lista.append([])
	lista[n].append(['delitos y justicia 17'])
	lista[n].append(['dyj17'])
	lista[n].append(['to violate', 'trial', 'vandal', 'vandalism', 'verdict', 'violation', 'violator', 'witness'])
	lista[n].append(['violar', 'juicio', 'vándalo', 'vandalismo', 'veredicto', 'violación', 'violador', 'testigo'])

	n = n+1
	lista.append([])
	lista[n].append(['militares y guerra 1'])
	lista[n].append(['myg1'])
	lista[n].append(['air force', 'allied forces', 'armed forces', 'army', 'artillery', 'attack', 'battery', 'battle'])
	lista[n].append(['fuerza aérea', 'fuerzas aliadas', 'fuerzas armadas', 'ejército', 'artillería', 'ataque', 'batería', 'batalla'])

	n = n+1
	lista.append([])
	lista[n].append(['militares y guerra 2'])
	lista[n].append(['myg2'])
	lista[n].append(['bomb', 'camouflage', 'captain', 'casualties', 'ceasefire', 'civilians', 'colonel', 'combat'])
	lista[n].append(['bomba', 'camuflaje', 'capitán', 'bajas de guerra', 'alto el fuego', 'civiles', 'coronel', 'combate'])

	n = n+1
	lista.append([])
	lista[n].append(['militares y guerra 3'])
	lista[n].append(['myg3'])
	lista[n].append(['commander', 'conflict', 'enemy', 'explosion', 'general', 'grenade', 'helicopter', 'hostilities'])
	lista[n].append(['comandante', 'conflicto', 'enemigo', 'explosión', 'general', 'granada', 'helicóptero', 'hostilidades'])

	n = n+1
	lista.append([])
	lista[n].append(['militares y guerra 4'])
	lista[n].append(['myg4'])
	lista[n].append(['human rights', 'humanitarian aid', 'injured', 'invasion', 'lieutenant', 'military', 'military base', 'military intelligence'])
	lista[n].append(['derechos humanos', 'ayuda humanitaria', 'herido', 'invasión', 'teniente', 'militar', 'base militar', 'inteligencia militar'])

	n = n+1
	lista.append([])
	lista[n].append(['militares y guerra 5'])
	lista[n].append(['myg5'])
	lista[n].append(['mine', 'minefield', 'missile', 'navy', 'patrol', 'peace', 'pilot', 'prisoner'])
	lista[n].append(['mina', 'campo minado', 'misil', 'marina', 'patrulla', 'paz', 'piloto', 'prisionero'])

	n = n+1
	lista.append([])
	lista[n].append(['militares y guerra 6'])
	lista[n].append(['myg6'])
	lista[n].append(['propaganda', 'resistance', 'sergeant', 'soldier', 'surveillance', 'tank', 'target', 'territory'])
	lista[n].append(['propaganda de guerra', 'resistencia', 'sargento', 'soldado', 'vigilancia', 'tanque', 'blanco, objetivo', 'territorio'])

	n = n+1
	lista.append([])
	lista[n].append(['militares y guerra 7'])
	lista[n].append(['myg7'])
	lista[n].append(['terrorist', 'to attack', 'to bomb', 'to defeat', 'to defend', 'to invade', 'to kill', 'to shoot'])
	lista[n].append(['terrorista', 'atacar', 'bombardear', 'derrotar', 'defender', 'invadir', 'matar', 'disparar'])

	n = n+1
	lista.append([])
	lista[n].append(['militares y guerra 8'])
	lista[n].append(['myg8'])
	lista[n].append(['to wound', 'trench', 'troops', 'war', 'weapons'])
	lista[n].append(['herir', 'trinchera', 'tropas', 'guerra', 'armas'])

	n = n+1
	lista.append([])
	lista[n].append(['armas 1'])
	lista[n].append(['a1'])
	lista[n].append(['aircraftcarrier', 'airgun', 'ammunition', 'battleship', 'bazooka', 'blowgun', 'bomb', 'bomber'])
	lista[n].append(['portaviones', 'rifle de aire', 'miniciones', 'barco de guerra', 'bazooka', 'cervatana', 'bomba', 'avión bombardero'])

	n = n+1
	lista.append([])
	lista[n].append(['armas 2'])
	lista[n].append(['a2'])
	lista[n].append(['boomerang', 'bow and arrow', 'bullet', 'cannon', 'crossbow', 'dagger', 'fighter plane', 'flamethrower'])
	lista[n].append(['bumerán', 'arco y flecha', 'bala', 'cañón', 'ballesta', 'daga', 'avión caza', 'lanzallamas'])

	n = n+1
	lista.append([])
	lista[n].append(['armas 3'])
	lista[n].append(['a3'])
	lista[n].append(['grenade', 'gun', 'knife', 'machinegun', 'mine', 'missile', 'mortar', 'pistol'])
	lista[n].append(['granada', 'pistola', 'cuchillo', 'ametralladora', 'mina', 'misíl', 'mortero', 'pistola'])

	n = n+1
	lista.append([])
	lista[n].append(['armas 4'])
	lista[n].append(['a4'])
	lista[n].append(['rifle', 'rocket', 'rocket launcher', 'shotgun', 'sling', 'spear', 'submarine', 'sword'])
	lista[n].append(['fusil', 'cohete', 'lanzacohetes', 'escopeta', 'onda', 'lanza', 'submarino', 'espada'])

	n = n+1
	lista.append([])
	lista[n].append(['armas 5'])
	lista[n].append(['a5'])
	lista[n].append(['tank', 'warship'])
	lista[n].append(['tanque', 'barco de guerra'])

	n = n+1
	lista.append([])
	lista[n].append(['nacionalidades 1'])
	lista[n].append(['n1'])
	lista[n].append(['Afghan', 'American', 'Argentinian', 'Australian', 'Austrian', 'Belgian', 'Bolivian', 'Brazilian'])
	lista[n].append(['Afgano', 'Americano', 'Argentino', 'Australiano', 'Austríaco', 'Belga', 'Boliviano', 'Brasileño'])

	n = n+1
	lista.append([])
	lista[n].append(['nacionalidades 2'])
	lista[n].append(['n2'])
	lista[n].append(['British', 'Bulgarian', 'Canadian', 'Chilean', 'Chinese', 'Colombian', 'Costa Rican', 'Cuban'])
	lista[n].append(['Británico', 'Búlgaro', 'Canadiense', 'Chileno', 'Chino', 'Colombiano', 'Costarricense', 'Cubano'])

	n = n+1
	lista.append([])
	lista[n].append(['nacionalidades 3'])
	lista[n].append(['n3'])
	lista[n].append(['Czech', 'Danish', 'Dominican', 'Dutch', 'Ecuadorean', 'Egyptian', 'English', 'Filipino'])
	lista[n].append(['Checo', 'Danés', 'Dominicano', 'Holandés', 'Ecuadorean', 'Egipcio', 'inglés', 'Filipino'])

	n = n+1
	lista.append([])
	lista[n].append(['nacionalidades 4'])
	lista[n].append(['n4'])
	lista[n].append(['Finnish', 'French', 'German', 'Greek', 'Greenlander', 'Guatemalan', 'Haitian', 'Hawaiian'])
	lista[n].append(['Finlandés', 'Francés', 'Alemán', 'Griego', 'Groenlandés', 'Guatemalteco', 'Haitiano', 'Hawaiano'])

	n = n+1
	lista.append([])
	lista[n].append(['nacionalidades 5'])
	lista[n].append(['n5'])
	lista[n].append(['Honduran', 'Hungarian', 'Icelandic', 'Indian', 'Indonesian', 'Iranian', 'Iraqui', 'Irish'])
	lista[n].append(['Hondureño', 'Húngaro', 'Islandés', 'Indio', 'Indonesio', 'Iraní', 'Iraqui', 'Irlandés'])

	n = n+1
	lista.append([])
	lista[n].append(['nacionalidades 6'])
	lista[n].append(['n6'])
	lista[n].append(['Israeli', 'Italian', 'Jamaican', 'Japanese', 'korean', 'Lebanese', 'Malaysian', 'Maltese'])
	lista[n].append(['Israelí', 'Italiano', 'Jamaicano', 'Japonés', 'coreano', 'Libanés', 'Malasio', 'Maltés'])

	n = n+1
	lista.append([])
	lista[n].append(['nacionalidades 7'])
	lista[n].append(['n7'])
	lista[n].append(['Mexican', 'Moroccan', 'Nepalese', 'New Zealander', 'Nicaraguan', 'Nigerian', 'Norwegian', 'Pakistani'])
	lista[n].append(['Mejicano', 'Marroquí', 'Nepalés', 'Neozelandés', 'Nicaragüense', 'Nigeriano', 'Noruego', 'Paquistaní'])

	n = n+1
	lista.append([])
	lista[n].append(['nacionalidades 8'])
	lista[n].append(['n8'])
	lista[n].append(['Palestinian', 'Panamanian', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Puerto Rican', 'Rumanian'])
	lista[n].append(['Palestino', 'Panameño', 'Paraguayo', 'Peruano', 'Polaco', 'Portugués', 'Puertorriqueño', 'Rumano'])

	n = n+1
	lista.append([])
	lista[n].append(['nacionalidades 9'])
	lista[n].append(['n9'])
	lista[n].append(['Russian', 'Saudi Arabian', 'Scottish', 'Singaporean', 'Spanish', 'Swedish', 'Swiss', 'Syrian'])
	lista[n].append(['Ruso', 'Saudita', 'Escocés', 'Singaporean', 'Español', 'Sueco', 'Suizo', 'Sirio'])

	n = n+1
	lista.append([])
	lista[n].append(['nacionalidades 10'])
	lista[n].append(['n10'])
	lista[n].append(['Tahitian', 'Thai', 'Tunisian', 'Turkish', 'Ukrainian', 'Uruguayan', 'Venezuelan', 'Vietnamese'])
	lista[n].append(['Tahitiano', 'Tailandés', 'Tunecino', 'Turco', 'Ucraniano', 'Uruguayo', 'Venezolano', 'Vietnamita'])

	n = n+1
	lista.append([])
	lista[n].append(['nacionalidades 11'])
	lista[n].append(['n11'])
	lista[n].append(['Welsh', 'Yugoslavian'])
	lista[n].append(['Galés', 'Yugoslavo'])

	n = n+1
	lista.append([])
	lista[n].append(['política y gobierno 1'])
	lista[n].append(['pyg1'])
	lista[n].append(['ballot', 'bill', 'budget', 'bureaucracy', 'cabinet', 'campaign', 'candidate', 'capitalist'])
	lista[n].append(['votación', 'proyecto de ley', 'presupuesto', 'burocracia', 'gabinete', 'campaña', 'candidato', 'capitalista'])

	n = n+1
	lista.append([])
	lista[n].append(['política y gobierno 2'])
	lista[n].append(['pyg2'])
	lista[n].append(['centrist', 'citizen', 'civil servant', 'coalition', 'colonialist', 'communist', 'congress', 'congressman'])
	lista[n].append(['del centro', 'ciudadano', 'empleado público', 'coalición', 'colonialista', 'comunista', 'congreso', 'congresista'])

	n = n+1
	lista.append([])
	lista[n].append(['política y gobierno 3'])
	lista[n].append(['pyg3'])
	lista[n].append(['Conservative Party', 'democracy', 'democrat', 'democratic', 'Democratic Party', 'dictator', 'electoral roll', 'electorate'])
	lista[n].append(['partido conservador', 'democracia', 'demócrata', 'democrático', 'partido demócrata', 'dictador', 'padrón electoral', 'electorado'])

	n = n+1
	lista.append([])
	lista[n].append(['política y gobierno 4'])
	lista[n].append(['pyg4'])
	lista[n].append(['fascist', 'government', 'ideology', 'imperialist', 'Labour Party', 'law', 'left', 'legislature'])
	lista[n].append(['fascista', 'gobierno', 'ideología', 'imperialista', 'partido laborista', 'ley', 'wing  - de izquierda', 'legislatura'])

	n = n+1
	lista.append([])
	lista[n].append(['política y gobierno 5'])
	lista[n].append(['pyg5'])
	lista[n].append(['liberal', 'minister', 'ministry', 'monarchy', 'nationalist', 'opposition', 'parliament', 'party'])
	lista[n].append(['liberal', 'ministro', 'ministerio', 'monarquía', 'nacionalista', 'oposición', 'parlamento', 'partido'])

	n = n+1
	lista.append([])
	lista[n].append(['política y gobierno 6'])
	lista[n].append(['pyg6'])
	lista[n].append(['policy', 'political', 'politician', 'politics', 'poll', 'president', 'referendum', 'republic'])
	lista[n].append(['política, plan de acción', 'político (adjetivo)', 'político (persona)', 'política', 'encuesta, votación', 'presidente', 'referendum', 'república'])

	n = n+1
	lista.append([])
	lista[n].append(['política y gobierno 7'])
	lista[n].append(['pyg7'])
	lista[n].append(['republican', 'Republican Party', 'right', 'rights', 'senate', 'senator', 'social pressure', 'socialist'])
	lista[n].append(['republicano', 'partido republicano', 'wing  - de derecha', 'derechos', 'senado', 'senador', 'presión social', 'socialista'])

	n = n+1
	lista.append([])
	lista[n].append(['política y gobierno 8'])
	lista[n].append(['pyg8'])
	lista[n].append(['suffrage', 'supreme court', 'taxes', 'to elect', 'to govern', 'to run for president', 'to vote', 'voter'])
	lista[n].append(['sufragio', 'corte suprema', 'impuestos', 'elegir', 'gobernar', 'ser candidato a presidente', 'votar', 'votante'])

	n = n+1
	lista.append([])
	lista[n].append(['religión 1'])
	lista[n].append(['r1'])
	lista[n].append(['altar', 'apostle', 'archbishop', 'atheism', 'baptism', 'bible', 'bishop', 'cardinal'])
	lista[n].append(['altar', 'apóstol', 'arzobispo', 'ateísmo', 'bautismo', 'biblia', 'obispo', 'cardenal'])

	n = n+1
	lista.append([])
	lista[n].append(['religión 2'])
	lista[n].append(['r2'])
	lista[n].append(['cathedral', 'cemetery', 'chapel', 'chaplain', 'charity', 'choir', 'church', 'clergy'])
	lista[n].append(['catedral', 'cementerio', 'capilla', 'capellán', 'caridad', 'coro', 'iglesia', 'clero'])

	n = n+1
	lista.append([])
	lista[n].append(['religión 3'])
	lista[n].append(['r3'])
	lista[n].append(['confession', 'convent', 'cult', 'deacon', 'demon', 'disciple', 'faith', 'God'])
	lista[n].append(['confesión', 'convento', 'culto', 'diácono', 'demonio', 'discípulo', 'fe', 'Dios'])

	n = n+1
	lista.append([])
	lista[n].append(['religión 4'])
	lista[n].append(['r4'])
	lista[n].append(['gospel', 'heaven', 'hell', 'mass', 'miracle', 'monastery', 'monk', 'mosque'])
	lista[n].append(['evangelio', 'cielo', 'infierno', 'misa', 'milagro', 'monasterio', 'monje', 'mezquita'])

	n = n+1
	lista.append([])
	lista[n].append(['religión 5'])
	lista[n].append(['r5'])
	lista[n].append(['nun', 'parable', 'paradise', 'pastor', 'pilgrim', 'pope', 'prayer', 'priest'])
	lista[n].append(['monja', 'parábola', 'paraíso', 'pastor', 'peregrino', 'papa', 'oración', 'cura'])

	n = n+1
	lista.append([])
	lista[n].append(['religión 6'])
	lista[n].append(['r6'])
	lista[n].append(['procession', 'prophet', 'psalm', 'purgatory', 'rabbi', 'sacrilege', 'saint', 'sermon'])
	lista[n].append(['procesión', 'profeta', 'salmo', 'purgatorio', 'rabino', 'sacrilegio', 'santo', 'sermón'])

	n = n+1
	lista.append([])
	lista[n].append(['religión 7'])
	lista[n].append(['r7'])
	lista[n].append(['shrine', 'sin', 'sinner', 'soul', 'synagogue', 'temple', 'temptation', 'the devil'])
	lista[n].append(['santuario', 'pecado', 'pecador', 'alma', 'sinagoga', 'templo', 'tentación', 'el diablo'])

	n = n+1
	lista.append([])
	lista[n].append(['religión 8'])
	lista[n].append(['r8'])
	lista[n].append(['The Holy Spirit', 'vicar', 'worship'])
	lista[n].append(['El Espíritu Santo', 'vicario', 'adoración'])

	n = n+1
	lista.append([])
	lista[n].append(['escuela y educación 1'])
	lista[n].append(['eye1'])
	lista[n].append(['algebra', 'backpack', 'binder', 'biology', 'boarding school', 'book', 'break', 'cafeteria'])
	lista[n].append(['álgebra', 'mochila', 'carpeta', 'biología', 'internado', 'libro', 'recreo', 'cafetería'])

	n = n+1
	lista.append([])
	lista[n].append(['escuela y educación 2'])
	lista[n].append(['eye2'])
	lista[n].append(['calculator', 'calendar', 'chalk', 'chalkboard', 'chemistry', 'choir', 'class', 'classmate'])
	lista[n].append(['calculadora', 'calendario', 'tiza', 'pizarrón', 'química', 'coro', 'clase', 'compañero de clase'])

	n = n+1
	lista.append([])
	lista[n].append(['escuela y educación 3'])
	lista[n].append(['eye3'])
	lista[n].append(['classroom', 'computer science', 'counselor', 'course', 'crayon', 'degree', 'desk', 'diploma'])
	lista[n].append(['aula', 'computación', 'consejero', 'curso', 'crayón', 'título, licenciatura', 'escritorio', 'diploma'])

	n = n+1
	lista.append([])
	lista[n].append(['escuela y educación 4'])
	lista[n].append(['eye4'])
	lista[n].append(['dorm', 'elementary school', 'encyclopedia', 'eraser', 'exam', 'faculty', 'geometry', 'globe'])
	lista[n].append(['residencia para estudiantes', 'escuela primaria', 'enciclopedia', 'borrador', 'examen', 'profesorado', 'geometría', 'globo terráqueo'])

	n = n+1
	lista.append([])
	lista[n].append(['escuela y educación 5'])
	lista[n].append(['eye5'])
	lista[n].append(['grade', 'gym', 'gym teacher', 'high school', 'history', 'hole punch', 'homework', 'kindergarten'])
	lista[n].append(['calificación', 'gimnasio', 'profesor de gimnasia', 'escuela secundaria', 'historia', 'perforadora', 'tarea', 'jardín de infantes'])

	n = n+1
	lista.append([])
	lista[n].append(['escuela y educación 6'])
	lista[n].append(['eye6'])
	lista[n].append(['lab', 'library', 'locker', 'map', 'marker', 'math', 'notebook', 'pen'])
	lista[n].append(['laboratorio', 'biblioteca', 'armario', 'mapa', 'marcador', 'matemáticas', 'cuaderno', 'bolígrafo'])

	n = n+1
	lista.append([])
	lista[n].append(['escuela y educación 7'])
	lista[n].append(['eye7'])
	lista[n].append(['pencil', 'pencil sharpener', 'playground', 'poster', 'principal', 'private classes', 'professor', 'quiz'])
	lista[n].append(['lápiz', 'sacapuntas', 'patio', 'cartel', 'director de escuela', 'clases particulares', 'profesor', 'prueba, test'])

	n = n+1
	lista.append([])
	lista[n].append(['escuela y educación 8'])
	lista[n].append(['eye8'])
	lista[n].append(['ruler', 'scholarship', 'science', 'scissors', 'semester', 'stapler', 'student', 'subject'])
	lista[n].append(['regla', 'beca', 'ciencia', 'tijeras', 'semestre', 'grapadora', 'alumno', 'materia, asignatura'])

	n = n+1
	lista.append([])
	lista[n].append(['escuela y educación 9'])
	lista[n].append(['eye9'])
	lista[n].append(['tape', 'teacher', 'test', 'vacation'])
	lista[n].append(['cinta adhesiva', 'maestro, profesor', 'examen, prueba', 'vacaciones'])

	n = n+1
	lista.append([])
	lista[n].append(['colores y patrones 1'])
	lista[n].append(['cyp1'])
	lista[n].append(['aquamarine', 'black', 'blue', 'brown', 'checked', 'chestnut', 'coral', 'crimson'])
	lista[n].append(['aguamarina', 'negro', 'azul', 'marrón', 'a cuadros', 'castaño', 'coral', 'púrpura'])

	n = n+1
	lista.append([])
	lista[n].append(['colores y patrones 2'])
	lista[n].append(['cyp2'])
	lista[n].append(['dark', 'dark green', 'dotted', 'dull', 'flowered', 'fuchsia', 'golden', 'gray'])
	lista[n].append(['oscuro', 'verde oscuro', 'a lunares', 'apagado', 'floreado', 'fucsia', 'dorado', 'gris'])

	n = n+1
	lista.append([])
	lista[n].append(['colores y patrones 3'])
	lista[n].append(['cyp3'])
	lista[n].append(['green', 'indigo', 'lavender', 'light', 'loud', 'maroon', 'mauve', 'navy blue'])
	lista[n].append(['verde', 'índigo', 'lavanda', 'claro', 'chillón', 'bordó', 'lila', 'azul marino'])

	n = n+1
	lista.append([])
	lista[n].append(['colores y patrones 4'])
	lista[n].append(['cyp4'])
	lista[n].append(['ochre', 'olive', 'opaque', 'orange', 'pale', 'peach', 'pink', 'plain'])
	lista[n].append(['ocre', 'oliva', 'opaco', 'anaranjado', 'pálido', 'durazno', 'rosado', 'liso'])

	n = n+1
	lista.append([])
	lista[n].append(['colores y patrones 5'])
	lista[n].append(['cyp5'])
	lista[n].append(['printed', 'purple', 'red', 'scarlet', 'shiny', 'silver', 'sky blue', 'striped'])
	lista[n].append(['estampado', 'morado', 'rojo', 'rojo escarlata', 'brillante', 'plata', 'celeste', 'a rayas'])

	n = n+1
	lista.append([])
	lista[n].append(['colores y patrones 6'])
	lista[n].append(['cyp6'])
	lista[n].append(['teal', 'transparent', 'turquoise', 'violet', 'white', 'yellow'])
	lista[n].append(['verde azulado', 'transparente', 'turquesa', 'violeta', 'blanco', 'amarillo'])

	n = n+1
	lista.append([])
	lista[n].append(['envases y cantidades 1'])
	lista[n].append(['eyc1'])
	lista[n].append(['a dozen', 'a half', 'a handful', 'a heap', 'a mouthful', 'a pair', 'a piece', 'a quarter'])
	lista[n].append(['una docena', 'una mitad', 'un puñado', 'un montón', 'un bocado', 'un par', 'un pedazo', 'un cuarto'])

	n = n+1
	lista.append([])
	lista[n].append(['envases y cantidades 2'])
	lista[n].append(['eyc2'])
	lista[n].append(['a slice', 'a spoonful', 'a stack', 'an armful', 'bag', 'bar', 'barrel', 'basket'])
	lista[n].append(['una rebanada', 'una cucharada', 'una pila, un montón', 'una brazada', 'bolsita', 'barra', 'barril', 'canasta'])

	n = n+1
	lista.append([])
	lista[n].append(['envases y cantidades 3'])
	lista[n].append(['eyc3'])
	lista[n].append(['bottle', 'bowl', 'box', 'bucket', 'can', 'carton', 'crate', 'envelope'])
	lista[n].append(['botella', 'bol', 'caja', 'balde, cubo', 'lata', 'cartón', 'cajón', 'sobre de carta'])

	n = n+1
	lista.append([])
	lista[n].append(['envases y cantidades 4'])
	lista[n].append(['eyc4'])
	lista[n].append(['gallon', 'glass', 'gramme', 'half a dozen', 'jar', 'jug', 'kilo', 'liter'])
	lista[n].append(['galón', 'vaso', 'gramo', 'media docena', 'frasco, pote', 'jarro', 'kilo', 'litro'])

	n = n+1
	lista.append([])
	lista[n].append(['envases y cantidades 5'])
	lista[n].append(['eyc5'])
	lista[n].append(['mug', 'ounce', 'pack', 'package', 'pint', 'pot', 'pound', 'roll'])
	lista[n].append(['jarra', 'onza', 'paquete, cajetilla', 'paquete', 'pinta', 'tarro, pote', 'libra', 'rollo'])

	n = n+1
	lista.append([])
	lista[n].append(['envases y cantidades 6'])
	lista[n].append(['eyc6'])
	lista[n].append(['sachet', 'sack', 'six', 'spray can', 'ton', 'tube'])
	lista[n].append(['sachet', 'saco, costal', 'pack  - paquete de seis', 'aerosol, atomizador', 'tonelada', 'tubo, pomo'])

	n = n+1
	lista.append([])
	lista[n].append(['materiales y telas 1'])
	lista[n].append(['myt1'])
	lista[n].append(['acrylic', 'aluminium', 'brass', 'bronze', 'canvas', 'cardboard', 'cashmere', 'cement'])
	lista[n].append(['acrílico', 'aluminio', 'latón', 'bronce', 'lona', 'cartón', 'cachemira', 'cemento'])

	n = n+1
	lista.append([])
	lista[n].append(['materiales y telas 2'])
	lista[n].append(['myt2'])
	lista[n].append(['clay', 'concrete', 'copper', 'corduroy', 'cotton', 'denim', 'feather', 'fiberglass'])
	lista[n].append(['arcilla', 'hormigón', 'cobre', 'corderoy', 'algodón', 'tela de jean', 'pluma', 'fibra de vidrio'])

	n = n+1
	lista.append([])
	lista[n].append(['materiales y telas 3'])
	lista[n].append(['myt3'])
	lista[n].append(['flannel', 'gauze', 'glass', 'gold', 'iron', 'lace', 'lead', 'leather'])
	lista[n].append(['franela', 'gasa', 'vidrio', 'oro', 'hierro', 'encaje', 'plomo', 'cuero'])

	n = n+1
	lista.append([])
	lista[n].append(['materiales y telas 4'])
	lista[n].append(['myt4'])
	lista[n].append(['leather', 'linen', 'marble', 'nylon', 'paper', 'plaster', 'plastic', 'plywood'])
	lista[n].append(['cuero', 'lino', 'mármol', 'nylon', 'papel', 'yeso', 'plástico', 'aglomerado'])

	n = n+1
	lista.append([])
	lista[n].append(['materiales y telas 5'])
	lista[n].append(['myt5'])
	lista[n].append(['polyester', 'porcelain', 'pottery', 'rayon', 'rubber', 'silk', 'silver', 'steel'])
	lista[n].append(['poliéster', 'porcelana', 'cerámica', 'rayón', 'goma', 'seda', 'plata', 'acero'])

	n = n+1
	lista.append([])
	lista[n].append(['materiales y telas 6'])
	lista[n].append(['myt6'])
	lista[n].append(['stone', 'straw', 'suede', 'tin', 'velvet', 'wax', 'wood', 'wool'])
	lista[n].append(['piedra', 'paja', 'gamuza', 'estaño, hojalata', 'terciopelo', 'cera', 'madera', 'lana'])

	n = n+1
	lista.append([])
	lista[n].append(['materiales y telas 7'])
	lista[n].append(['myt7'])
	lista[n].append(['zinc'])
	lista[n].append(['cinc'])

	n = n+1
	lista.append([])
	lista[n].append(['formas y texturas 1'])
	lista[n].append(['fyt1'])
	lista[n].append(['circle', 'circular', 'concave', 'cone', 'conical', 'convex', 'cube', 'cubic'])
	lista[n].append(['círculo', 'circular', 'cóncavo', 'cono', 'cónico', 'convexo', 'cubo', 'cúbico'])

	n = n+1
	lista.append([])
	lista[n].append(['formas y texturas 2'])
	lista[n].append(['fyt2'])
	lista[n].append(['cylinder', 'cylindrical', 'hexagon', 'hexagonal', 'hollow', 'octagon', 'octagonal', 'oval'])
	lista[n].append(['cilindro', 'cilíndrico', 'hexágono', 'hexagonal', 'hueco', 'octógono', 'octogonal', 'óvalo, ovalado'])

	n = n+1
	lista.append([])
	lista[n].append(['formas y texturas 3'])
	lista[n].append(['fyt3'])
	lista[n].append(['pentagon', 'pentagonal', 'polygon', 'pyramid', 'pyramidal', 'rectangle', 'rectangular', 'rhombus'])
	lista[n].append(['pentágono', 'pentagonal', 'polígono', 'pirámide', 'piramidal', 'rectángulo', 'rectangular', 'rombo'])

	n = n+1
	lista.append([])
	lista[n].append(['formas y texturas 4'])
	lista[n].append(['fyt4'])
	lista[n].append(['rhombus', 'solid', 'sphere', 'spherical', 'spiral', 'square', 'triangle', 'triangular'])
	lista[n].append(['shaped  - romboidal', 'sólido', 'esfera', 'esférico', 'espiral', 'cuadrado', 'triángulo', 'triangular'])

	n = n+1
	lista.append([])
	lista[n].append(['calendario y tiempo 1'])
	lista[n].append(['cyt1'])
	lista[n].append(['afternoon', 'April', 'August', 'century', 'day', 'decade', 'December', 'early morning'])
	lista[n].append(['la tarde', 'abril', 'agosto', 'siglo', 'día', 'década', 'diciembre', 'madrugada'])

	n = n+1
	lista.append([])
	lista[n].append(['calendario y tiempo 2'])
	lista[n].append(['cyt2'])
	lista[n].append(['era', 'eternity', 'evening', 'fall / autumn', 'February', 'Friday', 'hour', 'January'])
	lista[n].append(['era, época', 'eternidad', 'noche', 'otoño', 'febrero', 'viernes', 'hora', 'enero'])

	n = n+1
	lista.append([])
	lista[n].append(['calendario y tiempo 3'])
	lista[n].append(['cyt3'])
	lista[n].append(['July', 'June', 'March', 'May', 'midnight', 'millennium', 'minute', 'Monday'])
	lista[n].append(['julio', 'junio', 'marzo', 'mayo', 'medianoche', 'milenio', 'minuto', 'lunes'])

	n = n+1
	lista.append([])
	lista[n].append(['calendario y tiempo 4'])
	lista[n].append(['cyt4'])
	lista[n].append(['month', 'morning', 'night', 'noon', 'November', 'October', 'Saturday', 'second'])
	lista[n].append(['mes', 'mañana', 'noche', 'mediodía', 'noviembre', 'octubre', 'sábado', 'segundo'])

	n = n+1
	lista.append([])
	lista[n].append(['calendario y tiempo 5'])
	lista[n].append(['cyt5'])
	lista[n].append(['September', 'summer', 'Sunday', 'sunrise', 'sunset', 'Thursday', 'Tuesday', 'Wednesday'])
	lista[n].append(['septiembre', 'verano', 'domingo', 'amanecer', 'atardecer', 'jueves', 'martes', 'miércoles'])

	n = n+1
	lista.append([])
	lista[n].append(['calendario y tiempo 6'])
	lista[n].append(['cyt6'])
	lista[n].append(['week', 'winter', 'year'])
	lista[n].append(['semana', 'invierno', 'año'])

	n = n+1
	lista.append([])
	lista[n].append(['puntos en el tiempo 1'])
	lista[n].append(['peet1'])
	lista[n].append(['at dawn', 'at dusk', 'at midnight', 'at night', 'at noon', 'every week', 'in a week', 'in the afternoon'])
	lista[n].append(['al amanecer', 'al atardecer', 'a medianoche', 'de noche', 'al mediodía', 'todas las semanas', 'dentro de una semana', 'por la tarde'])

	n = n+1
	lista.append([])
	lista[n].append(['puntos en el tiempo 2'])
	lista[n].append(['peet2'])
	lista[n].append(['in the early morning', 'in the evening', 'in the morning', 'last Friday', 'last month', 'last night', 'last week', 'last year'])
	lista[n].append(['por la madrugada', 'por la noche', 'por la mañana', 'el viernes pasado', 'el mes pasado', 'anoche', 'la semana pasada', 'el año pasado'])

	n = n+1
	lista.append([])
	lista[n].append(['puntos en el tiempo 3'])
	lista[n].append(['peet3'])
	lista[n].append(['next Friday', 'next week', 'next year', 'the day after', 'the day after tomorrow', 'the day before', 'the day before yesterday', 'this evening'])
	lista[n].append(['el viernes que viene', 'la semana que viene', 'el año que viene', 'el día siguiente', 'pasado mañana', 'el día antes', 'anteayer', 'esta noche'])

	n = n+1
	lista.append([])
	lista[n].append(['puntos en el tiempo 4'])
	lista[n].append(['peet4'])
	lista[n].append(['this Friday', 'this month', 'this week', 'this year', 'three weeks ago', 'today', 'tomorrow', 'tomorrow afternoon'])
	lista[n].append(['este viernes', 'este mes', 'esta semana', 'este año', 'hace tres semanas', 'hoy', 'mañana', 'mañana por la tarde'])

	n = n+1
	lista.append([])
	lista[n].append(['puntos en el tiempo 5'])
	lista[n].append(['peet5'])
	lista[n].append(['tomorrow evening', 'tomorrow morning', 'tonight', 'two days ago', 'two days earlier', 'two days later', 'yesterday', 'yesterday evening'])
	lista[n].append(['mañana por la noche', 'mañana por la mañana', 'esta noche', 'hace dos días', 'dos días antes', 'dos días después', 'ayer', 'ayer por la noche'])

	n = n+1
	lista.append([])
	lista[n].append(['puntos en el tiempo 6'])
	lista[n].append(['peet6'])
	lista[n].append(['yesterday morning'])
	lista[n].append(['ayer por la mañana'])

	n = n+1
	lista.append([])
	lista[n].append(['aeropuerto y aviones 1'])
	lista[n].append(['aya1'])
	lista[n].append(['air hostess', 'airline', 'airport', 'aisle', 'arrivals', 'baggage', 'baggage claim', 'boarding pass'])
	lista[n].append(['azafata', 'compañía aérea', 'aeropuerto', 'pasillo', 'llegadas', 'equipaje', 'reclamo de equipaje', 'tarjeta de embarque'])

	n = n+1
	lista.append([])
	lista[n].append(['aeropuerto y aviones 2'])
	lista[n].append(['aya2'])
	lista[n].append(['carry', 'cart', 'check', 'cockpit', 'connecting flight', 'control tower', 'crew', 'customs'])
	lista[n].append(['on luggage  - equipaje de mano', 'carrito, carretilla', 'in  - registración', 'cabina', 'conexión', 'torre de control', 'tripulación', 'aduana'])

	n = n+1
	lista.append([])
	lista[n].append(['aeropuerto y aviones 3'])
	lista[n].append(['aya3'])
	lista[n].append(['delayed', 'departure lounge', 'departures', 'destination', 'domestic flight', 'duty free', 'emergency exit', 'emergency landing'])
	lista[n].append(['demorado', 'sala de espera', 'salidas', 'destino', 'vuelo de cabotaje', 'libre de impuestos', 'salida de emergencia', 'aterrizaje de emergencia'])

	n = n+1
	lista.append([])
	lista[n].append(['aeropuerto y aviones 4'])
	lista[n].append(['aya4'])
	lista[n].append(['excess baggage', 'flight attendant', 'flight number', 'gate', 'immigration', 'international flight', 'jet lag', 'landing'])
	lista[n].append(['exceso de equipaje', 'auxiliar de vuelo', 'número de vuelo', 'puerta', 'inmigración', 'vuelo internacional', 'descompensación por la diferencia horaria', 'aterrizaje'])

	n = n+1
	lista.append([])
	lista[n].append(['aeropuerto y aviones 5'])
	lista[n].append(['aya5'])
	lista[n].append(['life vest', 'loudspeakers', 'luggage', 'luggage compartment', 'meal tray', 'non', 'on schedule', 'one'])
	lista[n].append(['chaleco salvavidas', 'altoparlantes', 'equipaje', 'compartimiento para equipaje', 'bandeja de comida', 'stop flight  - vuelo directo', 'en horario', 'way trip  - viaje de ida'])

	n = n+1
	lista.append([])
	lista[n].append(['aeropuerto y aviones 6'])
	lista[n].append(['aya6'])
	lista[n].append(['overweight', 'passenger', 'passport', 'pilot', 'plane', 'restrooms', 'round trip ticket', 'row'])
	lista[n].append(['sobrepeso', 'pasajero', 'pasaporte', 'piloto', 'avión', 'sanitarios', 'pasaje de ida y vuelta', 'fila'])

	n = n+1
	lista.append([])
	lista[n].append(['aeropuerto y aviones 7'])
	lista[n].append(['aya7'])
	lista[n].append(['runway', 'scales', 'seat', 'seat belt', 'security check', 'shuttle', 'steward', 'stewardess'])
	lista[n].append(['pista', 'balanza', 'asiento', 'cinturón de seguridad', 'control de seguridad', 'autobús transbordador', 'auxiliar de vuelo', 'azafata'])

	n = n+1
	lista.append([])
	lista[n].append(['aeropuerto y aviones 8'])
	lista[n].append(['aya8'])
	lista[n].append(['stopover', 'takeoff', 'timetable', 'to board', 'to land', 'to take off', 'travel agency', 'visa'])
	lista[n].append(['escala', 'despegue', 'listado de horarios', 'embarcar', 'aterrizar', 'despegar', 'agencia de viajes', 'visa'])

	n = n+1
	lista.append([])
	lista[n].append(['medios de transporte 1'])
	lista[n].append(['mdt1'])
	lista[n].append(['airliner', 'airplane', 'bicycle', 'bike', 'boat', 'bus', 'canoe', 'car'])
	lista[n].append(['avión de pasajeros', 'avión', 'bicicleta', 'bici', 'barco, buque', 'colectivo', 'canoa, piragua', 'auto, carro'])

	n = n+1
	lista.append([])
	lista[n].append(['medios de transporte 2'])
	lista[n].append(['mdt2'])
	lista[n].append(['cruiser', 'ferry', 'glider', 'helicopter', 'hot air ballon', 'jet plane', 'moped', 'motorbike'])
	lista[n].append(['crusero', 'transbordador', 'planeador', 'helicóptero', 'globo aerostático', 'avión a reacción', 'ciclomotor', 'motocicleta'])

	n = n+1
	lista.append([])
	lista[n].append(['medios de transporte 3'])
	lista[n].append(['mdt3'])
	lista[n].append(['motorboat', 'ocean liner', 'pickup truck', 'raft', 'rocket', 'roller skates', 'sailboat', 'scooter'])
	lista[n].append(['lancha', 'transatlántico', 'camioneta', 'balza', 'cohete', 'patines', 'velero', 'escúter'])

	n = n+1
	lista.append([])
	lista[n].append(['medios de transporte 4'])
	lista[n].append(['mdt4'])
	lista[n].append(['ship', 'skateboard', 'streetcar', 'subway', 'taxi cab', 'train', 'truck', 'van'])
	lista[n].append(['buque, barco', 'monopatín, patineta', 'tranvía', 'tren subterráneo', 'taxi', 'tren', 'camión', 'furgoneta - traffic'])

	n = n+1
	lista.append([])
	lista[n].append(['medios de transporte 5'])
	lista[n].append(['mdt5'])
	lista[n].append(['wagon'])
	lista[n].append(['carro, carreta'])

	n = n+1
	lista.append([])
	lista[n].append(['el automóvil 1'])
	lista[n].append(['ea1'])
	lista[n].append(['air conditioning', 'antenna', 'back seat', 'battery', 'blinker', 'bodywork', 'brake', 'car chassis'])
	lista[n].append(['aire acondicionado', 'antena', 'asiento trasero', 'batería, acumulador', 'guiño, luz direccional', 'carrocería', 'freno', 'chasis'])

	n = n+1
	lista.append([])
	lista[n].append(['el automóvil 2'])
	lista[n].append(['ea2'])
	lista[n].append(['carburetor', 'clutch', 'dashboard', 'driving lights', 'engine', 'exhaust pipe', 'fan', 'fender'])
	lista[n].append(['carburador', 'embrague', 'tablero del auto', 'luces de posición', 'motor', 'caño de escape', 'ventilador', 'parachoques'])

	n = n+1
	lista.append([])
	lista[n].append(['el automóvil 3'])
	lista[n].append(['ea3'])
	lista[n].append(['front seat', 'fuel gauge', 'gas pedal', 'gas tank', 'gasoline', 'gear lever', 'glove compartment', 'handbrake'])
	lista[n].append(['asiento delantero', 'indicador de nafta', 'acelerador', 'tanque de nafta', 'combustible', 'palanca de cambios', 'guantera', 'freno de mano'])

	n = n+1
	lista.append([])
	lista[n].append(['el automóvil 4'])
	lista[n].append(['ea4'])
	lista[n].append(['headlights', 'hood', 'horn', 'hubcap', 'ignition', 'lever', 'mudguard', 'muffler'])
	lista[n].append(['faros', 'capot', 'bocina', 'tapa de la rueda', 'arranque', 'palanca', 'guardabarros', 'silenciador'])

	n = n+1
	lista.append([])
	lista[n].append(['el automóvil 5'])
	lista[n].append(['ea5'])
	lista[n].append(['odometer', 'oil gauge', 'oil pump', 'parking lights', 'plate', 'radiator', 'rear lights', 'rearview mirror'])
	lista[n].append(['contador de kilómetros', 'indicador de aceite', 'bomba de aceite', 'luces de posición', 'chapa, patente', 'radiador', 'luz trasera', 'espejo retrovisor'])

	n = n+1
	lista.append([])
	lista[n].append(['el automóvil 6'])
	lista[n].append(['ea6'])
	lista[n].append(['reverse', 'seat belt', 'shock absorber', 'side lights', 'side mirror', 'spare wheel', 'spark plug', 'speedometer'])
	lista[n].append(['marcha atrás', 'cinturón de seguridad', 'amortiguador', 'luces de posición', 'espejo lateral', 'rueda de auxilio', 'bujía', 'velocímetro'])

	n = n+1
	lista.append([])
	lista[n].append(['el automóvil 7'])
	lista[n].append(['ea7'])
	lista[n].append(['steering wheel', 'temperature gauge', 'tire', 'trunk', 'wheels', 'windshield', 'windshield wiper'])
	lista[n].append(['volante', 'indicador de temperatura', 'neumático, cubierta', 'baúl', 'ruedas', 'parabrisas', 'limpiaparabrisas'])

	n = n+1
	lista.append([])
	lista[n].append(['la bicicleta 1'])
	lista[n].append(['lb1'])
	lista[n].append(['ball bearing', 'bell', 'brake', 'brake handle', 'cable', 'carrier', 'chain', 'chain wheel'])
	lista[n].append(['cojinete de bolas', 'timbre', 'freno', 'palanca de freno', 'cable', 'portaequipajes', 'cadena', 'plato'])

	n = n+1
	lista.append([])
	lista[n].append(['la bicicleta 2'])
	lista[n].append(['lb2'])
	lista[n].append(['crossbar', 'cyclist', 'dynamo', 'engine', 'exhaust pipe', 'gearlever', 'grips', 'handlebar'])
	lista[n].append(['barra', 'ciclista', 'dínamo', 'motor', 'escape', 'palanca de velocidades', 'puños', 'manubrio, manillar'])

	n = n+1
	lista.append([])
	lista[n].append(['la bicicleta 3'])
	lista[n].append(['lb3'])
	lista[n].append(['helmet', 'horn', 'hub', 'inner tube', 'kick stand', 'lamp', 'lock', 'motorcycle'])
	lista[n].append(['casco', 'bocina', 'eje', 'cámara de aire', 'pie', 'faro', 'seguro, traba', 'motocicleta'])

	n = n+1
	lista.append([])
	lista[n].append(['la bicicleta 4'])
	lista[n].append(['lb4'])
	lista[n].append(['mudguard', 'patch', 'pedal', 'pump', 'puncture', 'rear light', 'reflector', 'rim'])
	lista[n].append(['guardabarros', 'parche', 'pedal', 'inflador', 'pinchazo', 'piloto', 'ojo de gato, catafaro', 'llanta'])

	n = n+1
	lista.append([])
	lista[n].append(['la bicicleta 5'])
	lista[n].append(['lb5'])
	lista[n].append(['saddle', 'scooter', 'shock absorbers', 'spoke', 'sprocket', 'tire', 'tricycle', 'valve'])
	lista[n].append(['sillín', 'motoneta', 'amortiguadores', 'rayo', 'piñón', 'neumático', 'triciclo', 'válvula'])

	n = n+1
	lista.append([])
	lista[n].append(['la bicicleta 6'])
	lista[n].append(['lb6'])
	lista[n].append(['wheel'])
	lista[n].append(['rueda'])

	n = n+1
	lista.append([])
	lista[n].append(['las embarcaciones 1'])
	lista[n].append(['le1'])
	lista[n].append(['aircraft carrier', 'barge', 'battle ship', 'boat', 'canoe', 'cargo boat', 'coast guard ship', 'cranes'])
	lista[n].append(['portaaviones', 'barcaza', 'acorazado', 'buque, navío', 'canoa', 'buque de carga', 'guardacostas', 'grúas'])

	n = n+1
	lista.append([])
	lista[n].append(['las embarcaciones 2'])
	lista[n].append(['le2'])
	lista[n].append(['cruise ship', 'cruiser', 'destroyer', 'dock', 'ferry', 'fishing boat', 'freighter', 'houseboat'])
	lista[n].append(['crucero de placer', 'crucero de la marina', 'destructor', 'dársena', 'transbordador', 'barco pesquero', 'carguero', 'casa flotante'])

	n = n+1
	lista.append([])
	lista[n].append(['las embarcaciones 3'])
	lista[n].append(['le3'])
	lista[n].append(['hovercraft', 'hydroplane', 'kayak', 'launch', 'lifeboat', 'liner', 'merchant ship', 'minerlayer'])
	lista[n].append(['aerodeslizador', 'hidroavión', 'kayac', 'lancha', 'bote salvavidas', 'transatlántico', 'barco mercante', 'minador'])

	n = n+1
	lista.append([])
	lista[n].append(['las embarcaciones 4'])
	lista[n].append(['le4'])
	lista[n].append(['minesweeper', 'motorboat', 'quay', 'rowing boat', 'sailing boat', 'ship', 'shipyard', 'skiff'])
	lista[n].append(['dragaminas', 'lancha', 'muelle', 'bote a remos', 'barco de vela, velero', 'buque, barco', 'astillero', 'esquife'])

	n = n+1
	lista.append([])
	lista[n].append(['las embarcaciones 5'])
	lista[n].append(['le5'])
	lista[n].append(['steamer', 'submarine', 'tanker', 'torpedo boat', 'training ship', 'tug boat', 'vessel', 'warship'])
	lista[n].append(['barco de vapor', 'submarino', 'petrolero', 'torpedero', 'barco-escuela', 'remolcador', 'nave, barco', 'barco de guerra'])

	n = n+1
	lista.append([])
	lista[n].append(['las embarcaciones 6'])
	lista[n].append(['le6'])
	lista[n].append(['whaler', 'wharf', 'yacht'])
	lista[n].append(['ballenero', 'embarcadero, muelle', 'yate'])

	n = n+1
	lista.append([])
	lista[n].append(['el barco 1'])
	lista[n].append(['eb1'])
	lista[n].append(['anchor', 'bow', 'bridge', 'buoy', 'cabin', 'captain', 'chain', 'compass'])
	lista[n].append(['ancla', 'proa', 'puente de mando', 'boya', 'camarote', 'capitán', 'cadena', 'brújula'])

	n = n+1
	lista.append([])
	lista[n].append(['el barco 2'])
	lista[n].append(['eb2'])
	lista[n].append(['crew', 'deck', 'dinghy', 'engine room', 'fire hydrant', 'flare', 'foremast', 'funnel'])
	lista[n].append(['tripulación', 'cubierta', 'bote', 'sala de máquinas', 'boca de incendio', 'bengala', 'trinquete', 'chimenea'])

	n = n+1
	lista.append([])
	lista[n].append(['el barco 3'])
	lista[n].append(['eb3'])
	lista[n].append(['galley', 'gangway', 'hatch', 'hold', 'horn', 'hose', 'hull', 'keel'])
	lista[n].append(['cocina', 'pasarela de salida', 'escotilla', 'bodega', 'sirena', 'manguera', 'casco', 'quilla'])

	n = n+1
	lista.append([])
	lista[n].append(['el barco 4'])
	lista[n].append(['eb4'])
	lista[n].append(['ladder', 'launching', 'life belt', 'life jacket', 'life raft', 'lifeboat', 'line', 'mast'])
	lista[n].append(['escalera', 'botadura', 'salvavidas', 'chaleco salvavidas', 'balsa salvavidas', 'bote salvavidas', 'soga, cable, cabo', 'mástil'])

	n = n+1
	lista.append([])
	lista[n].append(['el barco 5'])
	lista[n].append(['eb5'])
	lista[n].append(['master', 'oars', 'pier', 'port side', 'porthole', 'propeller', 'rudder', 'sail'])
	lista[n].append(['capitán', 'remos', 'embarcadero', 'babor', 'ojo de buey', 'hélice', 'timón', 'vela'])

	n = n+1
	lista.append([])
	lista[n].append(['el barco 6'])
	lista[n].append(['eb6'])
	lista[n].append(['sailor', 'starboard', 'stern'])
	lista[n].append(['marinero', 'estribor', 'popa'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 1'])
	lista[n].append(['prans1'])
	lista[n].append(['lots', 'form', 'bottom', 'rocking', 'mid', 'tier', 'way', 'settle'])
	lista[n].append(['un montón', 'formar', 'fondo', 'balanceo', 'medio', 'nivel', 'camino', 'resolver'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 2'])
	lista[n].append(['prans2'])
	lista[n].append(['support', 'rate', 'sponsor', 'blend', 'cans', 'supply', 'budget', 'chances'])
	lista[n].append(['apoyo', 'tarifa', 'patrocinador', 'mezcla', 'latas', 'suministro', 'presupuesto', 'posibilidades'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 3'])
	lista[n].append(['prans3'])
	lista[n].append(['powerful', 'throttled', 'seems', 'able', 'mess', 'stage', 'purposes', 'keyboard'])
	lista[n].append(['poderoso', 'estrangulado', 'parece', 'poder', 'lío', 'escenario', 'fines', 'teclado'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 4'])
	lista[n].append(['prans4'])
	lista[n].append(['crap', 'kind', 'shut', 'stuff', 'poorly', 'stock', 'turning', 'gorgeous'])
	lista[n].append(['mierda', 'tipo', 'cerrar', 'cosas', 'mal', 'valores', 'torneado', 'maravilloso'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 5'])
	lista[n].append(['prans5'])
	lista[n].append(['guess', 'achieve', 'shroud', 'overheat', 'pick', 'boom', 'layout', 'dye', 'scribe'])
	lista[n].append(['adivinar', 'lograr', 'sudario', 'sobrecalentar', 'recoger', 'auge', 'diseño', 'colorante', 'escriba'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 6'])
	lista[n].append(['prans6'])
	lista[n].append(['replacement', 'forcibly', 'geez', 'bulk', 'grinding', 'cuz', 'cue', 'mill'])
	lista[n].append(['reemplazo', 'a la fuerza', 'caray', 'abultar', 'molienda', 'porque', 'señal', 'molino'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 7'])
	lista[n].append(['prans7'])
	lista[n].append(['tape', 'gum', 'bucks', 'sale', 'deal', 'countertop', 'unusable', 'quote'])
	lista[n].append(['cinta', 'goma', 'dólares', 'venta', 'acuerdo', 'mostrador', 'inutilizable', 'citar'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 8'])
	lista[n].append(['prans8'])
	lista[n].append(['intake', 'riveted', 'covering', 'acetone', 'way', 'zip', 'behold', 'showing'])
	lista[n].append(['consumo', 'remachado', 'cubierta', 'acetona', 'camino', 'cremallera', 'Mirad', 'demostración'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 9'])
	lista[n].append(['prans9'])
	lista[n].append(['damn', 'dialed', 'exhaust', 'hook', 'fine', 'frame', 'buggy', 'field'])
	lista[n].append(['Maldita sea', 'marcado', 'escape', 'gancho', 'multa', 'cuadro', 'calesa', 'campo'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 10'])
	lista[n].append(['prans10'])
	lista[n].append(['overpowered', 'slide', 'quit', 'set', 'plug', 'wired', 'wireless', 'whatever'])
	lista[n].append(['dominado', 'diapositiva', 'dejar', 'conjunto', 'enchufe', 'cableado', 'inalámbrico', 'lo que sea'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 11'])
	lista[n].append(['prans11'])
	lista[n].append(['wire', 'awesome', 'stealth', 'storage', 'suspect', 'grab', 'port', 'bet'])
	lista[n].append(['cable', 'increíble', 'sigilo', 'almacenamiento', 'sospechar', 'agarrar', 'Puerto', 'apuesta'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 12'])
	lista[n].append(['prans12'])
	lista[n].append(['league', 'sales', 'pitch', 'doubt', 'heck', 'fullscreen', 'piece', 'tonight'])
	lista[n].append(['liga', 'ventas', 'tono', 'duda', 'infierno', 'pantalla completa', 'trozo', 'esta noche'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 13'])
	lista[n].append(['prans13'])
	lista[n].append(['campaign', 'stack', 'invoice', 'featured', 'sheer', 'awesomeness', 'merch', 'store'])
	lista[n].append(['Campaña', 'apilar', 'factura', 'destacado', 'escarpado', 'genialidad', 'mercadería', 'almacenar'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 14'])
	lista[n].append(['prans14'])
	lista[n].append(['previous', 'while', 'geez', 'bulk', 'grinding', 'squeamish', 'unfortunately', 'interferes'])
	lista[n].append(['anterior', 'mientras', 'caray', 'abultar', 'molienda', 'delicado', 'Desafortunadamente', 'interfiere'])

	n = n+1
	lista.append([])
	lista[n].append(['palabras random selección 15'])
	lista[n].append(['prans15'])
	lista[n].append(['connector', 'blown', 'ensure', 'shards', 'shorted', 'taped', 'carnage'])
	lista[n].append(['conector', 'estropeado', 'asegurar', 'fragmentos', 'en corto', 'grabado', 'carnicería'])

	n = n+1
	lista.append([])
	lista[n].append(['the -no se usa-'])
	lista[n].append(['the-n'])
	lista[n].append(['the -no se usa-', 'the -no se usa- 2', 'con instituciones y modos de transporte, cuando estamos hablando en general de ellos', 'the -no se usa 4-'])
	lista[n].append(['cuando hablamos de algo en general', 'cuando nos referimos a la televisión, las horas de las comidas, los días, de la semana, la hora, los meses del año, las estaciones o los años', '', 'con nombres de ciudades ni nombres de lugares en general'])

	n = n+1
	lista.append([])
	lista[n].append(['genitivo'])
	lista[n].append(['gen'])
	lista[n].append(['genitivo 1', 'genitivo 2', 'genitivo 3', 'genitivo 4', 'genitivo 5'])
	lista[n].append(['siempre utilizamos el genitivo para referirnos a personas', 'cuando nos referimos a cosas o lugares utilizaremos la preposición "of"', 'al final de la oración que acostumbra a ser la respuesta a una pregunta anterior', "cuando hay más de un poseedor, apóstrofo viene después de la 's'", 'cuando el nombre poseedor termina en una s, solo se añade el apóstrofe al final de la s'])

	n = n+1
	lista.append([])
	lista[n].append(['pronombres demostrativos'])
	lista[n].append(['pdem'])
	lista[n].append(['this. This is Miguel', 'that. Peter, is that you?', 'this. cuando presentamos personas'])
	lista[n].append(['para presentarnos por telefono', 'para preguntar quién hay al otro lado de la línea telefónica o en un lugar oscuro', 'this is my friend Jill'])

	n = n+1
	lista.append([])
	lista[n].append(['pronombres reflexivos'])
	lista[n].append(['pref'])
	lista[n].append(['pronombres reflexivos 1', 'pronombres reflexivos 2', 'by + pronombre reflexivo', 'pronombres reflexivos 3'])
	lista[n].append(['para  enfatizar el sujeto', 'con algunos verbos puede cambiar el significado', 'solo', 'no utilizamos pronombres reflexivos para acciones que la gente suele hacer a sí misma'])

	n = n+1
	lista.append([])
	lista[n].append(['the'])
	lista[n].append(['the'])
	lista[n].append(['the 1', 'the 2', 'the 3', 'the 4'])
	lista[n].append(['cuando sabemos de quién o de qué estamos hablando', 'nombres de regiones geológicas, cadenas de montañas, mares, océanos, grupos de islas, ríos y países', 'para hacer referencias a direcciones y a los puntos cardinales', 'con los adjetivos en grado superlativo y números ordinales'])

	n = n+1
	lista.append([])
	lista[n].append(['articulo indeterminado'])
	lista[n].append(['aind'])
	lista[n].append(['se usa "a" antes de las palabras que comienzan por la letra "u" o "eu"', 'se usa "an" con palabras que comienzan con h'])
	lista[n].append(['cuando son pronunciadas como el sonido "yu"', 'sólo cuando esta no se pronuncia'])
	
	n = n+1
	lista.append([])
	lista[n].append(['preposiciones de lugar'])
	lista[n].append(['plug'])
	lista[n].append(['next to, beside', 'by', 'between', 'behind', 'opposite', 'in front of', 'under', 'above', 'below'])
	lista[n].append(['al lado de, junto a', 'cerca, al lado de, junto a', 'entre', 'detrás de', 'delante y cara a cara', 'delante de pero no cara a cara', 'debajo de', 'por encima sin tocar', 'por debajo sin tocar'])

	n = n+1
	lista.append([])
	lista[n].append(['preposiciones de tiempo'])
	lista[n].append(['ptie'])
	lista[n].append(['before', 'after', 'during', 'for'])
	lista[n].append(['antes, antes de', 'después, después de, tras', 'durante', 'durante, por, -expresear un periodo de tiempo-'])

	n = n+1
	lista.append([])
	lista[n].append(['preposiciones de movimiento o dirección'])
	lista[n].append(['pmod'])
	lista[n].append(['to', 'across', 'along', 'around', 'down', 'into', 'off', 'onto', 'over', 'past', 'through', 'toward, towards', 'up'])
	lista[n].append(['a, hacia, dirección a, -siempre indica movimiento-', 'al otro lado de, de un lado a otro, -indicar movimiento hacia el lado opuesto-', 'a lo largo de', 'alrededor de', 'abajo, indica movimiento de una posición superior a una posición inferior', 'en, dentro de', 'más distante, más lejano', 'en, sobre, por encima de, arriba de', 'sobre, encima de, arriba de', 'por delante', 'a través de, por, -mostrar movimientos dentro de un espacio cerrado-', 'hacia, con dirección a', 'hacia arriba, -se utiliza para indicar movimiento de una posición inferior a una posición superior-'])

	n = n+1
	lista.append([])
	lista[n].append(['formación plurales sustantivos'])
	lista[n].append(['fps'])
	lista[n].append(['consonante + y', 'terminan en vocal + y añadimos s', 'terminan en s, ss, sg, ch, x, o', 'terminan en f o fe'])
	lista[n].append(['la y cambia a i + es', 'añadimos s', 'añadimos es', 'cambiamos la f o fe por ves'])

	n = n+1
	lista.append([])
	lista[n].append(['nombres propios siempre en mayúsculas'])
	lista[n].append(['npsem'])
	lista[n].append(['nombres de personas', 'meses y días de la semana', 'fiestas', 'nombres de empresas u organizaciones', 'nombres de países, ciudades, pueblos, etc', 'nacionalidades e idiomas', 'nombres geográficos y celestes', 'monumentos y edificios', 'acontecimientos históricos', 'títulos de las personas', 'religiones, deidades y escritura', 'títulos de libros, películas y obras de arte'])
	lista[n].append(['', '', '', '', '', '', '', '', '', '', '', ''])

	n = n+1
	lista.append([])
	lista[n].append(['orden de adjetivos izquierda-derecha'])
	lista[n].append(['odaid'])
	lista[n].append(['opinión, valor', 'tamaño, longitud', 'edad, temperatura', 'forma, superficie', 'color', 'origen', 'material', 'uso', 'nombre'])
	lista[n].append(['delicious', 'short, big, small, tall', 'new, old, young, hot, cold', 'round, thin, square', 'red, black, blue, green', 'Spanish, American, French', 'silver, cotton, paper, iron', 'electric, potilical', 'bath (towel)'])

	n = n+1
	lista.append([])
	lista[n].append(['imperativo'])
	lista[n].append(['imp'])
	lista[n].append(['no se utiliza el sujeto', 'verbo principal en infinitivo', 'imperativo negativo', 'let´s'])
	lista[n].append(['se supone que el sujeto siempre es you', '', 'Do not / Don´t + verbo', 'incluirnos a nosotros mismos'])

	n = n+1
	lista.append([])
	lista[n].append(['pronombres indefinidos'])
	lista[n].append(['pind'])
	lista[n].append(['all', 'another', 'any', 'anybody, anyone', 'anything', 'anywhere', 'both', 'each'])
	lista[n].append(['todo/todos', 'otro', 'algún/algunos, ningún, cualquier', 'alguien, nadie, cualquiera', 'algo, nada, cualquier', 'cualquier lugar', 'ambos, los dos', 'cada, cada uno'])

	n = n+1
	lista.append([])
	lista[n].append(['pronombres indefinidos 2'])
	lista[n].append(['pind2'])
	lista[n].append(['either', 'enough', 'every', 'everybody, everyone', 'everything', 'everywhere', 'few', 'fewer', 'less', 'little'])
	lista[n].append(['cualquiera, -de dos-', 'bastante, suficiente', 'cada, todos', 'todos, todo el mundo', 'todo, todos', 'todas partes', 'pocos, unos', 'menos', 'menos', 'poco'])

	n = n+1
	lista.append([])
	lista[n].append(['pronombres indefinidos 3'])
	lista[n].append(['pind3'])
	lista[n].append(['less', 'little', 'many', 'more', 'most', 'much', 'neither', 'nobody, no one', 'none'])
	lista[n].append(['menos', 'poco', 'muchos', 'más', 'la mayoría', 'mucho', 'ninguno, -de dos-', 'nadie', 'ningún, nada'])

	n = n+1
	lista.append([])
	lista[n].append(['pronombres indefinidos 4'])
	lista[n].append(['pind4'])
	lista[n].append(['none', 'nothing', 'nowhere', 'one', 'other', 'others', 'several', 'some'])
	lista[n].append(['ningún, nada', 'nada', 'ningún lugar', 'un, uno', 'otro', 'otros', 'varios', 'algún, algunos, algo de'])

	n = n+1
	lista.append([])
	lista[n].append(['pronombres indefinidos 5'])
	lista[n].append(['pind5'])
	lista[n].append(['somebody, someone', 'something', 'somewhere', 'such', 'they', 'you', 'se puede usar el genitivo sajón'])
	lista[n].append(['alguien', 'algo', 'algún lugar', 'tal, tan', 'ellos', 'tu', 'con los pronombres indefinidos'])

	n = n+1
	lista.append([])
	lista[n].append(['pronombres relativos'])
	lista[n].append(['prel'])
	lista[n].append(['cláusulas relativas', 'agregar información adicional', 'definen al sustantivo e indentifican a qué cosa o persona nos referimos'])
	lista[n].append(['las que añaden información adicional y aquellas que modifican o definen el sujeto de la oración', 'se utilizan comas para separar la cláusula relativa, no se puede usar that', 'no se usan comas'])

	n = n+1
	lista.append([])
	lista[n].append(['tipos de conjunciones'])
	lista[n].append(['tdc'])
	lista[n].append(['conjunciones coordinantes', 'siempre van entre las frases o palabras', 'conjunciones subordinantes'])
	lista[n].append(['cuando queremos enlazar dos frases que tienen el mismo valor', '', 'cuando una de las frases depende de la otra, en general van adelante de la frase subordinada'])

	n = n+1
	lista.append([])
	lista[n].append(['conjunciones 1'])
	lista[n].append(['conj1'])
	lista[n].append(['after', 'althought', 'and', 'as', 'as...as', 'as long as', 'as soon as', 'as well as', 'as far as'])
	lista[n].append(['después de', 'aunque', 'y', 'como, cuando, mientras', 'tan...como', 'siempre que, siempre y cuando, con tal de que, a condición de', 'en cuanto, tan pronto como, tan pronto...como', 'además de, así como, también', 'en la medida que, hasta, hasta donde, en tanto en cuanto, en relación con'])

	n = n+1
	lista.append([])
	lista[n].append(['conjunciones 2'])
	lista[n].append(['conj2'])
	lista[n].append(['because', 'before', 'both...and', 'but', 'either...or', 'even if', 'even thought', 'sin embargo'])
	lista[n].append(['porque', 'antes de', 'no sólo sino tambien, tanto...como', 'pero, sino', 'o...o', 'aunque', 'aunque', 'however'])

	n = n+1
	lista.append([])
	lista[n].append(['conjunciones 3'])
	lista[n].append(['conj3'])
	lista[n].append(['if', 'in case', 'in orden to', 'moreover', 'neither...nor', 'nevertheless', 'nor', 'now that'])
	lista[n].append(['si', 'en caso de que, por si', 'para, con objeto de', 'además', 'ni...ni', 'sin embargo, no obstante', 'ni', 'ahora que'])

	n = n+1
	lista.append([])
	lista[n].append(['conjunciones 4'])
	lista[n].append(['conj4'])
	lista[n].append(['or', 'once', 'since', 'so', 'so that', 'then', 'therefore', 'though'])
	lista[n].append(['o', 'una vez que', 'desde, desde que', 'así que', 'para que', 'entonces', 'por lo tanto, por consiguiente', 'aunque'])
	
	n = n+1
	lista.append([])
	lista[n].append(['conjunciones 5'])
	lista[n].append(['conj5'])
	lista[n].append(['unless', 'until', 'when', 'whereas', 'whether', 'whether...or', 'yet'])
	lista[n].append(['a menos que', 'hasta que', 'cuando', 'mientras que', 'si', 'si...o', 'sin embargo, no obstante'])

	n = n+1
	lista.append([])
	lista[n].append(['conjunciones 6'])
	lista[n].append(['conj6'])
	lista[n].append(['according to', 'after', 'although', 'and', 'as', 'as if', 'as long as', 'as soon as', 'as though', 'as well as'])
	lista[n].append(['de acuerdo a', 'después de', 'aunque, si bien', 'y', 'cuando, mientras, a medida que, como', 'como si', 'mientras, con tal que', 'en cuanto', 'como si', 'además de'])

	n = n+1
	lista.append([])
	lista[n].append(['conjunciones 7'])
	lista[n].append(['conj7'])
	lista[n].append(['because', 'because of', 'before', 'both...and', 'but', 'even thought', 'except', 'for'])
	lista[n].append(['porque', 'debido a', 'antes que', 'tanto...como', 'pero', 'aunque', 'excepto, salvo', 'porque'])

	n = n+1
	lista.append([])
	lista[n].append(['conjunciones 8'])
	lista[n].append(['conj8'])
	lista[n].append(['furthermore', 'nowever', 'in case of', 'in order to', 'moreover', 'namely', 'nevertheless', 'nor'])
	lista[n].append(['además', 'sin embargo', 'en caso de', 'para', 'además, por otra parte', 'a saber', 'sin embargo, no obstante', 'ni'])

	n = n+1
	lista.append([])
	lista[n].append(['conjunciones 9'])
	lista[n].append(['conj9'])
	lista[n].append(['notwithstanding', 'or else', 'otherwhise', 'provided', 'providing', 'since', 'so as to', 'so as not to', 'so that'])
	lista[n].append(['no obstante', 'sino', 'de otra manera, si no', 'siempre que, con tal de que', 'siempre que, con tal de que', 'puesto que', 'para', 'para no', 'para que'])

	n = n+1
	lista.append([])
	lista[n].append(['conjunciones 10'])
	lista[n].append(['conj10'])
	lista[n].append(['still', 'than', 'therefore', 'though', 'unless'])
	lista[n].append(['sin embargo, no obstante', 'que, -en comparaciones-', 'por lo tanto', 'aunque', 'a menos que'])

	n = n+1
	lista.append([])
	lista[n].append(['conjunciones 11'])
	lista[n].append(['conj11'])
	lista[n].append(['whenever', 'whereas', 'whether', 'wheter...or', 'while', 'yet', 'even if', 'even so', 'even when'])
	lista[n].append(['cada vez que, cuando', 'siendo que, mientras', 'si', 'si...o', 'mientras, mientras que, aunque', 'sin embargo, no obstante', 'incluso si', 'aún así', 'aún cuando, incluso cuando'])

	n = n+1
	lista.append([])
	lista[n].append(['superlativo'])
	lista[n].append(['sup'])
	lista[n].append(['si el adjetivo es posesivo, no se usa "the"', 'no se usa "the" si comparamos algo con si mismo', 'comparativo', 'superlativo'])
	lista[n].append(['his smartest student is Lisa', 'New York is coldest in January', 'more, less', 'the most, the least'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos ed ing'])
	lista[n].append(['aeding 1'])
	lista[n].append(['alarmed, alarming', 'aggravated, aggravating', 'annoyed, annoying', 'astonished', 'astounded, astounding', 'bored, boring', 'captivated, captivating', 'challenged, challenging'])
	lista[n].append(['alarmado, alarmante', 'agravado, agravante', 'molesto, molesto', 'asombrado, asombroso', 'asombrado, asombroso', 'aburrido, aburrido', 'cautivado, cautivador', 'desafiado, desafiante'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos ed ing'])
	lista[n].append(['aeding 2'])
	lista[n].append(['charmed, charming', 'comforted, comforting', 'confused, confusing', 'convinced, convincing', 'depressed, depressing', 'dissappointed, disappointing', 'discouraged, discouraging', 'disgusted, disgusting'])
	lista[n].append(['encantado, encantador', 'consolado, consolador', 'confuso, confuso', 'convencido, convincente', 'deprimido, deprimente', 'decepcionado, decepcionante', 'desalentado, desalentador', 'indignado, repugnante'])

	n = n+1
	lista.append([])
	lista[n].append(['adjectivos ed ing 3'])
	lista[n].append(['aeding 3'])
	lista[n].append(['distressed, distressing', 'disturbed, disturbing', 'embarrassed, embarrasing', 'encouraged, encouraging', 'entertained, entertaining', 'excited, exciting', 'exhausted, exhausting', 'fascinated, fascinating'])
	lista[n].append(['preocupado, preocupante', 'perturbado, perturbador', 'avergonzado, vergonzoso', 'animado, alentador', 'entretenido, entretenido', 'emocionado, emocionante', 'agotado, agotador', 'fascinado, fascinante'])

	n = n+1
	lista.append([])
	lista[n].append(['ed ing 4'])
	lista[n].append(['aeding 4'])
	lista[n].append(['frightened, frightening', 'frustrated, frustrating', 'fulfilled, fulfilling', 'gratified, gratifying', 'inspired, inspiring', 'insulted, insulting', 'interested, interesting', 'moved, moving'])
	lista[n].append(['asustado, espantoso', 'frustrado, frustrante', 'satisfecho, satisfactorio', 'satisfecho, gratificante', 'inspirado, inspirador', 'insultado, insultante', 'interesado, interesante', 'emocionado, emocionante'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos ed ing 5'])
	lista[n].append(['aeding 5'])
	lista[n].append(['overwhelmed, overwhelming', 'perplexed, perplexing', 'pleased, pleasing', 'relaxed, relaxing', 'relieved, relieving', 'satisfied, satisfying', 'shocked, shocking', 'sickened, sickening', 'soothed, soothing'])
	lista[n].append(['abrumado, abrumador', 'desconcertado, desconcertante', 'satisfecho, satisfactorio', 'relajado, relajante', 'consolado, consolador', 'satisfactorio, satisfactorio', 'conmocionado, chocante', 'asqueado, asqueroso', 'relajado, relajante'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos ed ing 6'])
	lista[n].append(['aeding6'])
	lista[n].append(['soothed, soothing', 'surprised, surprising', 'tempted, tempting', 'terrified, terrifying', 'threatened, threatening', 'thrilled, thrilling', 'tired, tiring', 'touched, touching', 'unsettled, unsettling', 'worried, worrying'])
	lista[n].append(['relajado, relajante', 'sorprendido, sorprendente', 'tentado, tentador', 'aterrado, aterrador', 'amenazado, amenazante', 'emocionado, emocionanted', 'cansado, agotador', 'conmovido, conmovedor', 'perturbado, perturbador', 'preocupado, preocupante'])

	n = n+1
	lista.append([])
	lista[n].append(['intensificadores 1'])
	lista[n].append(['int1'])
	lista[n].append(['very', 'really', 'extremely', 'amazingly', 'exceptionally', 'incredibly', 'remarkably', 'particularly', 'enough'])
	lista[n].append(['muy', 'verdaderamente', 'extremadamente', 'sorprendentemente', 'excepionalmente', 'increiblemente', 'notablemente', 'particularmente', 'suficiente, -va después del adjetivo-'])

	n = n+1
	lista.append([])
	lista[n].append(['adjetivos fuertes'])
	lista[n].append(['afue'])
	lista[n].append(['indican extremos', 'no se usa very', 'enormous', 'terrible', 'tiny', 'excellent', 'brilliant', 'perfect', 'marvelous'])
	lista[n].append(['algo o alguien es excepcional', 'se usa absolutely, exceptionally, particularly, really, enough', 'enorme', 'terrible', 'diminuto', 'excelente', 'brillante', 'perfecto', 'maravilloso'])

	n = n+1
	lista.append([])
	lista[n].append(['intensificadores con adjetivos comparativos y adjetivos superlativos'])
	lista[n].append(['icacyas'])
	lista[n].append(['palabras o frases particulares como intensificadores', 'much', 'a lot', 'a great deal', 'a good bit', 'con adjetivos superlativos', 'easily', 'by far'])
	lista[n].append(['is much faster than, is a lot taller than', 'mucho', 'mucho', 'mucho', 'bastante', 'is by far the most..., was easily the longest...', 'fácilmente', 'sin duda'])

	n = n+1
	lista.append([])
	lista[n].append(['mitigadores con adjetivos comparativos'])
	lista[n].append(['mcac'])
	lista[n].append(['a bit', 'rather', 'a little bit', 'slightly'])
	lista[n].append(['un poco', 'bastante', 'un poco', 'un poco'])

	n = n+1
	lista.append([])
	lista[n].append(['like'])
	lista[n].append(['like'])
	lista[n].append(['like', 'she dances like a professional', 'it´s so like ben, it´s just like', 'I look like my mother', 'sports like football'])
	lista[n].append(['parecido a, lo mismo de', 'verbo + like + sustantivo/pronombre', 'es tan típico de', 'parecer, parecerse', 'presentar ejemplos'])

	n = n+1
	lista.append([])
	lista[n].append(['as'])
	lista[n].append(['as'])
	lista[n].append(['en la misma manera, en la misma condición de', 'as she always does', 'like = such as', 'as como preposición'])
	lista[n].append(['as', 'as + sujeto + verbo', 'presentar ejemplos', 'papel o profesión de algo o alguien'])

	n = n+1
	lista.append([])
	lista[n].append(['gerundio'])
	lista[n].append(['ger'])
	lista[n].append(['se puede usar el gerundio', 'después de presposiciones', 'después de expresiones o verbos frasales'])
	lista[n].append(['como objeto, sujeto o complemento', 'about, at, by', 'feel like'])

	n = n+1
	lista.append([])
	lista[n].append(['infinitivo'])
	lista[n].append(['inf'])
	lista[n].append(['se puede usar como', 'se usa el infinitivo después de adjetivos'])
	lista[n].append(['como objeto, sujeto o complemento', 'glad, disappointed'])

	n = n+1
	lista.append([])
	lista[n].append(['construcción de preguntas'])
	lista[n].append(['cpre'])
	lista[n].append(['en las preguntas, las preposiciones se encuentran generalmente', 'preguntas de objeto', 'preguntas del sujeto'])
	lista[n].append(['al final de la frase', 'requieren el verbo auxiliar do', 'el pronombre interrogativo o question word'])

	n = n+1
	lista.append([])
	lista[n].append(['construcción de preguntas'])
	lista[n].append(['cpre'])
	lista[n].append(['en las preguntas, las preposiciones se encuentran generalmente', 'preguntas del objeto', 'preguntas del sujeto', 'preguntas del sujeto, no se utiliza el verbo auxiliar y el orden de las palabras no se invierte'])
	lista[n].append(['al final de la frase', 'requieren el verbo auxiliar do', 'el pronombre interrogativo o question word sirve como el sujeto de la frase', 'who called last night?'])

	n = n+1
	lista.append([])
	lista[n].append(['preguntas coletillas'])
	lista[n].append(['pcol'])
	lista[n].append(['question tags', 'auxliar de la frase principal de signo contrario+ sujeto', 'excepción'])
	lista[n].append(['¿?, verdad, no es verdad, no, no es así, en serio', 'sino hay, se usa do', 'am I, aren´t I'])

	n = n+1
	lista.append([])
	lista[n].append(['used to 1'])
	lista[n].append(['usedt1'])
	lista[n].append(['use', 'used to, verbo modal', 'used to, verbo modeal 2', 'sujeto + used to + verbo en infinitivo', 'Did + sujeto + use to + verbo en infinitivo ... ?', 'would', 'would en negativo'])
	lista[n].append(['usar, utilizar', 'algo que ocurria o sucedia en el pasado de manera habitual', 'algo que antes era verdad pero ya no lo es', 'sujeto + didn´t use to + verbo en infinitivo', '', 'eventos o acciones repetidas en el pasado, no con estados o hábitos', 'no se puede usar'])

	n = n+1
	lista.append([])
	lista[n].append(['to be used to'])
	lista[n].append(['tbut'])
	lista[n].append(['to be used to, se usa como adjetivo', 'si to be used to esta antes de un verbo'])
	lista[n].append(['se usa para cosas que son familiares o normales o comunes y se puede usar en cualquier tiempo verbal', 'el verbo debe de estar en gerundio'])

	n = n+1
	lista.append([])
	lista[n].append(['to get used to'])
	lista[n].append(['tgut'])
	lista[n].append(['to get used to, acostumbrando a'])
	lista[n].append(['indica el proceso de familiarizarse con algo'])

	n = n+1
	lista.append([])
	lista[n].append(['already just still yet'])
	lista[n].append(['ajsy'])
	lista[n].append(['already, va generalmente entre el verbo auxiliar y el verbo', 'just, va entre el verbo auxiliar y el verbo', 'still, va siempre después del sujeto', 'yet, va al final de la frase'])
	lista[n].append(['ya', 'acabar de, justo', 'aún, todavía', 'aún/todavía, ya, -negativas, interrogativas-'])

	n = n+1
	lista.append([])
	lista[n].append(['for since ago'])
	lista[n].append(['fsa'])
	lista[n].append(['for, indica duración o un periodo de tiempo', 'since, indica el principio de un periodo de tiempo que sigue al presente', 'ago, se refiere a un tiempo en el pasado o un tiempo antes del actual y va al final de la frase'])
	lista[n].append(['durante', 'desde', 'hace'])

	n = n+1
	lista.append([])
	lista[n].append(['modales perfectos'])
	lista[n].append(['mper'])
	lista[n].append(['can´t have, cuando estamos bastante seguros de que algo no ocurrió o que no fue verdad en el pasado', 'couldn´t = can´t have'])
	lista[n].append(['similar a must have pero en forma negativa', ''])

	n = n+1
	lista.append([])
	lista[n].append(['futuro perfecto'])
	lista[n].append(['fper'])
	lista[n].append(['to be going to/ will + have + participio pasado'])
	lista[n].append(['intercambiables'])

	n = n+1
	lista.append([])
	lista[n].append(['condicionales'])
	lista[n].append(['cond'])
	lista[n].append(['tipo 0, * = if/when ', 'tipo 1, * = if', 'tipo 2, * = if', 'tipo 3, * = if'])
	lista[n].append(['* present simple/presente * present simple/presente', '* present simple/presente * future simple/futuro/modals/modales', '* past simple/pasado imperfecto(subjuntivo) * would/condicional/modals/modales', '* past perfect/pasado pluscuamperfecto(subjuntivo) * would/condicional/modals/modales have'])

	n = n+1
	lista.append([])
	lista[n].append(['voz pasiva'])
	lista[n].append(['vpas'])
	lista[n].append(['sujeto + to be (en el tiempo indicado) + participio pasado + by'])
	lista[n].append([''])

	n = n+1
	lista.append([])
	lista[n].append(['estilo directo'])
	lista[n].append(['edir'])
	lista[n].append(['" " sujeto said/sujeto asked'])
	lista[n].append(['sujeto said/sujeto asked " "'])

	n = n+1
	lista.append([])
	lista[n].append(['estilo indirecto'])
	lista[n].append(['eind'])
	lista[n].append(['that a veces se usa en frases afirmativas y negativas para introducir lo que ha dicho la otra persona', 'degradacion presente', 'degradación pasado', 'degradación pasado perfecto', 'cuando hablamos de algo que no ha cambiado (que sigue siendo cierto) o de algo en el futuro', 'would, could, should, might, ought to, -degradación-', 'will, -degradación-', 'can, -degradación-', 'must, -degradación-', 'shall, -degradación-', 'may, -degradación-'])
	lista[n].append(['if/whether a veces se usa en frases interrogativas', 'presente => pasado', 'pasado => pasado perfecto', 'no hay', 'no es necesario cambiar el tiempo', 'no hay', 'would', 'could', 'had to', 'should', 'might, could'])

	n = n+1
	lista.append([])
	lista[n].append(['say'])
	lista[n].append(['say'])
	lista[n].append(['say', 'se usa en', 'si queremos usarlo con un objeto personal'])
	lista[n].append(['decir algo', 'estilo indirecto y el indirecto', 'se usa la preposición to'])

	n = n+1
	lista.append([])
	lista[n].append(['tell'])
	lista[n].append(['tell'])
	lista[n].append(['tell', 'se usa en', 'cuando usamos tell', 'se usa en 1', 'se usa en 2', 'se usa en 3', 'se usa en 4', 'se usa en 5'])
	lista[n].append(['decir algo a alguien', 'estilo directo e indirecto', 'necesitamos usar un objeto indirecto que va después del verbo', 'ordenes e instrucciones', 'cuando damos o pedimos información', 'con cuentos o bromas, contar', 'con la verdad y las mentiras', 'con el tiempo o la fecha'])

	n = n+1
	lista.append([])
	lista[n].append(['agregar información'])
	lista[n].append(['ainf'])
	lista[n].append(['and', 'also', 'in addition', 'as well as', 'too', 'besides', 'furthermore', 'moreover'])
	lista[n].append(['y', 'también, -entre el sujeto y el verbo-', 'además, -al principio de la oración-', 'además de', 'también, -al final de una oración/entre el sujeto y el verbo-', 'además de, -al principio de una oración-', 'además (formal), -al principio de una oración-', 'además, -al principio de una oración-'])

	n = n+1
	lista.append([])
	lista[n].append(['contrastar información'])
	lista[n].append(['cinf'])
	lista[n].append(['bur', 'yet', 'however', 'although, though, even though', 'despite, despite the fact that', 'in spite of', 'nevertheless', 'nonetheless', 'while'])
	lista[n].append(['pero', 'pero, -formal-', 'sin embargo, -al principio de una frase-', 'aunque, -al principio de una oración o entre las dos cláusulas', 'a pesar de, -debe ir antes de un sustantivo o gerundio; si va antes de una cláusula debemos usar la segunda forma-', 'a pesar de, -mismas reglas que despite-', 'no obstante, -al principio de una oración o entre dos cláusulas; siempre va antes de una coma-', 'no obstante, -se usa igual que nevertheless-', 'si bien, -frecuentemente al principio-'])

	n = n+1
	lista.append([])
	lista[n].append(['ideas condicionales'])
	lista[n].append(['icond'])
	lista[n].append(['providing', 'provided that', 'as long as, so long as', 'unless', 'only if', 'even if', 'whether or not'])
	lista[n].append(['si, -puede ir al principio o en medio de la oración-', 'a condición de, -puede ir al principio o en medio de la oración-', 'mientras, -puede ir al principio o en medio de la oración-', 'a menos que, siempre antes de una oración afirmativa', 'solo sí', 'aun si, incluso si', 'we will go to the beach whether or not it rains, iremos a la playa llueva o no llueva'])

	n = n+1
	lista.append([])
	lista[n].append(['dar una razón o causa'])
	lista[n].append(['duroc'])
	lista[n].append(['because, because of', 'since', 'since, since of', 'as, as of', 'due to, due to the fact that', 'owing to', '', 'owing to, owing to the fact that'])
	lista[n].append(['porque, -al principio o en medio de una oración; si va antes de un sustantivo se utiliza la segunda forma-', 'ya que, -al principio o en medio de una oración; si va antes de un sustantivo se utiliza la segunda forma-', 'ya que, -al principio o en medio de una oración; si va antes de un sustantivo se utiliza la segunda forma-', 'como, -al principio o en medio de una oración; si va antes de un sustantivo se utiliza la segunda forma-', 'debido a, -debe ir antes de un sustantivo, si va antes de una cláusula se usa la segunda forma-', 'owing to', '', 'debido a, -debe ir antes de un sustantivo, si va antes de una cláusula se usa la segunda forma-'])

	n = n+1
	lista.append([])
	lista[n].append(['dar un resultado o un efecto'])
	lista[n].append(['duroue'])
	lista[n].append(['so', 'as a result', 'therefore', 'consequently', 'as a consequence', 'accordingly'])
	lista[n].append(['así que, -generalmente en medio de la oración; antes del resultado-', 'como resultado, -generalmente al principio; antes del resultado-', 'por lo tanto, -generalmente al principio; antes del resultado-', 'en consecuencia, -generalmente al principio; antes del resultado-', 'como consecuencia, -generalmente al principio; antes del resultado-', 'en consecuencia, -generalmente al principio; antes del resultado-'])

	n = n+1
	lista.append([])
	lista[n].append(['dar ejemplos'])
	lista[n].append(['dejem'])
	lista[n].append(['for example', 'such as', 'for instance'])
	lista[n].append(['por ejemplo, -puede ir al principio o en medio; al principio lleva una coma; en medio lleva dos comas-', 'tales como, -siempre en medio y con una coma antes-', 'por ejemplo, -puede ir al principio o en medio; al principio lleva una coma; en medio lleva dos comas-'])

	n = n+1
	lista.append([])
	lista[n].append(['secuenciación de ideas'])
	lista[n].append(['sdid'])
	lista[n].append(['firstly, secondly, ... lastly', 'the following'])
	lista[n].append(['en primer lugar, en segundo lugar, ... por último', 'el/los siguiente/s'])

	n = n+1
	lista.append([])
	lista[n].append(['resumir ideas'])
	lista[n].append(['ride'])
	lista[n].append(['in conclusion, to clonclude', 'in conclusion, to conclude, in summary, in short/brief'])
	lista[n].append(['', 'en conclusión, para concluir, en resumen, en resumen, -generalmente al principio y antes de una coma-'])

	n = n+1
	lista.append([])
	lista[n].append(['prefijos 1'])
	lista[n].append(['pre1'])
	lista[n].append(['a, an', 'anti', 'auto', 'bi', 'co', 'com', 'com, con', 'de', 'dis'])
	lista[n].append(['sin', 'contra/opuesto', 'sí mismo', 'dos', 'con', '', 'con', 'separadp', 'no'])

	n = n+1
	lista.append([])
	lista[n].append(['prefijos 2'])
	lista[n].append(['pre2'])
	lista[n].append(['en', 'extra', 'il, im, in, ir', 'in', 'inter', 'macro', 'micro', 'mis'])
	lista[n].append(['causar a', 'más', 'no, sin', 'en, dentro de', 'entre', 'grande', 'pequeño', 'mal, incorrecta'])

	n = n+1
	lista.append([])
	lista[n].append(['prefijos 3'])
	lista[n].append(['pre3'])
	lista[n].append(['mono', 'non', 'post', 'pre, pro', 're', 'sub', 'trans', 'tri', 'un'])
	lista[n].append(['uno', 'no, sin', 'después', 'antes', 'otra vez', 'abajo', 'a través de', 'tres', 'no'])

	n = n+1
	lista.append([])
	lista[n].append(['sufijos sustantivo 1'])
	lista[n].append(['susus1'])
	lista[n].append(['acy', 'al', 'ance, ence', 'dom', 'er, or', 'ism', 'ist'])
	lista[n].append(['estado o calidad de', 'acto o proceso', 'estado o calidad de', 'lugar o estado de ser', 'alguien que, uno que', 'dotrina, creencia', 'alguien que, uno que'])

	n = n+1
	lista.append([])
	lista[n].append(['sufijos sustantivo 2'])
	lista[n].append(['susus2'])
	lista[n].append(['ity, ty', 'ment', 'ness', 'ship', 'sion, tion'])
	lista[n].append(['calidad de', 'condición de', 'estado de ser', 'posición', 'estado de ser'])

	n = n+1
	lista.append([])
	lista[n].append(['sufijos verbo'])
	lista[n].append(['suver'])
	lista[n].append(['ate', 'en', 'ify, fy', 'ize, ise'])
	lista[n].append(['convertirse en, hacerse, volverse', 'convertirse en, hacerse, volverse', 'convertirse en, hacerse, volverse', 'convertirse en, hacerse, volverse'])

	n = n+1
	lista.append([])
	lista[n].append(['sufijos adjetivo'])
	lista[n].append(['suadj'])
	lista[n].append(['able, ible', 'ful', 'ic, ical', 'ious, ous', 'ish', 'ive', 'less', 'y'])
	lista[n].append(['capaz de', 'notable para', 'relativas a', 'caracterizado por', 'tener la calidad de', 'tener la calidad de', 'sin', 'caracterizado por'])

	n = n+1
	lista.append([])
	lista[n].append(['so'])
	lista[n].append(['so'])
	lista[n].append(['so', 'so + adjetivo/adverbio', 'so + cuantificador + noun', 'so + that'])
	lista[n].append(['tan, así, entonces', 'sentimientos o efectos extremos', 'extremos en cantidad', 'tan + que, resultados o consecuencias'])

	n = n+1
	lista.append([])
	lista[n].append(['such'])
	lista[n].append(['such'])
	lista[n].append(['such + adjetivo + sustantivo', 'such + that', 'such + sustantivo critico', 'such + sustantivo'])
	lista[n].append(['mostrar extremos', 'tan + que, mostrar extremos que terminan en un resultado', 'da énfasis, he is such a jerk, you are such a clown', 'tal, un tipo de'])

	n = n+1
	lista.append([])
	lista[n].append(['enough'])
	lista[n].append(['enough'])
	lista[n].append(['adjetivo/adverbio + enough', 'enough + sustantivo', 'enough + adjetivo + sustantivo', 'adjetivo + enough + sustantivo', 'enough of + determinante (articulo o pronombre)'])
	lista[n].append(['suficientemente', 'suficiente', 'suficiente', 'sustantivo + suficientemente + adjetivo', 'bastantes'])

	n = n+1
	lista.append([])
	lista[n].append(['too'])
	lista[n].append(['too'])
	lista[n].append(['too + adjetivo/adverbio', 'too many + nombre contable, too much + nombre incontable', 'too many of + determinante + nombre contable, too much of + determinante + nombre incontable'])
	lista[n].append(['demasiado', 'demasiados, demasiado', 'demasiados, demasiado'])

	n = n+1
	lista.append([])
	lista[n].append(['even'])
	lista[n].append(['even'])
	lista[n].append(['even, -adjetivo-', 'even, -adverbio-', 'se encuentra', 'cuando se encuentra al principio de una frase se refiere al sujeto', 'cuando se encuentra al principio de una frase', 'antes de otras palabras', 'frases negativas para expresar extremos negativos', 'en comparaciones para dar énfasis'])
	lista[n].append(['uniforme, plano, justo, igual', 'incluso, hasta', 'antes del verbo que modifica', '', 'se refiere al sujeto', 'que queremos enfatizar', 'ni, antes del verbo principal', 'antes del adjetivo o adverbio'])

	n = n+1
	lista.append([])
	lista[n].append(['else'])
	lista[n].append(['else'])
	lista[n].append(['después de pronombres indefinidos', 'después de pronombres interrogativos', 'posesiva', 'or else', 'elsewhere'])
	lista[n].append(['para referirnos a personas o cosas además de las ya mencionadas', 'más', 'else´s', 'o si no, si no', 'otro sitio, -un lugar que no sea el ya mencionado-'])

	n = n+1
	lista.append([])
	lista[n].append(['-ever'])
	lista[n].append(['-ever'])
	lista[n].append(['-ever en pronombres interrogativos', 'significado general', 'cuando se utilizan como interrogativos', 'whatever, -adjetivo o pronombre-', 'whichever, -adjetivo o pronombre-', 'wherever, -conjunción-', 'whenever, -conjunción-', 'whoever, whomever, -pronombre-', 'however, -adverbio-'])
	lista[n].append(['más o menos equivalente a: cualquier/a que', 'no importa, da igual', 'expresan extrañeza, sorpresa, indignación o exasperación', 'cualquier que, lo que quiera', 'cualquiera', 'dondequiera, en cualquier lugar o parte', 'siempre que, cuando sea', 'quienquiera', 'como quiera'])

	n = n+1
	lista.append([])
	lista[n].append(['either y neither'])
	lista[n].append(['eyn'])
	lista[n].append(['podemos utilizarlos como', 'either...or...', 'neither...or...', 'both + sustantivo', 'either, neither, -como pronombre llevan of-', 'either, neither, -adverbios-', 'either, neither, -determinante-', 'si una de las dos está en plural, se usa plural', 'si una de las dos partes está en plural'])
	lista[n].append(['pronombres, determinantes o adverbios', '...o...', 'ni...ni...', 'ambos', 'o/ni, cualquier/ninguno, también', 'sujeto + verbo auxiliar + either, neither + verbo + sujeto,', 'cualquier, ningún', '', 'se usa plural'])

	n = n+1
	lista.append([])
	lista[n].append(['each y every'])
	lista[n].append(['each y every'])
	lista[n].append(['each y every como determinantes de cantidad', 'each', 'each of + pronombre/sustantivo con un determinante'])
	lista[n].append(['each puede usarse como pronombre', 'cada, -uno por uno-', 'cada uno/a de'])

	n = n+1
	lista.append([])
	lista[n].append(['every'])
	lista[n].append(['every'])
	lista[n].append(['destacamos el grupo y solo se puede usar con grupos de tres o más personas o cosas', 'se usa con'])
	lista[n].append(['se utiliza para generalizar o para expresar la frecuencia con que algo suceda y siempre va seguida de un sustantivo', 'sustantivos abstractos y adverbios'])

	n = n+1
	lista.append([])
	lista[n].append(['go y come'])
	lista[n].append(['gyc'])
	lista[n].append(['go', 'come'])
	lista[n].append(['ir, -se utiliza para indicar una dirección alejándose del orador o la persona a la que se habla o a un sitio diferente del actual', 'venir, -indica un movimiento hacia o en la dirección del orador o la persona a la que se habla; se utiliza para expresar movimiento desde un sitio diferente al sitio actual del orador o la persona a la que se habla-'])

	n = n+1
	lista.append([])
	lista[n].append(['bring y take'])
	lista[n].append(['byt'])
	lista[n].append(['bring', 'take'])
	lista[n].append(['traer, -indica un movimiento a la dirección del orador o la persona a la que se habla-', 'llevar, -indica un movimiento de alejamiento del sitio actual del orador o la persona a la que se habla-'])

	return lista

def contador():
	lista_aux = lista()
	num = 0

	for x in lista_aux:
		num = len(x[2]) + num

	print(num)

def encontrador(encontrar, ingles_espanol):
	import practicador_in

	lista_aux = lista()

	if ingles_espanol == 'español' or ingles_espanol == '2':
		parametro_idioma = 3
	elif ingles_espanol == 'ingles' or ingles_espanol == '1':
		parametro_idioma = 2
	else:
		parametro_idioma = 2

	for x in lista_aux:
		for y in x[parametro_idioma]:
			if not y.find(encontrar) == -1:
				print(y)
				print(x[1])
				print(lista_aux.index(x)+1)

				practicador_in.impresor2('',lista_aux.index(x),'',lista = lista())#Se imprime la lista elegida
				print()

	input('Continuar [enter]: ')

def impresor(rango, lista):
	import practicador_in

	practicador_in.impresor1(rango, lista)

def seleccionador(lista_total):

	lista_seleccionada = []
	lista_seleccionada.append([])
	lista_seleccionada.append([])

	print('Para salir inserte 0 en número de lista')

	while True:

		e = False

		try:
			numero_lista = int(input('Seleccione número de lista: '))
			numero_elemento = int(input('Seleccione número de elemento de lista: '))

			if numero_lista == 0:
				break
		except:
			print('Error. No es un número')
			e = True

		try:
			elemento_ingles = lista_total[numero_lista-1][2][numero_elemento-1]
			elemento_espanol = lista_total[numero_lista-1][3][numero_elemento-1]
		except:
			if numero_lista > len(lista_total):
				print('Error. No es un número de lista valido')
			elif numero_elemento > len(lista_total[numero_lista-1][2]):
				print('Error. No es un número de elemento de lista valido')
			else:
				pass
			e = True

		if e == False:
			print(elemento_ingles)
			print(elemento_espanol)
			print()

			lista_seleccionada[0].append(elemento_ingles)
			lista_seleccionada[1].append(elemento_espanol)

	return lista_seleccionada

if __name__ == '__main__':
	impresor(1000, lista())

	'''lista_seleccionada = seleccionador(lista())

	import traductor_pal

	traductor_pal.impresor_lista_final(lista_seleccionada[0], lista_seleccionada[1], 'palabras random selección', 'prans', 8, 8)'''

	input()