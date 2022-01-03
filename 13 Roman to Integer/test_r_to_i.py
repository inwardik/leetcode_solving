import unittest
import r_to_i

def test_ok_pytest():
    sol = r_to_i.Solution()
    assert sol.romanToInt('I') == 1
    assert sol.romanToInt('IV') == 4
    assert sol.romanToInt('V') == 5
    assert sol.romanToInt('IX') == 9
    assert sol.romanToInt('X') == 10
    assert sol.romanToInt('XL') == 40
    assert sol.romanToInt('L') == 50
    assert sol.romanToInt('XC') == 90
    assert sol.romanToInt('C') == 100
    assert sol.romanToInt('C') == 100
    assert sol.romanToInt('CD') == 400
    assert sol.romanToInt('D') == 500
    assert sol.romanToInt('CM') == 900
    assert sol.romanToInt('M') == 1000
    

class TestRoman(unittest.TestCase):
    def test_ok(self):
        sol = r_to_i.Solution()
        self.assertEqual(sol.romanToInt('MDLVII'), 1557)
        self.assertEqual(sol.romanToInt('MCCXXXIV'), 1234)
        self.assertEqual(sol.romanToInt('DXLIII'), 543)
        self.assertEqual(sol.romanToInt('MMCCXXII'), 2222)
        self.assertEqual(sol.romanToInt('MCCCLXXV'), 1375)
        self.assertEqual(sol.romanToInt('XXXIII'), 33)
        self.assertEqual(sol.romanToInt('XXXVIII'), 38)
        self.assertEqual(sol.romanToInt('XLIII'), 43)
        self.assertEqual(sol.romanToInt('XLVIII'), 48)



