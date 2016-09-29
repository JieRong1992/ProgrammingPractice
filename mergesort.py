# compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
import sys
sys.setrecursionlimit(1000)
count=0
L=[]
newfile=open('/Users/RongJie/Desktop/question.txt','r')
for line in newfile:
    if line.strip():  # line contains eol character(s)
        n = int(line)
    L.append(n)


class NewClass():

    def __init__(self):
        self.count=0

    def merge_sort(self,List):
        mid = int(len(List) / 2)
        if len(List) <= 1: return List
        return self.merge(self.merge_sort(List[:mid]), self.merge_sort(List[mid:]))

    def merge(self,l1, l2):
        final = []
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                final.append(l1[i])
                i += 1
                if i == len(l1):
                    final += l2[j:]
            else:
                final.append(l2[j])
                self.count+=len(l1)-i
                j += 1
                if j == len(l2):
                    final += l1[i:]
        print(self.count)
        return final
