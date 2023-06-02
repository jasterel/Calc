import time
from threading import Thread

run = True

# Addition function
def addition(a, b):
    return a + b

# Subtraction function
def subtraction(a, b):
    return a - b

# Multiplication function
def multiplication(a, b):
    return a * b

# Division function
def division(a, b):
    return a / b

# Main calculator function
def calculator():
    operation = input("Выберите операцию (+, -, *, /): ")

    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))

    if operation == "+":
        result = addition(num1, num2)
    elif operation == "-":
        result = subtraction(num1, num2)
    elif operation == "*":
        result = multiplication(num1, num2)
    elif operation == "/":
        result = division(num1, num2)
    else:
        print("Напишите знак действия!")
        return

    print("Результат:", int(result))

# Calling the calculator function
calculator()

# Запуск функции ticker в отдельном потоке.
# Параметр daemon=True нужен чтобы
# дочерний поток умирал вместе с основным
# в случае внештатного выхода.
while run:
    command = input('Для выхода введите "exit"\n')
    if command.lower() == 'exit':
        run = False