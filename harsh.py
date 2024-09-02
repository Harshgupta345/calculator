books=[]
def add_tasks():
    task = input("enter task to added:")
    books.append(task)
    print(f"tasks'{task}'added")
def view_tasks():
    i=0
    for i in books:
        print(i) 
    if not books:
        print("no tasks")
def delete_tasks():
    view_tasks()
    dele=int(input("enter the task number to delete:"))
    rem=books.pop(dele-1)
    print(f"tasks'{rem}' is deleted")
while True:
    print("1 to add tasks\n2 to views task\n3 to delete task\n4 to exit")
    you=int(input("enter:"))
    if you==1:
        add_tasks()
    if you==2:
        view_tasks()
    if you==3:
        delete_tasks()
    if you==4:
        print("exit")
        break

