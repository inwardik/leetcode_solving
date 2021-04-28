import random
import string
class Solution:
    def substr0(self, input_string):
        if input_string == '':
            return 0
        if len(set(input_string)) == 1:
            return 1
        max_len = 0
        for i in range(len(input_string)):
            for j in range(i+1, len(input_string)):
                chank = input_string[i:j+1]
                if len(chank) == len(set(chank)) and len(chank) > max_len:
                    max_len = len(chank)
        return max_len

    def substr(self, input_string):
        letters = {}
        max_len = 0
        uniqual_chain = 0
        for i, letter in enumerate(input_string)
            if letter in letters:
                uniqual_chain = 0
                distance_eq_letter = i - letters[letter]
                if distance_eq_letter > max_len:
                    max_len = distance_eq_letter
            else:
                uniqual_chain += 1
                if uniqual_chain > max_len:
                    max_len = uniqual_chain



            letters['letter'] = i


        


s = Solution()
