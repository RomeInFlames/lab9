#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    """
    Ввод данных.
    """
    x1 = input("Введите данные ")
    return x1


def test_input(x):
    """
    Проверка.
    """
    testing_rez = True
    try:
        b = int(x1)
    except ValueError:
        testing_rez = False
    print(testing_rez)
    return testing_rez


def str_to_int(x):
    """
    Проведение преобразования.
    """
    c = int(x1)
    return c


def print_int(c):
    """
    Вывод значения.
    """
    print(c)

x2 = get_input()
if test_input(x2) == True:
    print_int(str_to_int(x2))
