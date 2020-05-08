"testing for custom fmod python function "
"Tested Software Metrics-pylint,mypy,pytest"
import unittest
import math
from math import fmod

class TestFmodMath(unittest.TestCase):
    "Testing for fmod "

    def test_param_to_be_correct(self):
        "params correct"
        expected = 1.0
        #test_info = (17, 4)
        #result = math.fmod(test_info)
        self.assertEqual(math.fmod(17, 4),expected)

    def test_missing_param(self):
         "mising params"
         with self.assertRaises(TypeError):
             self.assertEqual(custom_fmod(), True)
    
    def test_params_to_be_wrong(self):
     "params-wrong "
     with self.assertRaises(TypeError):
         custom_fmod({})
    
    def test_params_to_be_empty(self):
        "params empty"
        with self.assertRaises(TypeError):
            self.assertEqual(custom_fmod(''), True)
            self.assertEqual(custom_fmod([]), True)

def custom_fmod():
    "my fmod"
    if not float:
        raise ValueError("Fload or integer needed")
    if not isinstance():
      raise TypeError('set or list is required')
    return math.fmod(float)

if __name__ == '__main__':
    unittest.main()