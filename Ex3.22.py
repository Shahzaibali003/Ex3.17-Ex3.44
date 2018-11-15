#Exercise 3.22
#this program will square the 1st element and that element which is divisible by 8
lst=[2, 3, 4, 5, 6, 7, 8, 9]
for i in lst:
    if(i**2%8==0):
        print(i)
