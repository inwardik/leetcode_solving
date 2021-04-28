import unittest
import three_sum

class TestThreeSum(unittest.TestCase):
    def test_add(self):
        s = three_sum.Solution()
        # self.assertEqual(s.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertCountEqual(s.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertCountEqual(s.threeSum([-138, -349, 138, -21, -46, -198, -253, 243, -90, 286, -99, 40, -388, -273, 378, -87, 282, -197, 123, -239, -206, -396, 135, -325, -397, -343, 256, -273, -397, -340, 58, 234, 311, 241, -242, -33, 43, -361, 171, -276]), [[-138, -33, 171], [-273, 135, 138], [-197, -46, 243], [-253, -33, 286], [-90, -33, 123], [-325, 43, 282], [-340, 58, 282]])
        self.assertCountEqual(s.threeSum([160, 483, -110, 86, 381, 334, -36, 110, 27, -299, 0, 227, 436, 320, -294, 228, 171, -289, 159, -174, -70, -406, 450, -462, -409, -492, 113, 458, -205, -47]), [[-110, 0, 110], [-406, 86, 320]])
        self.assertCountEqual(s.threeSum([134, 339, -182, 177, -286, 92, -450, 404, -253, -441, -138, -435, 5, 361, 306, 55, -255, -331, 163, -500, -224, 395, -405, -316, -226, -181, -346, 15, -488, 68]), [[-226, 92, 134], [-182, 5, 177], [-255, 92, 163], [-450, 55, 395]])
        self.assertCountEqual(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]), [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]])
        




if __name__ == '__main__':
    unittest.main()