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

#O(n)


num = 10

def addOnesToTestList(num):
    testList = []
    for i in range(0, num):
        testList.append(1)
        print(testList)
    return testList

print "(O(n): )"
addOnesToTestList
print


#O(n loh n)

testList = [1, 43, 31, 21, 6, 96, 48, 13, 25, 5]

def mergeSort(testList):
    if len(testList) < 2:
        return testList
    middle = len(testList) / 2:
    left(mergeSort(testList[:middle]))