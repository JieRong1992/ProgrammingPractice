#奇数计数在中间
def pp(s):
    d={}
    count=0
    for letter in s:
        if letter==' ':
            continue
        if d.get(letter)==None:
            d[letter]=1
            count+=1
        else:
            d[letter]+=1
            if d[letter]%2==0:
                count-=1
            else:
                count+=1
                pring(count)
    if count<=1:
            return True
    else:
            return False
#test case
c=pp('adfadf')
print(c)
