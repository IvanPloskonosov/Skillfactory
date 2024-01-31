# numbers = '1 2 3 4 5 6 7'
#
# numbers_split = numbers.split()
# for x in numbers_split:
#     print(x)


# int_num = int(input("Введите целое число: ")) # вводим, например, 256
#
# print(int_num)
# # 256
# print(type(int_num)) # убеждаемся, что тип данных в переменной - int
# # <class 'int'>

# age = 25
# my_age = "I'm %d years old" % (age) # в шаблоне присутствует специальный символ %d
# print(my_age)

# pi = 31.4159265
# print ("%.4e" % (pi))

# day = 14
# month = 2
# year = 2012
#
# print("%d/%02d/%d" % (day, month, year))

# hours = 14
# minutes = 2
# secomds = 12
#
# print("%02d:%02d:%02d" % (hours, minutes, secomds))

# L = ["а", "б", "в", 1, 2, 3, 4]
# print(L[:3:-1])

# L = ['3.3', '4.4', '5.5', '6.6']
# print(list(map(float, L)))

# string = input("Введите числа через пробел:")
#
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(int, list_of_strings)) # cписок чисел
#
# print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка


# # все операции — деление строки по пробелам, преобразование к числам
# # и приведение объекта map к типу список, можно делать в одной строке
# L = list(map(float, input().split()))
#
# # обмениваем первое и последнее число
# # с помощью множественного присваивания
# L[0], L[-1] = L[-1], L[0]
#
# # находим сумму и добавляем её в конец списка
# L.append(sum(L))
#
# print(L)


# person = {} # с помощью фигурных скобок можно создать словарь
#
# # словарь заполняется по принципу — ключ:объект (через двоеточие)
# person = {'name' : 'Ivan Petrov'}
#
# # в него можно также добавлять новые объекты по ключу
# person['age'] = 25
# person['email'] = 'ivan_petrov@example.com'
# person['phone'] = '8(800)555-35-35'
#
# print(person)
# # {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}
# print(person.keys()) #Получение ключей
# print(person.values()) #Получение значений ключа


# d = {'day' : 22, 'month' : 6, 'year' : 2015}
#
# print("||".join(d.keys()))



# title = 'Алиса в стране чудес'
# author = 'Кэрролл'
# year = 1865
#
# book = {'title': title,
#         'author': author,
#         'year': int(year)}
#
# print(book)


# abit1 = {"ФИО" : 'Фадеев О.Е.', "Количество баллов" : 283, "Заявление" : True}
# abit2 = {"ФИО" : 'Дружинин И.Я.', "Количество баллов" : 278, "Заявление" : False}
# abit3 = {"ФИО" : 'Афанасьев Д.Н.', "Количество баллов" : 276, "Заявление" : True}
#
#
# abits = [abit1, abit2, abit3]
# abit4 = {"ФИО" : 'Popov Д.Н.', "Количество баллов" : 135, "Заявление" : True}
# abits.append(abit4)
# print(abits)

# text = input("Введите текст:")
# c = list(set(text))
#
# print("Количество уникальных символов:", len(c))


# abons = {"Иванов", "Петров", "Васильев", "Антонов"}
# debtors = {"Петров", "Антонов"}
# non_debtors = abons.difference(debtors)
# print(non_debtors)


# a = input("Введите первую последовательность чисел через пробел: ")
# b = input("Введите вторую последовательность чисел через пробел: ")
#
# a_set, b_set = set(a), set(b) # используем множественное присваивание
#
# a_and_b = a_set.intersection(b_set)
#
# print(a_and_b)


# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))


# a = 5
# b = 3+2
# print(id(a),id(b))
# print(id(a)-id(b))


# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
#
# print(list_id_before == list_id_after)

# N = 12345689
# print('3' in str(N) and '7' in str(N))


