import art
from termcolor import colored
import textwrap

def main():
    text = input("Введіть слово або фразу: ")
    custom_characters = input("Введіть символи для ASCII-арту (наприклад, '@', '#', '*'): ")
    width = int(input("Введіть ширину ASCII-арту: "))
    height = int(input("Введіть висоту ASCII-арту: "))
    ascii_art = art.text2art(text, font='block')
    print("Доступні кольори: червоний, синій, зелений, жовтий, білий")
    selected_color = input("Виберіть колір для тексту: ")
    
    colors = {
        'червоний': 'red',
        'синій': 'blue',
        'зелений': 'green',
        'жовтий': 'yellow',
        'білий': 'white',
    }
    
    if selected_color in colors:
        text_color = colors[selected_color]
    
        # Вирівнення ASCII-арту для зручності читання
        wrapped_ascii_art = textwrap.fill(ascii_art, width=width)
    
        # Виведення ASCII-арту з обраними символами, кольором та вирівнянням
        colored_ascii_art = colored(wrapped_ascii_art, text_color, attrs=['bold'])
        print(colored_ascii_art)
    
        
        save = input("Зберегти цей ASCII-арт у файл? (Так/Ні): ").strip().lower()
    
        if save == "так":
            file_name = input("Введіть ім'я файлу для збереження (з розширенням .txt): ")
            with open(file_name, 'w') as file:
                file.write(wrapped_ascii_art)
                print(f"ASCII-арт збережено у файлі {file_name}")
        else:
            print("Збереження скасовано.")
    else:
        print("Обраний колір не існує. Спробуйте ще раз.")
    