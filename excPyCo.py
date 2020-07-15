
# code under GNU/GPL & MIT
# Engineered @ 2019 - Felipe González: f.alfonso@res-ear.ch 
# 

# x = int(input('Enter an integer: '))

#
# x = 3
# ans = 0
# itersLeft = x
# while (itersLeft != 0):
#     ans = ans + x
#     itersLeft = itersLeft - 1
# print(str(x) + '*' + str(x) + ' = ' + str(ans))
#

#guess and check 

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))
    
