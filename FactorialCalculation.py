#Takinginput
num=int(input("Enter a number:"))

#Initialize Factorial
factorial=1

#Calculate Fcatorial using loop
for i in range(1,num+1):
    factorial*=i

#Print the Factorial
print("The Factorial of",num,"is",factorial)