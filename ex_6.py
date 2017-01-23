#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gen import gen_random
from librip.iterators import Unique as unique

path = str(sys.argv[1])

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path, encoding='cp1251') as f:
    data = json.load(f)



# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов


@print_result
def f1(arg):
    return list(sorted(unique([d['job-name'] for d in arg], ignore_case=True)))


@print_result
def f2(arg):
    return list(filter(lambda s: s.startswith('программист'), arg))



@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    salary = gen_random(100000, 200000, len(arg))
    return list(zip(arg, salary))

#python C:\Users\lunma\Desktop\Python_Labs\Lab4\lab_4-master\ex_6.py C:\Users\lunma\Desktop\Python_Labs\Lab4\lab_4-master\data_light_cp1251.json

with timer():
    f4(f3(f2(f1(data))))

#chcp 65001
#set PYTHONIOENCODING=utf-8
#python C:\Users\lunma\Desktop\Python_Labs\Lab4\lab_4-master\ex_6.py C:\Users\lunma\Desktop\Python_Labs\Lab4\lab_4-master\data_light_cp1251.json
f1