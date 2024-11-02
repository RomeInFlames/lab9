#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def negative():
    """
    Дать ответ.
    """
    print("Отрицательный")


def positive():
    """
    Дать ответ.
    """
    print("Положительный")


def test():
    """
    Определить число.
    """
    x = int(input("Число? "))
    if x < 0:
        negative()
    if x > 0:
        positive()


if __name__ == '__main__':
    test()
