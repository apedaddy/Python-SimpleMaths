nums = int(input("Enter how many numbers you want to calculate: "))
user_numbers =[]
for c1 in range (nums):
    no = int(input("Enter numbers: "))
    user_numbers.append(no)
sum1 = 0
sum2 = 0
sum3 = 0
for nos in user_numbers:


    if nos >1:
        if nos%2 ==0:
            sum1 += nos
        else:
            sum2 +=nos
    else:
        sum3 +=nos

print ("sum of even nos: ", sum1)
print ("sum of odd nos: ", sum2)
print ("sum of negative nos: ", sum3)