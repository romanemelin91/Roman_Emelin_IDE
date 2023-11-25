#Возможно, вы уже сталкивались с задачей, когда необходимо было создать словарь,
#в котором по ключам расположены списки. Например, у нас есть список из кортежей с фамилиями студентов и их учебными группами:

students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]

groups = dict()
 
#for student, group in students:
#    # Проверяем, есть ли уже эта группа в словаре
#    if group not in groups:
#        # Если группы ещё нет в словаре, создаём для неё пустой список
#        groups[group] = list()
#    groups[group].append(student)
 
# print(groups)
# {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']}

#Создадим defaultdict, в котором при обращении по несуществующему ключу будет автоматически создаваться новый список.
#Для этого при создании объекта defaultdict в круглых скобках передадим параметр list:

from collections import defaultdict
groups = defaultdict(list)

for student, group in students:
    groups[group].append(student)
 
print(groups)
# defaultdict(<class 'list'>, {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']})

print(groups[3])
# ['Petrov', 'Markov']

print(groups[2021])
# []