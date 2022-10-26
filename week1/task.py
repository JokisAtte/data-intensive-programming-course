import functools
import math

# Task 1
def mySum(x, y):
    return x + y

# Task 2
def pascal(row, column):
    if column == 0:
        return 1
    if row == 0:
        return column
    return (row * pascal(row-1, column-1)) / column

# Task 3
def balance(chars:list, i=0, cnt=0):
    if i == len(chars): return cnt == 0
    if cnt < 0: return False
    if chars[i] == "(": return  balance(chars, i + 1, cnt + 1)
    elif chars[i] == ")": return  balance(chars, i + 1, cnt - 1)
    return balance(chars, i + 1, cnt)

# Task 4
def higherOrdr(nums:list):
    reduceResult = functools.reduce(lambda a, b: math.sqrt(a)+math.sqrt(b), nums)
    return reduceResult

# Task 5
def task5():
    #Snippet 1
    from itertools import groupby  # itertools.groupby requires the list to be sorted
    result = {r: len(s) for r, s in {p: list(v) for p, v in groupby(sorted(list(map(lambda x: (x, 1), "sheena is a punk rocker she is a punk punk".split(" "))), key=lambda x: x[0]), lambda x: x[0])}.items()}
    print(result)
    print(sorted(list(map(lambda x: (x, 1), "sheena is a punk rocker she is a punk punk".split(" "))), key=lambda x: x[0]))
    #Explanation:
    # The end result is that every word is counted. Result is a map, where each word in the sentence is a key, and its value its the times it is in the sentence.
    # But how do we get here:
    # The snippet starts by calling split() on the string, which returns a list of the words in the string, using " " as the delimiter string
    # Then, this is mapped


    #Snippet 2
    result_2 = {r: functools.reduce(lambda x, y: x + y, list(map(lambda x: x[1], s))) for r, s in {p: list(v) for p, v in groupby(sorted(list(map(lambda x: (x, 1), "sheena is a punk rocker she is a punk punk".split(" "))), key=lambda x: x[0]), lambda x: x[0])}.items()}

    #Explanation

def main():
    print(pascal(4,1))
    print(higherOrdr([1,2,3,4]))
    task5()

main()