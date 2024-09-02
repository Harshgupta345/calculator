contacts={}
def add_cont() : 
    name=input("enter your contact name:")
    phone=int(input("enter number:"))
    contacts[name]=phone
    print(f"your cont,{name} is added")
def view_cont():
    print("contacts:")
    for name ,phone  in contacts.items():
        print(f"Name: {name} contact:{phone}")
def remove_cont():
    view_cont()
    dele=input("enter the contact:")
    if dele in contacts:
        del contacts[dele]
    print(f"cont'{dele}' is deleted")
while True :
    print("1 to add cont\n2 to views cont\n3 to delete cont\n4 to exit")
    you=int(input("enter:"))
    if you==1:
        add_cont()
    if you==2:
        view_cont()
    if you==3:
        remove_cont()

    if you==4:
        print("exit")
        break
print("happy")


    
