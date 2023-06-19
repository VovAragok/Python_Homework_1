# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

ticket_id = int(input(" Введите номер билета: "))
half_ticket = len(str(ticket_id))//2
temp = 0
sum_1 = 0
sum_2 = 0

while ticket_id > 0:
    if temp < half_ticket:
        sum_1 += (ticket_id % 10)
        temp += 1
        ticket_id //= 10
    else:
        sum_2 += ticket_id % 10
        ticket_id //= 10
if sum_1 == sum_2:
    print("Yes")
else:
    print("No")


ticket_id = (input(" введите номер билета: "))
half_ticket = len(str(ticket_id))//2
temp = 0
sum_1 = 0
sum_2 = 0
for i in ticket_id:
    if temp < half_ticket:
        sum_1 += int(i)
        temp += 1
    else:
        sum_2 += int(i)
if sum_1 == sum_2:
    print("Yes")
else:
    print("No")