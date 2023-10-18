import art
from termcolor import colored
import textwrap

# Попросіть користувача ввести слово або фразу
text = input("Введіть слово або фразу: ")

# Попросіть користувача ввести символи для створення ASCII-арту
custom_characters = input("Введіть символи для ASCII-арту (наприклад, '@', '#', '*'): ")

# Попросіть користувача ввести розмір ширини та висоти ASCII-арту
width = int(input("Введіть ширину ASCII-арту: "))
height = int(input("Введіть висоту ASCII-арту: "))

# Створіть ASCII-арт з вказаними символами та розмірами
ascii_art = art.text2art(text, font='block')

# Попросіть користувача вибрати колір тексту
print("Доступні кольори: червоний, синій, зелений, жовтий, білий")
selected_color = input("Виберіть колір для тексту: ")

# Визначте колір тексту на основі вибору користувача
colors = {
    'червоний': 'red',
    'синій': 'blue',
    'зелений': 'green',
    'жовтий': 'yellow',
    'білий': 'white',
}

if selected_color in colors:
    text_color = colors[selected_color]

    # Вирівняйте ASCII-арт для зручності читання
    wrapped_ascii_art = textwrap.fill(ascii_art, width=width)

    # Виведіть ASCII-арт з обраними символами, кольором та вирівнянням
    colored_ascii_art = colored(wrapped_ascii_art, text_color, attrs=['bold'])
    print(colored_ascii_art)

    # Попросіть користувача підтвердити збереження або відмінити
    save = input("Зберегти цей ASCII-арт у файл? (Так/Ні): ").strip().lower()

    if save == "так":
        # Попросіть користувача ввести ім'я файлу для збереження
        file_name = input("Введіть ім'я файлу для збереження (з розширенням .txt): ")

        # Збережіть ASCII-арт у текстовому файлі
        with open(file_name, 'w') as file:
            file.write(wrapped_ascii_art)
            print(f"ASCII-арт збережено у файлі {file_name}")
    else:
        print("Збереження скасовано.")
else:
    print("Обраний колір не існує. Спробуйте ще раз.")
