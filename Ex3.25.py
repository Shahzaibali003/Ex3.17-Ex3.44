#Exercise 3.25
wordList=eval(input("input the list of name:"))
for i in wordList:
    if i[1] in "abcdefghijklm":
        print(i)
