# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


n = int(input("Введите число "))
result = 0
while n > 0:
    result = result + n % 10
    n = n // 10

print(result)


n = input("введите число ")
result = 0
for i in n:
    result += int(i)
print(result)
