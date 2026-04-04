#Take input from the user
n=int(input("Enter the number of terms:"))

#First two terms
a,b=0,1

#Print Fibonacci series
print("Fibonacci Series")
for i in range(n):
    print(a,end="_")
    a,b=b,a+b