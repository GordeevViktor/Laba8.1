DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
    elif query == 'Кто все мои друзья?': 
        friends_string = ''
        # Чтобы получить перечень друзей - 
        # переберите словарь DATABASE в цикле
        for friend in DATABASE:     
             friends_string += friend + ' '# Добавляйте к переменной friends_string имя друга и пробел
        # Верните строку, составленную из 'Твои друзья: ' и friends_string 
        return('Твои друзья: ' + str(friends_string)) 
    elif query == 'Где все мои друзья?':
        city_frends = ''
        unique_cities = set(DATABASE.values())
        for city in unique_cities:
            city_frends += city + ' ' 
            return('Твои друзья в городах: '+ ' ' + str(city_frends))
    else:
        return '<неизвестный запрос>'

# Не изменяйте следующий код
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))