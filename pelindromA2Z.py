class Check:
    def __init__(self,s):
        self.s = s

    def palindrome(self):
        size = len(self.s)
        reverse_str = ""
        for i in range(size):
            reverse_str += self.s[size-i-1]
            i += 1
        if reverse_str == self.s:
             print(f"Entered String {self.s} is a Palindrome")
        else:
             print(f"Entered String {self.s} is not a Palindrome")

s = input("Check Palindrome String: ")
obj = Check(s)
obj.palindrome()

