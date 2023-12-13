# main.py
from .test import TestCalculator
import unittest

def main():
   suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)

   runner = unittest.TextTestRunner()

   runner.run(suite)
   
if __name__ == "__main__":
    main()