# N = 22345
# N_str = str(N)# преобразуем число в строку
# first_digit = int(N_str[0])# берём самый левый элемент строки и преобразуем его в число
# print(first_digit % 2 == 0)# выводим True в случае, если цифра делится на 2, иначе False


# list_1 = [1, 2]
#
# list_2 = [1, 2, 3]
# val = list_2.pop()
#
# print(id(list_1) == id(list_2))



# password = "dgh36gh7"
# answer = input()
#
# #В строку ниже вместо ??? необходимо написать условие, которое будем проверять, не забудьте удалить знаки ???
#
# if password == answer:
#     print("Пароль верен! Добро пожаловать.")
# else:
#     print("Вы ввели неверный пароль")





# name = input("Введите название на этикетке: ")
# if "Арорат" in name:
#     print("Нашлась подделка!", name)
# else:
#     print(f"Коньяк {name} не подделка")


# many = 2500
# cost = input("Введите стоимость кроссовок: ")
# if int(cost) <= int(many):
#     print("Вы можете купить эти кроссовки")
# else:
#     print("Увы, кроссовки слишком дорогие!")



# one = 12
# two = 30
# if one % 2 == 0 and two % 2 == 0:
#     print("Числа чётные")
# else:
#     print("Числа нечётные")

# one = 13;
# two = 30;
# print((one % 2 == 0) and (two % 2 == 0))


# x = int(input("Input X: "))
# y = int(input("Input Y: "))
# if x > 0 and y > 0:
#     print("Pervay chetvert'")
# if x > 0 and y < 0:
#     print("Chetvertay chetvert'")
# if x < 0 and y > 0:
#     print("Vtoray chetvert'")
# if x < 0 and y < 0:
#     print("Tretya chetvert'")



# speed = int(input("Input speed wind: "))
#
# if 1 <= speed <= 4:
#     print("Wind is weak")
# elif 5 <= speed <= 10:
#     print("Wind is moderate")
# elif 11 <= speed <= 18:
#     print("Wind is strong")
# elif speed >= 19:
#     print("Wind is hurricane")
# elif speed <= 0:
#     print("ERROR")




# number = input("Input number: ")
# string = str(number)
# if string == string[::-1]:
#     print("number - palindrom")
# else:
#     print("number - not palindrom")



# #спрашиваем какова темепратура
# temperature = int(input("Введите темературу за окном: "))
# if 20 <= temperature <= 30: #если температура в заданном диапазоне, то...
#     isRain = input("Есть осадки? - ")#спрашиваем есть ли осадки
#
#     if isRain == str("Да"):#если осадки есть, то...
#         print("Наденьте футболку, шорты и дождевик")
#     else:#если осадков нет, то...
#         print("Наденьте футболку и шорты")
#
# else: #если температура не в заданном диапазоне, то...
#     temperature2 = input("Температура выше 0 градусов? - ")#спрашиваем ниже ли температура ноля
#     if temperature2 == str("Нет"):# если температура выше ноля, то...
#         print("Наденьте пуховик")
#     else:#если же температура ниже ноля, то...
#         isRain2 = input("Есть осадки? - ")# спрашиваем, есть ли осадки
#         if isRain2 == str("Нет"):# если нет осадки, то...
#             print("Наденьте пальто")
#         else:# если же осадки есть, то...
#             isRain3 = input("Осадки сильные? - ")# спрашиваем, сильные ли осадки
#             if isRain3 == str("Нет"):# если осадки слабые, то...
#                 print("Наденьте пальто и дождевик")
#             else:# если осадки сильные, то...
#                 print("Наденьте пальто, резиновые сапоги и зонт")

# АЛЬТЕРНАТИВНОЕ РЕШЕНИЕ ЗАДАЧИ

