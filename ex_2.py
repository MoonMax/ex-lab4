#!/usr/bin/env python3
from librip.gen import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 2, 2, 2, 2, 1, 4, 2, 4, 1, 3, 3]
data2 = gen_random(1, 3, 10)

# Реализация задания 2

print("Итератор со списком data1")
myList = Unique(data1)
for i in myList:
    print(i, end = " ")

print("\nИтератор с генератором случайных чисел")
myList = Unique(data2)
for i in myList:
    print(i, end = " ")


print("\nИтератор с игнорированием регистров")
myList = Unique(['hello', 'mom', 'HELLO', 'dad'], ignore_case=False)
for i in myList:
    print(i, end = " ")

print("\nИтератор без игнорирования регистров")
myList = Unique(['hello', 'mom', 'HELLO', 'dad'], ignore_case=True)
for i in myList:
    print(i, end = " ")