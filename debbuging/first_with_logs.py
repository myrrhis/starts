import logging


def comparison(main_string, substring):
    flag = 0  # подсчет по количеству элементов, которые уже совпали
    p = 0  # индекс для подстроки
    s = 0  # индекс для строки
    remember_s = 0  # индекс для строки, с которого начинаем, если слетает последовательность

    while (p <= (len(substring) - 1)) and (s <= (len(main_string) - 1)):
        if flag < len(substring):
            if (substring[p] != main_string[s]) and (flag == 0):
                flag = 0
                s += 1
            elif (substring[p] != main_string[s]) and (flag > 0):
                flag = 0
                s = remember_s
                p = 0
            else:
                flag += 1
                p += 1
                s += 1
                remember_s = s
        else:
            if flag < 0:
                logging.error(f'Флаг равен {flag}')
            break
    assert flag > 0
    return False if flag < len(substring) else True


print(comparison(input(), input()))
