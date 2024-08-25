def reverse(x):
    reversed_num = 0
    while x > 0:
        digi = x % 10
        reversed_num = reversed_num * 10 + digi
        x = x // 10
    return reversed_num

print(reverse(120))
