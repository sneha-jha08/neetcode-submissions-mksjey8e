class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        res=[]
        digits=digits[::-1]
        for i in range(len(digits)):
            num+=pow(10,i)*digits[i]
        num+=1
        while num!=0:
            rem=num%10
            res.append(rem)
            num=num//10
        return res[::-1]