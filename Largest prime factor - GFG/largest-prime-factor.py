#User function Template for python3
import math
class Solution:
    def largestPrimeFactor (self, N):
        # code here
        largest_prime = -1  # Initialize largest_prime to -1

    # Divide N by 2 until it's not divisible by 2
        while N % 2 == 0:
            N //= 2
            largest_prime = 2  # Update largest_prime when 2 is a factor

    # Iterate through odd numbers as potential prime factors
        for i in range(3, int(math.sqrt(N)) + 1, 2):
            while N % i == 0:
                N //= i
                largest_prime = i  # Update largest_prime with the current prime factor

    # If N is still greater than 1, it is a prime number
        if N > 1:
            largest_prime = N  # Update largest_prime when N is a prime

        return largest_prime




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends