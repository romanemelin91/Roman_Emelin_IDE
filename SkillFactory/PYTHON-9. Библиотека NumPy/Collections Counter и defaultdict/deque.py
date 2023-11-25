#Создадим пустой дек (deque). Для этого сначала импортируем эту структуру данных из модуля collections,
# а затем создадим её пустой экземпляр:
from collections import deque
dq = deque()
print(dq)
# deque([])

clients = deque()
clients.append('Ivanov')
clients.append('Petrov')
clients.append('Smirnov')
clients.append('Tikhonova')
print(clients)
# deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])

#Объект deque поддерживает индексацию по элементам:

print(clients[2])
# Smirnov

#Освободилось два оператора — заберём двоих человек из начала очереди с помощью popleft:

first_client = clients.popleft()
second_client = clients.popleft()
 
print("First client:", first_client)
print("Second client:", second_client)
print(clients)
# First client: Ivanov
# Second client: Petrov
# deque(['Smirnov', 'Tikhonova'])

#Как видите, первые элементы исчезли из очереди. 
#Функции pop и popleft возвращают тот элемент, который они удаляют (последний или первый соответственно).

#Вдруг появился VIP-клиент. Для него тоже нет свободного оператора, но добавить его нужно в начало очереди с помощью appendleft:
clients.appendleft('Vip-client')
 
print(clients)
# deque(['Vip-client', 'Smirnov', 'Tikhonova'])

#Последний клиент в очереди устал ждать и отменил вызов. Удалим его с помощью pop:

tired_client = clients.pop()
print(tired_client, "left the queue")
print(clients)
# Tikhonova left the queue
# deque(['Vip-client', 'Smirnov'])

#С помощью pop всегда удаляется последний элемент из дэка. 
#Чтобы удалить конкретный элемент по индексу, необходимо воспользоваться встроенной конструкцией del:

clients = deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])
print(clients)
# deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])
del clients[2]
print(clients)
# deque(['Ivanov', 'Petrov', 'Tikhonova'])

#Создадим очередь из клиентов магазинчика на заправке и добавим в неё сразу всех туристов,
# приехавших на экскурсионном автобусе, с помощью extend:

# В скобках передаём список при создании deque,
# чтобы сразу добавить все его элементы в очередь
shop = deque([1, 2, 3, 4, 5])
print(shop)
# deque([1, 2, 3, 4, 5])
shop.extend([11, 12, 13, 14, 15, 16, 17])
print(shop)
# deque([1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16, 17])

#Если вдруг у турфирмы имеется договорённость с магазином, что клиенты турфирмы обслуживаются вне очереди, 
#добавим их в начало той же очереди с помощью extendleft:

shop = deque([1, 2, 3, 4, 5])
print(shop)
# deque([1, 2, 3, 4, 5])
shop.extendleft([11, 12, 13, 14, 15, 16, 17])
print(shop)
# deque([17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5])

#ОЧЕРЕДЬ С ОГРАНИЧЕННОЙ МАКСИМАЛЬНОЙ ДЛИНОЙ

#При создании очереди можно также указать её максимальную длину с помощью параметра maxlen. 
#Сделать это можно как при создании пустой очереди, так и при создании очереди от заданного итерируемого объекта:

limited = deque(maxlen=3)
print(limited)
# deque([], maxlen=3)
 
limited_from_list = deque([1,3,4,5,6,7], maxlen=3)
print(limited_from_list)
# deque([5, 6, 7], maxlen=3)



