import FizzBuzz
import unittest

class Test_FizzBuzz(unittest.TestCase):
    def test_threes(self):
        self.assertEqual(FizzBuzz.FizzBuzz(3),"Fizz")
        self.assertEqual(FizzBuzz.FizzBuzz(6),"Fizz")
        self.assertNotEqual(FizzBuzz.FizzBuzz(5),"Fizz")
        return

if __name__ == "__main__":
    unittest.main()