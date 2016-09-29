#一段字符两个指针
#重点是注意两个指针到最后一个的情况要特别讨论
#把字母和数字合并后存入L,最后把L合并成string
#把字符链接comb变成append,提高效率
def stringcomp(s):
    i = 0
    L = []
    N = len(s)
    while i < N:
        coun = 1 #每次一轮新的字母记数,要把他初始化
        if i == N - 1: #如果上排指针到最后一个,说明最后的这个字母只出现一次,所以不需要j,直接返回次数1
            comb = s[i] + str(coun)
            L.append(comb)
            break
        else:
            for j in range(i + 1, N):
                if s[i] != s[j]: #如果上排和下排不相等,就开始新一轮计数
                    comb = s[i] + str(coun) #新计数前要把之前的存起来
                    L.append(comb)
                    i = j  #i直接到J的位置上,因为从j位置开始出现的的字母
                    break
                else:
                    if j == N - 1: #如果i和j相同,且j到了最后一位,也说明这个字符串已经计算完了
                        coun += 1
                        com = s[i] + str(coun)
                        L.append(com)
                        i = N #跳出两层循环,因为已经结束
                    else: #两个相等且没到最后一位的话要计数,然后让j往后移
                        coun += 1
    newstr = ''.join(L)
    if len(newstr)>N:
        return s
    else:
        return newstr
#test case
print(stringcomp('casccccccccf'))
