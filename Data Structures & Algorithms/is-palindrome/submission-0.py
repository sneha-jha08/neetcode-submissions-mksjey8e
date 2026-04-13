class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphnumstr=(''.join(filter(str.isalnum, s))).lower()
        # print(alphnumstr[::-1])
        return alphnumstr==alphnumstr[::-1]