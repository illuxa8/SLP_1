class ASCIIArtGenerator:
    def __init__(self, user_input, art_color, width, height, alignment,language):
        self.user_input = user_input
        self.art_color = art_color
        self.width = width
        self.height = height
        self.alignment = alignment
        self.ascii_art = ""
        self.language = language

    def generate_ascii_art(self):
        input_lines = self.user_input.split('\n')
        max_length = max(len(line) for line in input_lines)

        self.ascii_art = [''] * len(self.language[' '])
        for i in range(len(self.language[' '])):
            for line in input_lines:
                if self.alignment == 'center':
                    line = line.center(max_length)
                elif self.alignment == 'right':
                    line = line.rjust(max_length)
                else:
                    line = line.ljust(max_length)

                for char in line:
                    char = char.upper()
                    if char in self.language:
                        self.ascii_art[i] += f'\x1b[{self.art_color}m{self.language[char][i]}\x1b[0m'
                    else:
                        self.ascii_art[i] += ' '

        self.ascii_art = '\n'.join(self.ascii_art)

    def display_ascii_art(self):
        print(self.ascii_art)

    def save_to_file(self):
        save_option = input("Save file? (Yes/No): ").lower()
        if save_option == 'так':
            filename = input("File name (з розширенням .txt): ")
            with open(filename, 'w') as file:
                file.write(self.ascii_art)
                print(f"ASCII-art was saved {filename}")