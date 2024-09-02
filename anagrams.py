list=[]
ist=[]
inpu=str(input("enter 1:"))
inp=inpu[0:len(inpu)]
for i in inp:
    list.append(i)
    list.sort()
put=str(input("enter 2:"))
inmp=put[0:len(put)]
for i in inmp:
    ist.append(i)
    ist.sort()
pr=list==ist
if(pr== True):
    print(inpu,"and",put,"are anagrams")
else:
    print(inpu,"and",put,"are not anagrams")
#inp=str(input("enter 2:"))
