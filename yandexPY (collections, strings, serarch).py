#! Коллекции
'''

# Список (Массив) [		] list() могут повторяться значения
# Множество {		} set() повторений быть не может, рандом порядок
# Словари
dict = {
    'hand': 'рука',
    'leg': 'нога'
}

print(dict['hand']) #рука
'''

''' #todo Пример использования команды set()

songs_list = [
    'Мы к вам заехали на час',
    'А как известно, мы народ горячий',
    'Куда ты, тропинка, меня завела',
    'Луч Солнца Золотого',
    'Рок-колыбельная',
    'Рок-колыбельная',
    'Куда ты, тропинка, меня завела',
    'А как известно, мы народ горячий',
    'Луч Солнца Золотого',
    'Ничего на свете лучше нету',
    'А как известно, мы народ горячий',
    'Луч Солнца Золотого',
    'Мы к вам заехали на час',
    'Ничего на свете лучше нету',
    'Куда ты, тропинка, меня завела',
    'Луч Солнца Золотого'
]

# Преобразуем список songs_list в сет
# и запишем этот сет в переменную unique_songs:
unique_songs = set(songs_list)

print(unique_songs)
print(len(unique_songs))
'''

''' #? объект.метод(аргумент) 

Метод — это разновидность функции, мини-программа. Однако, в отличие от функций, метод применяется к объекту
 .add(+) .union(объединение) .difference(-) .intersection(пересечение)  #* данные методы применяемы только к set (множествам != спискам)
'''
 
''' #? Методы для коллекций:
.values()   .keys() #* для просмотра словаря
for singer in favorite_songs.values(): #* перебор значений в цикле
.update()   dict1.update(dict2) #* объединение двух словарей без переменной
.items()    for song, performer in favorite_songs.items(): #* только через цикл
.append(+ in end)   sleep_list.append('example')
.split(указывается разделитель) сплитит в список (list) подходит для поиска
#todo words_list = poem_str.split(' ')
.join(list)
#todo new_string = '-'.join(words_list)

'''

""" #todo Пример создания словаря из 2 списков

friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

friends =  {}

for i in range(0, len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]
"""

""" #todo Пример использования метода .replace()
quote_1 = 'Работает? Не трогай'
if '?' in quote_1:
    q1 = quote_1.replace('?', ' и')
    print(q1)

Работает и Не трогай
 """

#! f Strings

""" #todo Пример использования f'strings
one_hundred = 100
rubles = 'рублей'
friends = 'друзей'
print(f'Не имей {one_hundred} {rubles}, а имей {one_hundred} {friends}.')
#* А без применения f-строк тот же код выглядит похуже:
print('Не имей ' + str(one_hundred) + ' ' + rubles + ', а имей ' + str(one_hundred) +' ' + friends + '.')
"""

""" #todo Пример осуществления поиска в коллекциях

sleep_list = [
    'спать', 
    'дрыхнуть', 
    'кемарить',
    'спать'
] 

sleep_set = {
    'дрыхнуть', 
    'спать', 
    'кемарить'
} 

sleep_dict = {
    'спать': 'дрыхнуть', 
    'почивать': 'кемарить'
}

if 'дрыхнуть' in sleep_list:
    print('В списке: нашлось!') 
else:
    print('В списке: не нашлось :(')

if 'дрыхнуть' in sleep_set:
    print('В сете: нашлось!') 
else:
    print('В сете: не нашлось :(')

if 'дрыхнуть' in sleep_dict.values():
    print('В словаре: нашлось!') 
else:
    print('В словаре: не нашлось :(')

"""

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

# Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья" 
# в зависимости от того, какое число передано в аргументе friends_count
def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        format_friends_count(count)
        # Вызовите функцию format_friends_count() и передайте в неё count.
        # Отредактируйте строку ниже: в ней должно использоваться выражение, 
        # которое вернёт функция format_friends_count()
        return f'У тебя {format_friends_count(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'

def process_query(query):
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return process_anfisa(elements[1])
    else:
        return process_friend(elements[0], elements[1])
    
def process_friend(name, query):
    namesearch = ', '.join(DATABASE)
    if name in namesearch:
        if query == 'ты где?': 
            return f'{name} в городе {DATABASE[name]}'
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'

print('Привет, я Анфиса!')
print(process_query('Анфиса, сколько у меня друзей?'))
print(process_query('Анфиса, кто все мои друзья?'))
print(process_query('Анфиса, где все мои друзья?'))
print(process_query('Анфиса, кто виноват?'))
print(process_query('Соня, ты где?'))
print(process_query('Коля, что делать?'))
print(process_query('Антон, ты где?'))