import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    for dict in items:
        if len(args) == 1:
            try:
                if dict[args[0]] is not None:
                    yield dict[args[0]]
            except:
                pass
        else:
            result = {}
            for index,value in enumerate(args):
                try:
                    if dict[args[index]] is not None:
                        result[value] = dict[args[index]]
                except:
                    pass
            yield result




# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
   for i in range(num_count):
       yield random.randint(begin, end)  #случайное число последовательности
