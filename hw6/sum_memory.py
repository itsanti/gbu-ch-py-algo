import sys


def sum_memory(obj, verbose=True):
    sum_mem = 0
    for item in obj:
        if item.startswith('__'):
            continue
        elif hasattr(obj[item], '__call__'):
            continue
        elif hasattr(obj[item], '__loader__'):
            continue
        else:
            sum_mem += sys.getsizeof(obj[item])
            if verbose:
                print(f'var = {item};\tclass = {type(obj[item])};\tvalue = {obj[item]};\tmem = {sys.getsizeof(obj[item])}')
        return f'sum memory {sum_mem}'
