# Импортируем объект Counter из модуля collections
from collections import Counter
# Создаём пустой объект Counter
c = Counter()

#Допустим, вы с другом из другого города решили посчитать количество цветов встреченных на дороге машин.
#У вас получились такие списки цветов:

cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow)
print(counter_spb)
 
# Counter({'black': 4, 'yellow': 3, 'white': 2})
# Counter({'white': 3, 'red': 2, 'black': 2, 'yellow': 2})

#Чтобы узнать, сколько машин разных цветов встретилось в двух городах, можно сложить два исходных счётчика и получить новый счётчик:
print(counter_moscow + counter_spb)
# Counter({'black': 6, 'white': 5, 'yellow': 5, 'red': 2})

#Чтобы узнать разницу между объектами Counter, необходимо воспользоваться функцией subtract, 
#которая меняет тот объект, к которому применяется.
#В примере выше из значений, посчитанных для Москвы, вычитаются значения, посчитанные для Санкт-Петербурга:

print(counter_moscow)
print(counter_spb)
# Counter({'black': 4, 'yellow': 3, 'white': 2})
# Counter({'white': 3, 'red': 2, 'black': 2, 'yellow': 2})
 
counter_moscow.subtract(counter_spb)
print(counter_moscow)
# Counter({'black': 2, 'yellow': 1, 'white': -1, 'red': -2})

# Пересоздаём счётчики, потому что объект counter_moscow поменял свои значения
# после функции subtract.
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow - counter_spb)
# Counter({'black': 2, 'yellow': 1})

print(*counter_moscow.elements())
# black black black black white white yellow yellow yellow

#Обратите внимание, что элементы возвращаются в алфавитном порядке, а не в том порядке, в котором их вносили в счётчик.

# Чтобы получить список уникальных элементов, достаточно воспользоваться функцией list():
print(list(counter_moscow))
# ['black', 'white', 'yellow']

#С помощью функции dict() можно превратить Counter в обычный словарь:

print(dict(counter_moscow))
# {'black': 4, 'white': 2, 'yellow': 3}

#Функция most_common() позволяет получить список из кортежей элементов в порядке убывания их встречаемости:
print(counter_moscow.most_common())
# [('black', 4), ('yellow', 3), ('white', 2)]

#В неё также можно передать значение, которое задаёт желаемое число первых наиболее частых элементов, например, 2:

print(counter_moscow.most_common(2))
# [('black', 4), ('yellow', 3)]    