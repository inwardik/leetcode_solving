from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min((len(set(candyType)), int(len(candyType) / 2)))



def main():
    s = Solution()
    print(type(s.distributeCandies([])))


if __name__ == '__main__':
    main()