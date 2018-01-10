#Adding multiple Numbers from the user 2.0

#Ends when 0
sum = 0
num = int(input("What is the number you want to add?\n"))
while num != 0:
    num = int(input("What is the number added? 0 stops the calculation\n"))
    sum += num
print("Your total number is ",sum)

