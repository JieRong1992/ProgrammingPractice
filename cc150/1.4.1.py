#重点在计数,奇数的计数必须小于等于1
#对于偶数个字符,计数要为0,对于奇数个字符,计数要==1
#在最后计算奇数个数
def pp(s):
    d={}
    count=0
    for letter in s:
        if letter==' ':
            continue
        if d.get(letter)==None:
            d[letter]=1
        else:
            d[letter]+=1
    for i in d:
        if d[i]%2==1:
           count+=1
    if count<=1:
            return True
    else:
            return False
#test
c=pp('acca')
print(c)
