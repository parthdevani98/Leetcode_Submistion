#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Calculate GCD
        gcd_result = gcd(A, B)

        # Calculate LCM using the relationship: LCM(A, B) = (A * B) / GCD(A, B)
        lcm_result = (A * B) // gcd_result

        return [lcm_result, gcd_result]
        
        # gcd = 1
        # for i in range(1, min(A,B)+1):
        #     if A % i == 0 and B % i == 0:
        #         gcd = i
        
        # lcm = (A * B)//gcd
        # return [lcm, gcd]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends