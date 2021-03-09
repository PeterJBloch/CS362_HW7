import FizzBuzz
import unittest

class Test_FizzBuzz(unittest.TestCase):
    def test_threes(self):
        self.assertEqual(FizzBuzz.FizzBuzz(3),"Fizz")
        self.assertEqual(FizzBuzz.FizzBuzz(6),"Fizz")
        self.assertNotEqual(FizzBuzz.FizzBuzz(5),"Fizz")
        return

    def test_fives(self):
        self.assertEqual(FizzBuzz.FizzBuzz(5),"Buzz")
        self.assertEqual(FizzBuzz.FizzBuzz(10),"Buzz")
        self.assertNotEqual(FizzBuzz.FizzBuzz(4),"Buzz")

    def test_both(self):
        self.assertEqual(FizzBuzz.FizzBuzz(15),"FizzBuzz")
        self.assertEqual(FizzBuzz.FizzBuzz(30),"FizzBuzz")
        self.assertNotEqual(FizzBuzz.FizzBuzz(5),"FizzBuzz")

if __name__ == "__main__":
    unittest.main()