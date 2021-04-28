import unittest
from st import Solution

class TestSolution(unittest.TestCase):
    def test_str(self):
        s = Solution()
        self.assertEqual(s.substr('abcabcbb'), 3)
        self.assertEqual(s.substr('abadesde'), 5)
        self.assertEqual(s.substr('aaaaa'), 1)
        self.assertEqual(s.substr('ababab'), 2)
        self.assertEqual(s.substr('abcadaabcde'), 5)
        self.assertEqual(s.substr('drngbguykmanzwsjuydiuhavdvkbajjlafrotwydsghzgskdmgbiipmhcmxyffjlxiodxrlfpikdayjnpdgjmvujjbvlymvgwjfx'), 14)
        self.assertEqual(s.substr('lsvcdpgtelnjwdusjmzerpdzhcdaasnkfrymcmimoypeoppieyopeuiaecanrkvxhafndrkrvqteuuxyqskrvlnlwetlhatqzsrj'), 12)
        self.assertEqual(s.substr('nithgqpawnfyuofdlpblhyjblluopfaiqlomrjkzskrlojkbny'), 13)
        self.assertEqual(s.substr('dwmrtzyfyfgezjczccwphqbkmljrplcntbkvqohhdivovggzicyoabwbgbfhvorwsmpqqamjcrbbwvtdbhoxikloltlfbfkqdaruoecddtvpwdarkynmtdanaoixladzjtfrqzykrjygpvziuccyza'), 13)
        self.assertEqual(s.substr('wuulbeynhuounhc'), 8)
        self.assertEqual(s.substr('okixpppyunxansl'), 6)



if __name__ == '__main__':
    unittest.main()