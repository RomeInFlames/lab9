#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    """
    Ввод данных.
    """
    x = input("Введите данные ")
    return x


def test_input(x):
    """
    Проверка.
    """
    testing_rez = True
    try:
        b = int(x)
    except ValueError:
        testing_rez = False
    print(testing_rez)
    return testing_rez


def str_to_int(x):
    """
    Проведение преобразования.
    """
    c = int(x)
    return c


def print_int(c):
    """
    Вывод значения.
    """
    print(c)

xx = get_input()
if test_input(xx) == True:
    print_int(str_to_int(xx))