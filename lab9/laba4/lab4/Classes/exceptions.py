class IncorrectArgumentException(Exception):
     def __init__(self, num2):
        self.num2 = num2
        super().__init__()

        