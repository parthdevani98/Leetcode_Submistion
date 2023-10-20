class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        m,c=min(a,b),1
        for i in range(2,m+1):
            if a%i==0 and b%i==0: c+=1
        return c
        