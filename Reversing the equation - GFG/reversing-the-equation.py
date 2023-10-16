#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        
        i=len(s)-1
        ans=""
        while(i>=0):
            
            num=int(s[i])
                
            j=i-1
            pw=1
            while(j>=0 and s[j]>='0' and s[j]<='9'):
                num=num+int(s[j])*(10**pw)
                pw+=1
                j-=1
        
        
            ans=ans+str(num)
            
            while(j>=0 and (s[j]<'0' or s[j]>'9')):
                ans+=s[j]
                j-=1
                
            i=j

        return ans
   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends