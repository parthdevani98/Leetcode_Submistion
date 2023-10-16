#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        count = 0
        N_str = str(N)
    
        for digit_str in N_str:
            digit = int(digit_str)
            if digit != 0 and N % digit == 0:
                 count += 1
    
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends