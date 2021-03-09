import LeapYear
import unittest

class Test_FizzBuzz(unittest.TestCase):
    def test_fours(self):
        self.assertEqual(LeapYear.LeapYear(4),True)
        self.assertEqual(LeapYear.LeapYear(8),True)
        self.assertEqual(LeapYear.LeapYear(3),False)

    def test_hundreds(self):
        self.assertEqual(LeapYear.LeapYear(200),False)
        self.assertEqual(LeapYear.LeapYear(300),False)

    def test_fourhundreds(self):
        self.assertEqual(LeapYear.LeapYear(400),True)
        self.assertEqual(LeapYear.LeapYear(2000),True)
        self.assertEqual(LeapYear.LeapYear(2100),False)

    


if __name__ == "__main__":
    unittest.main()