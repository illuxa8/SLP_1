from .exceptions import IncorrectArgumentException 
from ..Data.languages import *

class InputHandler:
    def get_user_input():
        input_value = input("Enter your phrase: ")
        if input_value.isalpha():
            return input_value
        else:
            raise IncorrectArgumentException("Input must contain only alphabetic characters.")
        


    def get_art_size():
        input_width = input("Width ASCII-art (1-100): ")
        input_height = input("Height ASCII-аrt (1-100): ")

        if input_width.isdigit() and input_height.isdigit():
            width = int(input_width)
            height = int(input_height)
        else:
            raise IncorrectArgumentException()
        
        result = [width, height]
        return result

    def get_alignment():
        input_value = input("text-align (left, center, right): ").lower()
        if (input_value.isalpha() and input_value in ['left', 'center', 'right']):
            return input_value
        else:
            raise IncorrectArgumentException()
    
    def get_color():
        input_value = input("Color ASCII-аrt ['@'(чорний), '#'(сірий), '*'(білий)]: ")
        if input_value in ['@', '#', '*']:
            return input_value
        else:
            raise IncorrectArgumentException()
        

    def get_language():
        input_value = input("language ASCII-art [eng,ukr]: ")
        if input_value == 'eng' or input_value == 'ukr':
            if(input_value =='eng'):
                return english_font
            else:
                return ukraine_font
        else:
            raise IncorrectArgumentException()
        
    def get_answer():
       user_control = input('continue? Y N: ')
       if user_control in ['Y', 'y', 'yes','N','n','no']:
           return user_control
       else:
           raise IncorrectArgumentException()


