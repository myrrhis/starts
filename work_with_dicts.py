from random import randint


def add_print_del_items(array):
    dictionary = {}
    for key, value in array:
        if not dictionary.get(key):
            dictionary[key] = value
    iterated_dict = dict(dictionary)
    for i in iterated_dict:
         print(i, dictionary[i])
        del dictionary[i]


def check_element_repeat(array, repeat_number):
    dictionary = {}
    for key in array:
        if dictionary.get(key):
            dictionary[key] += 1
        else:
            dictionary[key] = 1
        result = []
        for key, value in dictionary.items():
            if value >= repeat_number:
                result.append((key, value))
    return result


array = [(i, f'Значение {i}') for i in range(100)]
repeat_elements = [randint(1, 100) for _ in range(100)]

add_print_del_items(array)
print(check_element_repeat(repeat_elements, 5))
