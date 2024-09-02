cn=int(input("enter no of numbers:"))
list=[]
count=0
ist={}
sen=set()
while count<cn:
    ent=int(input("enter:"))
    count=count+1
    list.append(ent)


inp=int(input("enter your target:"))
for ent in list:
    comp=inp-ent
    if comp in list:
        ist[comp]=ent
        
print(set(ist))