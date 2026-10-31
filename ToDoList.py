
tasks=[]
def showMenu():
    print("\n ---TO-DO LIST---")
    print("1. Add the task")
    print("2. View the task")
    print("3. Mark the task as done")
    print("4. Remove the task ")
    print("5. exit")
def addTask():
    task=input("enter the task:- ")
    tasks.append({"task":task,"done":False})
    print(f"task '{task}' added!")
def viewTask():
    if not  tasks:
        print("no tasks yet!")
        return
    print("\n your tasks:")
    for index,task in enumerate(tasks,start=1):
        status="✅" if task["done"] else "❌"
        print(f"{index}.{task['task']}[{status}]")
def markTask():
    viewTask()
    if not tasks:
        return
    try:
        index=int(input("enter the task number mark to be done:-"))-1
        if 0<=index<len(tasks):
            tasks[index]["done"]=True
            print("Mark as done!")
        else:
            print("invalid number!")
    except ValueError:
        print("please enter the valid number!")
def deleteTask():
    if not tasks:
            return
    try:
      index=int(input("enter the task number to remove:-"))-1
      if 0<=index<len(tasks):
       removed=tasks.pop(index)
       print(f"deleted task:{removed['task']}")
      else:
          print("INVALID NUMBER!")
    except ValueError:
        print("please enter valid number! ")

                 



while True:
    showMenu()
    choice=input("enter the number (1-5): ")
    if choice=='1':
        addTask()
    elif choice=='2':
        viewTask()
    elif choice=='3':
       markTask()  
    elif choice=='4':
      deleteTask()  
    elif choice=='5':
      print("GOOD BYE!")
      break
    else:
        print("invalid choice .try again!")     
