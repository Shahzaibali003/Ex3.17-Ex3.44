#Exercise 3.29
n=eval(input("enter a positive integer n : "))
for i in range(1,n+1):
    if(n%i==0):
        print(i)
