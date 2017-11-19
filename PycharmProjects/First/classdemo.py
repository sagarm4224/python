class demo:
    "this is a demo class"
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name
    def displayemp(self):
        print("Name of the student is ", self.name , ", Roll no of the student is ", self.rollno)

emp = demo(121,"sagar")
emp1 = demo(131,"megha")

print(demo.__doc__)
emp.displayemp()
emp1.displayemp()