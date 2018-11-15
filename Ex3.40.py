#Exercise 3.40
#Implement function partition() that splits a list of soccer players into two groups.
#More precisely, it takes a list of first names (strings) as input and prints the names of those
#soccer players whose first name starts with a letter between and including A and M.
def partition(lst):
    for x in lst:
        x.casefold()
        if x[1] in "abcdefghijklm":
            print(x)
partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin'])
