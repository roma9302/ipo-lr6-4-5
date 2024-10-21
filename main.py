"""
Написать программу, которая:
- Создаёт с помощью генератора списков, список случайных целых чисел от -50 до 50 размером 25 элементов.
- Находит количество положительных, отрицательных и нулевых элементов в списке.
- Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
- Выводит самое большое и самое маленькое значение
"""
import random

#счетчик 
counter_zero = 0
counter_minus = 0
counter_plus = 0

#хранение значений
list_minus = []
list_plus = []

# Генерация списка из 25 случайных чисел от -50 до 50
list1 = [random.randint(-50, 50) for x in range(25)]

#цикл счетчика 
for i in list1:
    if i < 0:
        counter_minus += 1
        list_minus.append(i)
    elif i > 0:
        counter_plus += 1
        list_plus.append(i)
    elif i == 0:
        counter_zero += 1

# Вычисление процентов
percent_minus = (counter_minus / 25) * 100 if counter_minus > 0 else 0
percent_plus = (counter_plus / 25) * 100 if counter_plus > 0 else 0
percent_zero = 100 - (percent_minus + percent_plus)

#min max
min_el=min(list1)
max_el=max(list1)


# Вывод результатов
print("список:", list1)
print("Количество нулей:", counter_zero)
print("Количество положительных чисел:", counter_plus)
print("Количество отрицательных чисел:", counter_minus)
print("Отрицательные числа:", list_minus)
print("Положительные числа:", list_plus)
print("Процент отрицательных чисел:", percent_minus)
print("Процент положительных чисел:", percent_plus)
print("Процент нулей:", percent_zero)
print("Минимальное значение:" ,min_el)
print("Максимальное  значение:" ,max_el )
