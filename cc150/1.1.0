# O(n)
def Result(s):
    n=isunique(s)
    if n is True:
        print('is unique')
    else:
        print('not unique')

def isunique(s):
    d={}
    if len(s) > 128:
        return False
    for letter in s:
        if d.get(letter) == None:
            d[letter] = True
        else:
           return False

    return True

p = input('input a string')
Result(p)
