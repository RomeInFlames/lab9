#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Список работников.
workers = []


def add_worker(workers):
    # Запросить данные о работнике.
    name = input("Фамилия и инициалы? ")
    numb = input("Телефон? ")
    date = list(map(int, (input("Дата рождения? ")).split()))

    # Создать словарь.
    worker = {
        'name': name,
        'numb': numb,
        'date': date,
    }

    # Добавить словарь в список.
    workers.append(worker)
    # Отсортировать список в случае необходимости.
    if len(workers) > 1:
        workers.sort(key=lambda item: item.get('name', ''))

    return(workers)


def month_worker(workers):
    key_count1 = 0
    key_count2 = 0
    # Запросить искомый месяц.
    key_month = int(input("Месяц? "))

    # Найти соответствующих сотрудников.
    for key_count1, item in enumerate(workers):
        if key_month == workers[key_count1]["date"][1]:
            print(workers[key_count1])
            key_count2 += 1
    if key_count2 == 0:
        print('Сотрудников с указанными параметрами не найдено')
    return

def rezult():
    print("Отсортированный список:")
    for item in workers:
        print(item)

if __name__ == '__main__':
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        if command == "exit":
            break
        if command == "add":
            workers = add_worker(workers)
        if command == "month":
            month_worker(workers)
    rezult()