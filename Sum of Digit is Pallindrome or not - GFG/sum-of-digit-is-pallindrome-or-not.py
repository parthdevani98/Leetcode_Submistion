#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self,N):
        #code here
        digit_sum = 0
        while N > 0:
            digit_sum = digit_sum + N % 10
            N //=10
        
        if digit_sum == int(str(digit_sum)[::-1]):
            return 1
        return 0








#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends