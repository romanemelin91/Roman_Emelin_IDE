#объект Counter (от англ. «счётчик») предназначен для решения часто возникающей задачи по подсчёту различных элементов

# Импортируем объект Counter из модуля collections
from collections import Counter
# Создаём пустой объект Counter
c = Counter()

#c['red'] += 1
#print(c)
# Будет напечатано:
# Counter({'red': 1})

cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']

#Посчитать значения, конечно, можно и в цикле, используя синтаксис из предыдущего примера:

c = Counter()
for car in cars:
    c[car] += 1
 
print(c)
# Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})

#Однако гораздо проще при создании Counter сразу передать в круглых скобках итерируемый объект, в котором необходимо посчитать значения:

c = Counter(cars)
print(c)
# Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})

print(c['black'])
# 3

print(c['purple'])
# 0

#Узнать сумму всех значений в объекте Counter можно, воспользовавшись следующей конструкцией:
print(sum(c.values()))
# 9

#В этой конструкции мы сначала получаем элементы (число раз, когда встретился ключ)
#с помощью функции values (такая же функция есть и у словаря):

print(c.values())
# dict_values([3, 2, 3, 1])