# #Запрашиваем ввод температуры
# temperature = int(input("Input temperature: "))
#
# #для указания начальных статусов дождливости воспользуемся False или None
# rainy = None
# heavyRain = None
#
# #если температура <0 то про дождь спрашивать бессмысленно
# if temperature > 0:
#    rainy = input("Is rainy: ") == "yes"
# #если идет дождь спросим насколько он серьезный
#    if rainy:
#        heavyRain = input("Is heavy rain: ") == "yes"
#
#
# #реализуем логику по схеме
# decision = "Не решил что брать. Останусь дома."
# if (temperature) > 20 and (temperature < 30) :
#    if rainy:
#        decision = "Взять футболку шорты и дождевик"
#    else:
#        decision = "Взять футболку и шорты"
# elif temperature > 0:
#    if rainy:
#        if heavyRain:
#            decision = "Взять пальто, резиновые сапоги и зонт"
#        else:
#            decision = "Взять пальто и дождевик"
#    else:
#        decision = "Взять пальто"
# else:
#    decision = "Взять пуховик"
#
#
# #Выведем наше решение на экран
# print(decision)




# i = 1
# while i**2 < 1000:
#     i += 1
# print(i-1)

# n = 10
# i = 1
# while i ** 2 < n:
#     i += 1
# print(i)


# n = 10
# i = 0
# while i < n:
#     print('Hello')
#     i = i + 1


#Напишите программу, которая считает неотрицательные степени двойки до тех пор, пока
#это число не станет больше 10 000. В ответ запишите количество итераций, которые
#проделывает цикл.
# n = 2
# S = 0
# x = 0
# while n**x < 10000:
#     S += n
#     x += 1
# print(x)


#Олег положил тысячу рублей в банк под 8% годовых с ежегодной капитализацией процентов.
#Капитализация процентов означает, что проценты за каждый год прибавляются к сумме
#вклада и в следующем году также участвуют в начислении процентов.
#Определите, через сколько лет сумма на счете Олега составит не менее трёх тысяч рублей.
#Выведите на экран это число и запишите его в ответ.
# c = 1000
# x = 0
# while c < 3000:
#     c += (c*0.08)
#     x += 1
# print(c)
# print(x)



# employee = 5
# i = 1
# while i < employee:
#
#     if i > 1:
#         print('There are', i, 'people in the department')  # В отделе i человек
#     if i == 1:
#         print('There are', i, 'people in the department')  # В отделе i человек
#     i += 1




# S = 0  # заводим переменную счетчик, в которой мы будем считать сумму
# N = 5
#
# # заводим цикл for в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)


# S = 0
# N = 5
# for i in range(1, N + 1):
#     S = S + i
# print("Ответ: сумма равна: ", S)



# random_matrix = [
#    [9, 2, 1],
#    [2, 5, 3],
#    [4, 8, 5]
# ]
# min_value_rows = []
# min_index_rows = []
# max_value_rows = []
# max_index_rows = []
# for row in random_matrix:
#     min_index = 0
#     min_value = row[min_index]
#     max_index = 0
#     max_value = row[max_index]
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
# print("Minimal elements:", min_value_rows) # минимальные элементы
# print("Their indices:", min_index_rows) # их индексы
# print("Maximal elements:", max_value_rows) # максимальные элементы
# print("Their indices:", max_index_rows) # их индексы


# # поиск наибольшего числа (значения) в матрице и вывод этого числа
# test_matrix = [[1, 2, 3],
#                [7, -1, 2],
#                [123, 2, -1]
# ]
# max_value_rows = []
# max_index_rows = []
#
# for row in test_matrix:
#     max_value = 0
#     for index_col in range(len(row)):
#         if row[index_col] > max_value:
#             max_value = row[index_col]
# print(max_value)


# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")



# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")



# #подсчёт слов в тексте
#
# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
#
#
# wolds = 0
# in_word = False
# for char in text.split():
#     if char != ' ' and char != '\n' and in_word == False:
#         wolds += 1
#         in_word = False
# print(wolds)



