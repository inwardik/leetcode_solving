import string
class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        monthes = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        rep_day = (''.join([d for d in day if d in string.digits])).zfill(2)
        rep_month = str(monthes.index(month)+1).zfill(2)
        result = f'{year}-{rep_month}-{rep_day}'
        return result
        

s = Solution()
assert s.reformatDate("20th Oct 2052") == "2052-10-20"
assert s.reformatDate("6th Jun 1933") == "1933-06-06"
assert s.reformatDate("26th May 1960") == "1960-05-26"