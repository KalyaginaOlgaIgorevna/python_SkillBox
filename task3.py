# task3.py
#Если вы введете "5 2 9", то программа выведет 5, так как после сортировки числа будут иметь вид [2, 5, 9], и среднее число равно 5.

# Считываем три числа и преобразуем их в список
numbers = list(map(int, input().split()))

# Сортируем список
numbers.sort()

# Выводим среднее число (второй элемент отсортированного списка)
print(numbers[1])

