#1这个地方第一次错了(第一次写的是for i in range(length - 1)),
# 不是每次都从0开始到length结束,因为circle向里时这个i变小
L=[[0 for x in range(4)] for y in range(4)]
for list in L:
    x=1
    for i in range(len(list)):
        list[i]=x
        x+=1
#for list in L:
    #print(list)
# top=L[0][]
# right=L[][length-1]
# bottom=L[length-1][]
# left=L[][0]
def rotat(L):
    length=len(L)
    tem=[0][0]
    circle=int(length/2)
    for j in range(circle):
        for i in range(j,length - 1-j):    #1
            # top-->tem
            tem = L[j][i]
            # left-->top
            L[j][i] = L[-i - 1][j]
            # botton-->left
            L[-i - 1][j] = L[length - 1 - j][-i - 1]
            # right-->bottom
            L[length - 1 - j][-i - 1] = L[i][length - 1 - j]
            # tem-->right
            L[i][length - 1 - j] = tem
    return L
newlist=rotat(L)
for line in newlist:
    print(line)

