from itertools import chain

#Напишите генераторное выражение, которое возвращает кубы четных чисел от 0 до 10.

cube = (x ** 3 for x in range(0, 11) if x % 2 ==0)
print(list(cube))

"""Напишите функцию, которая принимает список чисел и возвращает сумму 
квадратов положительных чисел в этом списке. Используйте для этого генераторное выражение."""


def get_sum_of_squares_of_positive_numbers(list_num: list[int]) -> int:
    squares_of_positive_num = (num*num for num in list_num if num > 0)
    return sum(squares_of_positive_num)


print(get_sum_of_squares_of_positive_numbers([-1, 6, -9, 1, 10]))

"""Напишите генераторное выражение, которое возвращает буквы строки "hello", но только если они являются гласными."""

vowel = (letter for letter in "hello" if letter in "euoia")
print(list(vowel))

"""Найдите среднее арифметическое всех чисел, кратных 3 или 5, в заданном диапазоне."""
num = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0]
count_num = len(num)
sr_arif = sum(num) / count_num
print(sr_arif)

""""Объедините несколько списков в один список, учитывая возможные дубликаты элементов."""

list1 = [1, 2, 3, 4, 9]
list2 = [4, 5, 6, 1]
combined_list = list(set(chain(list1, list2)))

print(combined_list)


"""Дан список словарей. Отфильтруйте его по ключу age  и значению 30."""
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]

filt_age = (filter(lambda man: man["age"] == 30, people))

print(list(filt_age))
