set=[]
wet=[]
n=int(input("enter no of employes: "))
cun=int(input("enter no of employes present:"))
count=0
while count<cun:
    ui=int(input("enter:"))
    count=count+1
    wet.append(ui)
for i in range(1,n):
    set.append(i)
for i in wet:
    set.remove(i)
print("not present employes :")
for i in set:
    print(i,"is not present")
print("present lists are")
for i in wet:
    print(i,"is present")










