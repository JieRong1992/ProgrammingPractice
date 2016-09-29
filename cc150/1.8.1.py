#建立布尔array!
import random
def matrix():
    L = [[0 for x in range(5)] for y in range(6)]
    for list in L:
        x = 1
        for i in range(len(list)):
            list[i] = random.randint(0, 5)
            x += 1
    for list in L:
        print(list)
    return L
def zero(L):
    rowlen=len(L) #length of row
    collen=len(L[0]) #length of column
    rowlist=[]
    collist=[]
    for onerow in range(rowlen):   #begin compare zero, row by row
        for onecol in range(collen):  # every element in each row
            if L[onerow][onecol]==0:
                rowlist.append(onerow)
                collist.append(onecol)

    for i in rowlist: # entire row to zero
        for j in range(collen):
            L[i][j]=0
    for j in collist: # entire col to zero
        for i in range(rowlen):
            L[i][j]=0
    print('new matrix')
    for list in L:
        print(list)
    return L
