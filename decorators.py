from collections import Iterable

def print_result(function_to_decorate):
    def decorated_function(*args, **kwargs):
        print(function_to_decorate.__name__)
        result = function_to_decorate(*args, **kwargs)
        if isinstance(result, str):
            print(result)
        elif isinstance(result, dict):
            for k, v in result.items():
                print(k, '=', v)
        elif isinstance(result, Iterable):
            [print(i) for i in result]
        else:
            print(result)
        return result
    return decorated_function
# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2
