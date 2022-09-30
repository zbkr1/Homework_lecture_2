""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 """

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")


"""Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number

def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)

num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")


"""Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму."""

print('\nВведите число')
n = int(input())
print('Введите число_2\n', end = '')
 
n = int(input())
lst = [round((1+1/1)**n) for n in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst))}')


""" Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. """

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)
def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=11
    return count
print('Number of elements: ', get_numbers(numbers))
x = int(input('Enter  position of first element: '))
y = int(input('Enter position of second element: '))
for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult) 


""" Задача №18: Реализовать алгоритм перемешивания списка. """

print('\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]')
from time import time

lister = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def mix_list(old: list) -> list:
    new = []
    while old:
        x = str(time()).split('.')[1]
        x = list(map(int, [x[0], x[-1]]))
        x = x[0] if x[0] <= x[1] else x[1]
        if x > len(old)-1:
            new.append(old.pop(0))
        else:
            new.append(old.pop(x))
    return new

lister = mix_list(lister)
print(lister)