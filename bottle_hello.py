import bottle

@bottle.route('/')
def home_page():
	langs = ['Python', 'Ruby', 'Perl', 'C++']
	return bottle.template('hello_world', {'username':'Thiago','things':langs})

@bottle.route('/favorita', method='POST')
def favorita():
	lang = bottle.request.forms.get('lang')
	if lang == None or lang == '':
			lang = 'Nenhuma Escolhida'
	return bottle.template('lang_selection', {'lang':lang})

bottle.debug(True)
bottle.run(host='localhost', port=8082)
