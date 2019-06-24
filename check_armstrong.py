num = int(input('Enter your number: '))
'''
temp = num
newnum = 0
while num>0:
    rm = num%10
    newnum = newnum + rm**3
    num = num//10

if temp == newnum:
    print ("Armstrong")
else:
    print ("Not Armstrong")
'''
a = list(map(int,str(num)))
b = list(map(lambda x:x**3,a))
if num == (sum(b)):
    print ('Armstrong')
else:
    print ('Not Armstrong')