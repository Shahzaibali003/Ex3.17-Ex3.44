#Exercise 3.42
#Implement function avg() that takes as input a list that contains lists of numbers. Each
#number list represents the grades a particular student received for a course. For example,
#here is an input list for a class of four students:
def avg(multiList):
    sum=0
    for x in multiList:
        tmpLst=x
        for i in tmpLst:
            sum+=i        
        print(sum/len(tmpLst))
        sum =0

multiList=[[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]]
avg(multiList)

