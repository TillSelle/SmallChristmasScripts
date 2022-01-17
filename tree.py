# https://github.com/matrix1001/ezcolor
from ezcolor import Color
# -------------------------------------
import random
import math

if __name__ == '__main__':
    color = Color()
    xMasChar = "*"
    numStars = 1
    currStr = ""
    odd = []
    # iterating each number in list
    for num in range(8, 36 + 1):
        if num % 2 != 0:
            odd.append(num)
    height = random.choice(odd)
    maxStars = height*2
    whitespace = ""

    for n in range(0,maxStars+1):
        whitespace += " "
    stempWidth = int(maxStars / 4)
    stempStr = ""
    stempWS = whitespace
    for x in range(0,stempWidth+1):
        if (x % 2):
            stempWS = stempWS[0 : -1 : ]
        if (x == 0):
            stempStr += "["
        elif (x == stempWidth):
            stempStr += "]"
        else:
            stempStr += "|"
    for x in range(1, height + 1):
        currStr += whitespace
        for i in range(0, numStars):
            choice = random.choice(range(0,44))
            if (choice <= 24):
                currStr += color.green(xMasChar)
            if (choice >= 25 and choice <= 30):
                currStr += color.yellow(xMasChar)
            if (choice >= 31 and choice <= 37):
                currStr += color.blue(xMasChar)
            if (choice >= 38 and choice <= 44):
                currStr += color.red(xMasChar)
        print(currStr)
        currStr = ""
        numStars += 2
        whitespace = whitespace[0 : -1 : ]
    for x in range(0, int(height / 5)):
        print(stempWS + stempStr)
