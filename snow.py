# https://github.com/matrix1001/ezcolor
from ezcolor import Color
# -------------------------------------
import random

if __name__ == '__main__':
    color = Color()
    xMasChar = "*"
    numStars = 1
    currStr = ""
    odd = []
    for num in range(8, 36 + 1):
        if num % 2 != 0:
            odd.append(num)
    height = random.choice(odd)
    maxStars = height*2
    whitespace = ""
    for n in range(0,maxStars+1):
        whitespace += " "
    for x in range(1, height + 1):
        for i in range(0, numStars):
            currStr += whitespace + color.blue(xMasChar)
        print(currStr)
        currStr = ""
        numStars += 2
        whitespace = whitespace[0 : -1 : ]
