#mylist = [2,3,4,5,8,12,73]
totno = int(input('Please enter how many nos you want in the list: '))
totlist = []
for askno in range (totno):
    nums = int(input('Enter your numbers '))
    totlist.append(nums)

oddlist =[]
evenlist=[]

for no in totlist:
    if no%2 ==0:
        evenlist.append(no)
    else:
        oddlist.append(no)
maxeven = max(evenlist)
maxodd = max(oddlist)

print (maxeven)
print(maxodd)
