#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def endless_0():
    """
    Перемножение значений до введения "0".
    """
    last_number = 1
    key_number = 1

    while last_number != 0:
        number = str(input())
        n = 0

        while n < len(number) and last_number != 0:
            key_number *= last_number
            last_number = int(number[n])
            n += 1

    return key_number


print("Итоговое значение: ", endless_0())





