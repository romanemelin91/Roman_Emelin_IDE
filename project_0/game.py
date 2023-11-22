"""Игра угадай число"""

import numpy as np
    
number = np.random.randint(1, 101) #Загадываем число

#Создание логики игры, как мы угадываем число
#Количество попыток
count = 0

#Пишем цикл, где мы будем позволять вводить и угадывать числа
while True:
    count+=1
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    if predict_number > number:
        print("Число должно быть меньше!")
        
    elif predict_number < number:
        print("Число должно быть больше!")
        
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #Конец игры. Выход из бесконечного цикла
    