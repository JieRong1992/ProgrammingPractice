#把两个string分别存入两个dict,比较两个dict看是否相等
#没有考虑空格和大小写
#速度较慢,因为需要把两个都存入dict之后才能比
def coun(s):
    d={}
    for letter in s:
        if d.get(letter)==None:
            d[letter]=1
        else:
            d[letter]+=1
    return d
def jug(d1,d2):
    a = coun(d1)
    b = coun(d2)
    if d1==d2:
        return('no')
    if a==b:
        print('yes')
    else:
        print('no')
d1=input('enter a string')
d2=input('enter another string')
jug(d1,d2)
