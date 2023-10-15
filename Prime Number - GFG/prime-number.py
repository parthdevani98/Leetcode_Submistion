#User function Template for python3
import math
class Solution:
    def isPrime (self, N):
        # code here
        if N <= 1:
            return 0  # 0 and 1 are not prime numbers

        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                return 0  # N is divisible by a number other than 1 and itself

        return 1  # N is prime


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends