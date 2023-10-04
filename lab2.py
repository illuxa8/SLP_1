# Функція для додавання
def add(x, y):
    return x + y

# Функція для віднімання
def subtract(x, y):
    return x - y

# Функція для множення
def multiply(x, y):
    return x * y

# Функція для ділення
def divide(x, y):
   
    return x / y

# Перевірка дійсності введеного оператора
while True:
    operator = input("Введіть операцію (+, -, *, /): ")
    if operator in ('+', '-', '*', '/'):
        break
    else:
        print("Помилка! Введений оператор не є дійсним. Спробуйте ще раз.")

