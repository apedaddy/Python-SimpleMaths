print ('Program to create multiplication table of given number: ')
print ('________________________________________________________')

no = int(input("Enter your number: "))
tot = int(input("Enter upto which number you want to calculate: "))

for c in range (1,tot+1):
    print (no, 'X', c," = ", no*c)
#End of the program