# num = 12345
# digit_found = False
#
# while num != 0:
#     digit = num % 10
#     num = num // 10
#
#     if digit == 5:
#         digit_found = True
#         break
#
# if digit_found:
#     print("Цифра 5 найдена в числе")
# else:
#     print("Цифра 5 не найдена в числе")




# def hello_world():
#     print("Hello World")
#
# hello_world()



# def del_check(a, n):
#     if a % n == 0:
#         print(f"Number {n} delitel' number {a}")
#     else:
#         print(f"Number {n} not delitel' number {a}")
# del_check(50, 3)
# del_check(4, 2)




# def reverse_stair(n):
#     for i in range(n, 0, -1):
#         print("*" * i)
#
# reverse_stair(12)


# def get_multipliers(a):
#    count = 0
#    for n in range(1, a + 1):
#        if a % n == 0:
#            count += 1
#
#    return count
#
# print(get_multipliers(5))
# print(get_multipliers(4))



# def check_palindrome(str_):
#    str_ = str_.lower()
#    str_ = str_.replace(" ", "")
#
#    if str_ == str_[::-1]:
#        return True
#    else:
#        return False
#
# print(check_palindrome("test"))  # False
# print(check_palindrome("Кит на море не романтик"))  # True



# import time
#
# N = 100
#
# def decorator_time(fn):
#    def wrapper():
#        print(f"Запустилась функция {fn}")
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        print(f"Функция выполнилась. Время: {dt:.10f}")
#        return dt  # задекорированная функция будет возвращать время работы
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#     mean_pow_2 += pow_2()
#     mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / N:.10f}")



# def D(a, b, c):
#     return b**2 - 4*a*c
#
# def quadratic_solve(a, b, c):
#     if D(a, b, c) < 0:
#         return "Нет вещественных корней"
#     elif D(a, b, c) == 0:
#         return -b/(2*a)
#     else:
#         return (-b - D(a, b, c) ** 0.5) / (2*a), (-b + D(a, b, c) ** 0.5) / (2*a)
#
#
# print(quadratic_solve(2,3,1))



# # Напишите рекурсивную функцию, которая зеркально разворачивает число.
# # Предполагается, что число не содержит нули.
# def mirror_numbers(a, res=0):
#     return mirror_numbers(a // 10, res*10 + a % 10) if a else res
# print(mirror_numbers(000))


# # Напишите рекурсивную функцию, находящую минимальный элемент списка без использования
# # циклов и встроенной функции min().
# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])



# # Поработаем над более сложной рекурсивной функцией.
# # Сейчас попробуем реализовать функцию equal(N, S), проверяющую,
# # совпадает ли сумма цифр числа N с числом S.
# # При написании программы следует обратить внимание на то,
# # что, если S стала отрицательной, то необходимо сразу вернуть False.
# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return equal(N//10, S - N%10)
# print(equal(1, 1))




# yesno = input("""Введите Y, если хотите авторизоваться, или N,
# если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь не авторизован. Функция выполнена не будет")
#     return wrapper
#
# @is_auth
# def from_db():
#     print("some data from database")
#
# from_db()




# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# yesno = input("""Введите Y, если хотите авторизоваться, или N,
# если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# if auth:
#     username = input("Введите ваш username:")
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь не авторизован. Функция выполнена не будет")
#     return wrapper
#
# def has_access(func):
#     def wrapper():
#         if username in USERS:
#             print("Авторизован как", username)
#             func()
#         else:
#             print("Доступ пользователю", username, "запрещён")
#     return wrapper
#
# @is_auth
# @has_access
#
# def from_db():
#     print("some data from database")
#
# from_db()





# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower, L)))





# # (вес, рост)
# data = [
#    (82, 1.91),
#    (68, 1.74),
#    (90, 1.89),
#    (73, 1.79),
#    (76, 1.84)
# ]
#
# print(sorted(data, key=lambda x: x[0] / x[1]**2))
# print(min(data, key=lambda x: x[0] / x[1]**2))



