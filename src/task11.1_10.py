"""Напишите генератор, который принимает на вход последовательность чисел и генерирует квадраты этих чисел."""
import random

def square_generator(nums):
    for num in nums:
        yield num ** 2

square = square_generator([2, 3, 5, 6])

print(next(square))
print(next(square))
print(next(square))
print("_______")


"""Напишите генератор, который генерирует случайные числа в заданном диапазоне."""
def random_generator(start: int, end: int):
    while True:
        num_rand = random.randint(start, end)
        yield num_rand

rand = random_generator(20, 90)

print(next(rand))
print(next(rand))
print(next(rand))
print("_______")


"""Напишите генератор, который генерирует последовательность чисел по заданной формуле."""
def fun_generator(fun, num):
    while True:
        yield num
        num = fun(num)


"""Напишите генератор, который принимает на вход два списка и генерирует элементы, которые есть в обоих списках."""
def intersection_generator(lst1, lst2):
    for item in lst1:
        if item in lst2:
            yield item

