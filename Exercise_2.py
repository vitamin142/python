#   2. Пользователь вводит время в секундах. Переведите время в часы, минуты
#      и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
time_of_day = int(input('Введите время суток в секундах'))
print('В секундах', time_of_day)
hours = (time_of_day // 3600)
minutes = (time_of_day - hours * 3600) // 60
seconds = (time_of_day - (hours * 3600 + minutes * 60))
print(f'Время в формате чч:мм:сс будет, {hours}:{minutes}:{seconds}')