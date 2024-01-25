# task6.py
domain = input().split('.') # Считываем доменное имя и разбиваем его на части по точкам
for part in reversed(domain): # Перебираем части в обратном порядке
    print(part) # Выводим каждую часть домена
# К примеру введете www.example.com  