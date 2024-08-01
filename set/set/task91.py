def get_same_numbers(list_1: list[int], list_2: list[int]) -> list[int]:
    """функцию, которая получает на вход два списка чисел и возвращает одинаковые числа"""
    same_nambers = [i for i in list_1 if i in list_2]

    return same_nambers


def get_polydromes(list_num: list[int]) -> list[int]:
    """Функция вщзвращает список полиндромов"""
    list_pld = [i for i in list_num if str(i) == str(i)[::-1]]

    return list_pld


def get_unique_numbers(list_1: list[int], list_2: list[int]) -> list[int]:
    """Функция возвращает числа, которые есть или только в первом или только во втором"""
    # unique_numbers = [i for i in list_1 if i not in list_2]
    # for i in list_2:
    #     if i not in list_1:
    #         unique_numbers.append(i)

    return list(set(list_1) - set(list_2)) + list(set(list_2) - set(list_1))


print(get_same_numbers([1, 2, 3, 4], [3, 4, 5, 6]))
print(get_polydromes([121, 123, 131, 34543]))
print(get_unique_numbers([1, 2, 3, 4], [3, 4, 5, 6]))
