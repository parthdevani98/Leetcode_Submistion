#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def print_divisors(self, N):
        divisors = []  # List to store divisors
        for i in range(1, int(N**0.5) + 1):
            if N % i == 0:
                divisors.append(i)
            # If i is not equal to N / i, add N / i as well (to avoid duplicates)
                if i != N // i:
                    divisors.append(N // i)
    
        divisors.sort()  # Sort the list of divisors in ascending order
        print(*divisors, end=' ')

    

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        ob.print_divisors(N)
        print()
# } Driver Code Ends