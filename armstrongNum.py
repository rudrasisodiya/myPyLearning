class ArmstrongNumCheck():

    def num_check(self,num):
        nm_str = str(num)
        size = len(nm_str)
        val = 0
        val_final = 0
        for i in range(size):
            val = int(nm_str[i])**size
            val_final +=  val
        if val_final == num:
            return True
        else:
            return False

obj = ArmstrongNumCheck()
num =int(input("Enter Your Number Here: "))

if obj.num_check(num) == True:
    print(f"{num}, is an Armstrong Number")
else:
    print(f"{num}, is not an Armstrong Number")