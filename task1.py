# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint
n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
first = [randint(0, 10) for i in range(n)]
print(first)
second = [randint(0, 10) for i in range (m)]
print(second)

first = set(first)
print(first)
second = set(second)
print(second)

result = first.intersection(second)
print(sorted(result))