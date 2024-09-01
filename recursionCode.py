
class Solution:
    def printNos(self, N):
        if (N <= 0):
            return
        self.printNos(N - 1)
        print(N, end=' ')

def main():
    T = int(input("Enter Number: "))

    while (T > 0):
        N = int(input("Enter Number: "))

        ob = Solution()

        ob.printNos(N)
        print()
        T -= 1
if __name__ == "__main__":
    main()