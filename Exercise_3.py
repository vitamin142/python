#       3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#       Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number_n = int(input('Введите число n: '))
total = (number_n + int(str(number_n) + str(number_n)) + int(str(number_n) + str(number_n)+ str(number_n)))
print('Сумма чисел n + nn + nn =', total)
