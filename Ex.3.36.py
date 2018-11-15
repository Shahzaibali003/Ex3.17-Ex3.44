#Exercise 3.36
#Implement function reverse_int() that takes a three-digit integer as input and returns
#the integer obtained by reversing its digits. For example, if the input is 123, your
#function should return 321. You are not allowed to use the string data type operations to
#do this task. Your program should simply read the input as an integer and process it as an
#integer using operators such as // and %. You may assume that the input integer does not
#end with the 0 digit
def reverse_int():
    Number = int(input("Please Enter any Number: "))
    Reverse = 0
    while(Number > 0):
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Number = Number //10
        print(Reverse)
    print("\n Reverse of entered number is = %d" %Reverse)

reverse_int()
