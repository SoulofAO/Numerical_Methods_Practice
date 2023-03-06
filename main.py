from sympy import *

t = [[-1,2],[0,1],[1,2],[2,17],[3,82]]
def GetTree(t):
    l = 1
    answer = []
    firstarray = []
    for x in t:
        firstarray.append(float(x[1]))
    answer.append(firstarray)

    while l<len(t):
        newArray = []
        count = 0
        while count + l < len(t):
            result = (answer[l-1][count+1]-answer[l-1][count])/(t[count+l][0]-t[count][0])
            newArray.append(result)
            count = count+1
        l=l+1
        answer.append(newArray)
    return answer





answertree = GetTree(t)
print(answertree)

x = Symbol('x')
h=""
for i in range(len(t)):
    h = h + "+"
    h = h + str(answertree[i][0])
    num = 0
    while num < i:
       h=h+"*"+"(x-"+str(t[num][0])+")"
       num=num+1
print(h)
expr = sympify(h)
expr = Eq(expr,0)
expr = expand(expr)
print(expr)
print(solveset(expr,x))
