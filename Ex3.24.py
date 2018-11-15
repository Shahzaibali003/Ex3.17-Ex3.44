#Exercise 3.24
#This program will not print the given worfd which is with != sign
wordList=eval(input("input the list of word : "))
for i in wordList:
    if i != "secret":
        print(i)
