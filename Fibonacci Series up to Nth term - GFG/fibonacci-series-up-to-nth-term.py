#User function Template for python3

class Solution:
    def series(self, n):
        # Code here
        def fibonacci_recursive(n, a=0, b=1):
            if n >= 0:
                return [a] + fibonacci_recursive(n - 1, b, a + b)
            else:
                return []

        return fibonacci_recursive(n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends