# class car():
#     def __init__(self,type):
#        self.type=type

#     @staticmethod
#     def start():
#        print("car start..")
#     @staticmethod
#     def stop():
#         print("car stop..")


# class toyota(car):
#     def __init__(self,name,type):
#         self.name=name
#         #super().__init__(type)
# car1=toyota("perius","electric")
# print(car1.type)
# class person:
#     name="vivek"

#     # def change_name(self,name):
#     #     self.__class__.name="rahul"
#     @classmethod
#     def change_name(cls,name):
#         cls.name="rahul"
# p1=person()
# print(p1.name)
# p1.change_name("ayush")
# print(p1.name)
# print(person.name)
# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def showcpm(self):
#         print(self.real,"+",self.img,"i")
#     def __add__(self, num2):
#         newReal=self.real+num2.real
#         newImg=self.img+num2.img
#         return complex(newReal,newImg)
# num1=complex(1,4)
# num1.showcpm()
# num2=complex(3,4)
# num2.showcpm()
# num3=num1.__add__(num2)
# # num3=num1+num2
# num3.showcpm()
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*(self.radius**2) 
#     def perimeter(self):
#         return 2*3.14*(self.radius)
# c1=circle(21)
# print("radius of circle is",c1.radius)
# print("area of circle is",c1.area())
# print("perimeter of circle is",c1.perimeter())
# class empolyee:
#     def __init__(self,role,department,salaries):
#         self.role=role
#         self.department=department
#         self.salaries=salaries
#     def showDetail(self):
#         print("role of employee is",self.role)
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
