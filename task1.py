# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите число: "))
print_number = number
result = 0
while number >= 1:
    result = result + number % 10
    number = number // 10
print(f'Сумма чисел числа {print_number} = {result}')