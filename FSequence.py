#This is a Fibinacci Sequence program without complex data structures

print("hello Person")


#Getting user data
howLong = int(input("How long do you want the sequence to be? Starts after 1\n"))


#Presetting variables 
newNumber = 1
currentNumber = 1
beforeNumber = 0


#The start
print("0")
print(newNumber)


#The actual sequence
for i in range(howLong):
    print(newNumber)
    beforeNumber = currentNumber
    currentNumber = newNumber
    newNumber = currentNumber + beforeNumber

