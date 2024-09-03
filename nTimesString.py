#Take a number and string from user, print user's string number of time

class PrintTimeFun:
    def __init__(self,s):
        self.s = s
    def showString(self,num):
        if (num <= 0):
            return
        self.showString( num - 1)
        print(self.s, end=' ')


num = int(input("How many time you would like to print string: "))
s = input("Enter your string here: ")
obj = PrintTimeFun(s)
obj.showString(num)