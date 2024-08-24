#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def passedBy(self, a, b):
        # Code here
        self.a = a
        self.b = b
        return self.a+1,self.b+2

#{
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input ("Array Size: "))
    for _ in range (t):
        a, b = list(map(int, input("Enter Array values separated by SPACE: ").split()))
        ob = Solution()
        res = ob.passedBy(a, b)
        print(res[0], res[1])
# } Driver Code Ends