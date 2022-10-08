# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

import random
first_list=[]
for i in range(10):
    first_list.append(random.randint(1,11))
print(f"Исходный список: {first_list}")
second_list = [ i for i in first_list if first_list.count (i) == 1]
print(f"Список из неповторяющихся элементов исходного списка: {second_list}")