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

while True:
    # Перевірка дійсності введеного оператора
    while True:
        operator = input("Введіть операцію (виберіть одне з: '+', '-', '*', '/'): ").lower()
        if operator in ('+', '-', '*', '/'):
            break
        else:
            print("Помилка! Введена операція не є дійсною. Спробуйте ще раз.")

    # Введення чисел від користувача
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    # Вибір операції та виклик відповідної функції
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)

    # Виведення результату
    print(f"Результат: {result}")

    # Питання користувачу про продовження
    again = input("Бажаєте виконати ще одне обчислення? (так/ні): ").lower()
    if again != 'так':
        if again != 'ні':
            print("Помилка! Введіть 'так' або 'ні'.")
        else:
            break   
