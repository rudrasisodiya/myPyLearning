class Solution:
    def evenlyDivides(self, N):
        count = 0
        orgnl_N = N
        while N > 0:
            last_digit = N % 10
            N = N // 10
            if last_digit != 0 and orgnl_N % last_digit == 0:
                count += 1
        return count

if __name__ == '__main__':
    t = int(input("Enter Your Number Here: "))
    ob = Solution()
    print(ob.evenlyDivides(t))