import calc as cl
import unittest
from calculator import *

class TestCalculatorArea(unittest.TestCase):
    
    def Test_1(self):
        self.assertEqual(cl.division(4, 2), 2)
        self.assertEqual(cl.substraction(4, 2), 2)

y = TestCalculatorArea()      
y.Test_1()
n = value1
print(n)