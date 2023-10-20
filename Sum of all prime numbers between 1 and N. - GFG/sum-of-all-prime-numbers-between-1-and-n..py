#User function Template for python3

class Solution:
    def prime_Sum(self, n):
        # Create a boolean list to mark numbers as prime or not
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        # Sieve of Eratosthenes to mark non-prime numbers
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1

        # Calculate the sum of prime numbers
        prime_sum = sum(i for i in range(2, n + 1) if is_prime[i])
        return prime_sum

    
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		ob = Solution()
		ans = ob.prime_Sum(n)
		print(ans)
# } Driver Code Ends