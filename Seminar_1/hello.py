# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры:*
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# print ("Введите 1 число")
# a = int(input () )
# print ("Введите 2 число")
# b = int (input ())

# if a*a == b or b*b ==a :
#     print ("ДА")
# else:
#     print ("НЕТ")

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# list = input("Add 5 value: ").split(", ")
# max = max(list)
# print(list,"YES",max)
# value = int(input())
# revers = 0
# while value != 0:
#     revers = revers * 10 + (value % 10)
#     value //= 10
# print(revers)

# a, b = int(input()), int(input())
# c, d = int(input()),int(input())
# ab = 0
# cd = 0
# if a > b:
#     ab = b
# else:
#     ab = a
# if c > d:
#     cd = d
# else:
#     cd = c
# if ab < cd:
#     print(ab)
# else:
#     print(cd)


a, b, c = int(input()), int(input()), int(input())
sum = 0
if a > 0:
    sum += a
if b > 0:
    sum += b
if c > 0:
    sum += c
print(sum)
