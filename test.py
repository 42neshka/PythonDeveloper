DATABASE = {
	'Серёга': 'Омск',
	'Соня': 'Москва',
	'Миша': 'Москва',
	'Дима': 'Челябинск',
	'Алина': 'Красноярск',
	'Егор': 'Пермь',
	'Коля': 'Красноярск'
}

def search(name):
	if 'name' in DATABASE.values():
		return DATABASE['name']

print (search('Соня'))
