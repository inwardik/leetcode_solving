import unittest
from i_to_ro import Solution

def test_ok_pytest():
    s = Solution()
    assert s.intToRoman(1) == 'I'
    assert s.intToRoman(4) == 'IV'
    assert s.intToRoman(5) == 'V'
    assert s.intToRoman(9) == 'IX'
    assert s.intToRoman(10) == 'X'
    assert s.intToRoman(40) == 'XL'
    assert s.intToRoman(50) == 'L'
    assert s.intToRoman(90) == 'XC'
    assert s.intToRoman(100) == 'C'
    assert s.intToRoman(400) == 'CD'
    assert s.intToRoman(500) == 'D'
    assert s.intToRoman(900) == 'CM'
    assert s.intToRoman(1000) == 'M'


class TestRoman(unittest.TestCase):
    def test_roman(self):
        s = Solution()
        self.assertEqual(s.intToRoman(1557), 'MDLVII')
        self.assertEqual(s.intToRoman(1234), 'MCCXXXIV')
        self.assertEqual(s.intToRoman(543), 'DXLIII')
        self.assertEqual(s.intToRoman(2222), 'MMCCXXII')
        self.assertEqual(s.intToRoman(1375), 'MCCCLXXV')
        self.assertEqual(s.intToRoman(33), 'XXXIII')
        self.assertEqual(s.intToRoman(38), 'XXXVIII')
        self.assertEqual(s.intToRoman(43), 'XLIII')
        self.assertEqual(s.intToRoman(48), 'XLVIII')

