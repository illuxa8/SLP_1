from .Classes.generator import ASCIIArtGenerator 
from .Classes.input import InputHandler
from .Data.data import color_mapping
def main():
    while(1):
        user_language = InputHandler.get_language()
        user_input = InputHandler.get_user_input()
        size = InputHandler.get_art_size()
        width = size[0]
        height = size[1]
        alignment = InputHandler.get_alignment()
        color = color_mapping[InputHandler.get_color()]
        ascii_art = ASCIIArtGenerator(user_input,color,width,height,alignment,user_language)
    
        ascii_art.generate_ascii_art()
        ascii_art.display_ascii_art()
        
        user_control = InputHandler.get_answer()
        if(user_control in ['N','n','no']):
            break
        