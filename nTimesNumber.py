class NtimeNum:
    def nuNTime(self,num):
        if(num <= 0):
            return
        self.nuNTime(num - 1)
        print(num, end=" ")

num = int(input("Enter Your Number: "))
obj = NtimeNum()
obj.nuNTime(num)