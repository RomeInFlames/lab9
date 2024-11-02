#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cylinder():
    """
    Рассчитать цилиндр.
    """
    r = int(input("Радиус цилиндра? "))
    l = int(input("Высота цилиндра? "))


    def circle():
        """
        Рассчитать площадь круга.
        """
        circle_cr = 6.28 * r
        return circle_cr


    command = input("Нужно ли вычислять только боковую поверхность? ")
    if command == "Да":
        p = 6.28 * r * l
        print(p)

    elif command == "Нет":
        p = 2 * circle() + 6.28 * r * l
        print(p)

if __name__ == '__main__':
    cylinder()

