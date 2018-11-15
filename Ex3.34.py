#Exercise 3.34
#that takes as input two arguments: an hourly wage and the
#number of hours an employee worked in the last week.compute and
#return the employee’s pay. Any hours worked beyond 40 is overtime and should be paid at
#1.5 times the regular hourly wage.
sum = 0
def pay(x,y):
    if y < 40:
        sum = x*y
    else:
        sum = x*40
        sum += (x*1.5)*(y-40)
       
    return sum
pay(10,35)
pay(10,45)
