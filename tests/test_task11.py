import pytest
from src.task11.1_10.py import intersection_generator


#"""Напишите тесты на pytest для генератора из задания 4. Тестами покройте граничные случаи."""

def test_intersection_generator():
    list1 = [1, 2, 3, 4, 9]
    list2 = [4, 5, 6, 1]
    generator = intersection_generator([list1, list2])
    assert next(generator) == 1
    assert next(generator) == 4