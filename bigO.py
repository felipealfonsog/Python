#big o notation
#O(1)

num = 100

def deductOne(num):
    num -=1
    return num

print "O(1):", "Win", deductOne(num), "Win"

#logaritmic O O(log n)

num = 10

def divide(num):
    while num > 1:
        num /= 2
        print(num)
    return num

print "O(log n):"
divide(num)
print

