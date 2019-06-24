num = int(input("Enter your number: "))
# Initial sum of digits set to 0
sum = 0
while (num>0):
    # Divide number by 10 - remainder will be last digit to come out
    digi = (num%10)
    sum = sum + digi
    num = num//10
print (f"The sum of all digits in the number is: {sum}")