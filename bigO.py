#big o notation
#O(1)
#Time complextity workds with python from MITx
# code under GNU/GPL
# C - 2019 - f.alfonso@res-ear.ch 
# 

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
    middle = len(testList) / 2
    left = mergeSort(testList[:middle])
    right = mergeSort(testList[middle:])
    result = []
    print "Left:: ", left
    print "Right: ", right
    while len(left) > 0 and len(right) > 0:
       if left[0] <= right[0]:
          result.append(left[0])
          left.pop(0)
    else:
            result.append(right[0])
            right.pop(0)
    result += left
    result += right
    print "Result:", result
    return result

print "O(n log n):"
mergeSort(testList)
print


#O(n**2)
testList = [1,43,31,21,6,96,48,13,25,5]


def bubbleSort(testList):
    for i in range(len(testList)):
        for j in range(i+1, len(testList)):
            if testList[j] < testList[i]:
                testList[j], testList[i] = testList[i], testList[j]
            print testList
print "O(n**2):"
bubbleSort(testList)
print

#

