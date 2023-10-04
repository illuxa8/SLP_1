import math

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
    if y == 0:
        return "Ділення на нуль неможливе"
    return x / y

# Функція для піднесення до степеня
def power(x, y):
    return x ** y

# Функція для квадратного кореня
def square_root(x):
    if x < 0:
        return "Неможливо взяти квадратний корінь від від'ємного числа"
    return math.sqrt(x)

# Функція для залишку від ділення
def modulo(x, y):
    if y == 0:
        return "Ділення на нуль неможливе"
    return x % y

# Змінна для зберігання значення пам'яті
memory = None

while True:
    # Перевірка дійсності введеного оператора
    while True:
        operator = input("Введіть операцію (виберіть одне з: '+', '-', '*', '/', '^', '√', '%', 'M+', 'MR'): ").lower()
        if operator in ('+', '-', '*', '/', '^', '√', '%', 'm+', 'mr'):
            break
        else:
            print("Помилка! Введена операція не є дійсною. Спробуйте ще раз.")

    if operator == 'm+':
        # Зберігання результату в пам'яті
        memory = result if 'result' in locals() else None
    elif operator == 'mr':
        # Отримання значення з пам'яті
        if memory is not None:
            print(f"Значення з пам'яті: {memory}")
        else:
            print("Пам'ять порожня")

    elif operator in ('+', '-', '*', '/', '^', '%'):
        # Введення чисел від користувача (десяткові числа)
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
        elif operator == '^':
            result = power(num1, num2)
        elif operator == '%':
            result = modulo(num1, num2)
        # Виведення результату з точністю до двох знаків після коми
        print(f"Результат: {result:.2f}")

    elif operator == '√':
        # Введення числа для обчислення квадратного кореня
        num1 = float(input("Введіть число для обчислення квадратного кореня: "))

        # Вибір операції та виклик відповідної функції
        result = square_root(num1)
        if isinstance(result, str):
            print(result)
        else:
            # Виведення результату з точністю до двох знаків після коми
            print(f"Результат: {result:.2f}")

    # Питання користувачу про продовження
    again = input("Бажаєте виконати ще одне обчислення? (так/ні): ").lower()
    if again != 'так':
        if again != 'ні':
            print("Помилка! Введіть 'так' або 'ні'.")
        else:
            break
