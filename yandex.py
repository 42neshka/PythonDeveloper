
#!Список (Массив) [		] list() могут повторяться значения
#!Множество {		} set() повторений быть не может

'''

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

'''
#!объект.метод(аргумент) 
#!Метод — это разновидность функции, мини-программа. Однако, в отличие от функций, метод применяется к объекту
#! .add(+) .union(объединение) .difference(-) .intersection(пересечение)

#! Словари
dict = {
    'hand': 'рука',
    'leg': 'нога'
}

.values()   .keys()     for singer in favorite_songs.values():
.update()   dict1.update(dict2)
.items()    for song, performer in favorite_songs.items():

.append(+ in end)   sleep_list.append('example')

.split(указывается разделитель) сплитит в список (list) подходит для поиска
words_list = poem_str.split(' ')
.join(list)
new_string = '-'.join(words_list)

'''

""" 
quote_1 = 'Работает? Не трогай'
if '?' in quote_1:
    q1 = quote_1.replace('?', ' и')
    print(q1)

Работает и Не трогай
 """

""" 
#! f Strings
one_hundred = 100
rubles = 'рублей'
friends = 'друзей'
print(f'Не имей {one_hundred} {rubles}, а имей {one_hundred} {friends}.')

# А без применения f-строк тот же код выглядит похуже:
print('Не имей ' + str(one_hundred) + ' ' + rubles + ', а имей ' + str(one_hundred) +' ' + friends + '.')




"""