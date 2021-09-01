                        ##   inheritance concept   ###

 #eg
# class parents():
#     def show(self):
#         print("parents instance method")
# class son(parents):
#     def disp(self):
#         print("son instance method ")
# a=son()
# a.disp()


#eg
# class father:
#     money=20000
#     def show(self):
#         print("father class:")
#     @classmethod
#     def disp(cls):
#         print("income of father is: ",cls.money)
#
#     @staticmethod
#     def stat():
#         a=10
#         print("sweety mummy give sweety :",a,"Rs")
#
# class son(father):
#         def son_show(self):
#             print("son class")
# s=son()
# s.son_show()
# s.disp()
# s.show()
# s.stat()
# print()
# f=father()
# f.disp()

#eg                        constructor in inheritance
# class father:
#     def __init__(self,m):
#         self.money=m
#         print("father class constructor")
#     def show(self):
#         print("father class instance method",self.money)
# class son(father):
#     def disp(self):
#         print("son class instances",self.money)
#
# a=son(1000)
# a.show()
# a.disp()
# print()
# b=father(200)
# b.show()

#eg                        constructor overridden
# class Father:
#     def __init__(self):
#         self.money=1000
#         print("father class constructor")
#
#     def show(self):
#         print("father class instances method",self.money)
#
# class son(Father):
#     def __init__(self):
#         self.money=2000
#         self.name="rahul"
#         print("son constructor class")
#     def disp(self):
#         print("money:",self.money,"name:",self.name)
#         print("son class instance method")
# f=Father()
# f.show()
# print()
# s=son()
# # print(s.money)
# s.disp()

#eg
# class Father:
#     def __init__(self,m):
#         self.money=m
#         print("father class constructor")
#
#     def show(self):
#         print("father class instance method")
# class son(Father):
#     def __init__(self,m,j):
#         self.job=j
#         super().__init__(m)
#         print("son class constructor")
#     def disp(self):
#         print("son class instance method")
#         print("money",self.money,"job:",self.job)
# s=son(1000,"python")
# s.disp()


#eg
# class Father:
#     def __init__(self,money,work):
#         self.money=money
#         self.work=work
#         print("Father class constructor")
#     def disp(self):
#         print("father work as:",self.work,"and salary is", self.money)
# class son(Father):
#     def __init__(self,money,work,pm):
#         self.pocket_money=pm
#         super().__init__(money,work)   ## call father class
#         print("son class constructor")
#     def show(self):
#         print("father earn:",self.money,"and son want :",self.pocket_money,"pocket money")
#
# s=son(1000,"pythoneer",200)
# s.show()
# f=Father(1000,"pythoneer")
# f.disp()


# class Laptop:
#     ability="unique"
#     def __init__(self,lap,color,ram):
#         self.comp=lap
#         self.color=color
#         self.ram=ram
#     def show(self):
#         print(self.comp,self.color,self.ram)
# class student(Laptop):
#     def __init__(self,name,age,lap,color,ram):
#         self.name=name
#         self.age=age
#         super().__init__(lap,color,ram)
#     def disp(self):
#         print(self.name,"has",self.comp,"laptop")
#         print("his age is ",self.age,"and want",self.ram,"ram")
#         print("he want",self.color,"color laptop.")
# a=student("sakib",22,"Dell","blue","4GB")
# a.disp()


#eg
# class students:
#     def get_students(self):
#         self.name=input("name")
#         self.age=input("age")
#         self.gender=input("gender")
#
# class test(students):
#     def get_marks(self):
#         self.studentclass=input("class")
#         print("enter the marks of respective subjects out of 100")
#         self.literature=int(input("literature"))
#         self.maths=int(input("maths"))
#         self.biology=int(input("biology"))
#         self.physics=int(input("physics"))
#
# class marks(test):
#     def disp(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("gender:",self.gender)
#         print("studyin:",self.studentclass)
#         print("total marks:",self.literature+self.maths+self.biology+self.physics)
#
# a=marks()
# a.get_students()
# a.get_marks()
# a.disp()

                    ## hierarchical inheritance
#eg
# class Details:
#     def __init__(self):
#         self.__id="<No Id>"
#         self.__name="<No Name>"
#         self.__gender="<No Gender>"
#     def setData(self,id,name,gender):
#         self.__id=id
#         self.__name=name
#         self.__gender=gender
#     def showData(self):
#         print("Id: ",self.__id)
#         print("Name: ", self.__name)
#         print("Gender: ", self.__gender)
#
# class Employee(Details): #Inheritance
#     def __init__(self):
#         self.__company="<No Company>"
#         self.__dept="<No Dept>"
#     def setEmployee(self,id,name,gender,comp,dept):
#         self.setData(id,name,gender)
#         self.__company=comp
#         self.__dept=dept
#     def showEmployee(self):
#         self.showData()
#         print("Company: ", self.__company)
#         print("Department: ", self.__dept)
#
# class Doctor(Details): #Inheritance
#     def __init__(self):
#         self.__hospital="<No Hospital>"
#         self.__dept="<No Dept>"
#     def setEmployee(self,id,name,gender,hos,dept):
#         self.setData(id,name,gender)
#         self.__hospital=hos
#         self.__dept=dept
#     def showEmployee(self):
#         self.showData()
#         print("Hospital: ", self.__hospital)
#         print("Department: ", self.__dept)
#
# def main():
#     print("Employee Object")
#     e=Employee()
#     e.setEmployee(1,"Prem Sharma","Male","gmr","excavation")
#     e.showEmployee()
#     print("\nDoctor Object")
#     d = Doctor()
#     d.setEmployee(1, "pankaj", "male", "aiims", "eyes")
#     d.showEmployee()
#
# if __name__=="__main__":
#     main()


#eg
# class Details:
#     def __init__(self,id,name,gender):
#         self.id=id
#         self.name=name
#         self.gender=gender
#     def disp(self):
#         print("id:",self.id)
#         print("name:",self.name)
#         print("gender:",self.gender)
#
# class Employees(Details):
#     def __init__(self,id,name,gender,company,department):
#         print("Employees object")
#         super().__init__(id,name,gender)
#         self.company=company
#         self.department=department
#
#     def dispE(self):
#         print("company:",self.company)
#         print("department:",self.department)
#
# class Doctor(Details):
#     def __init__(self,id,name,gender,hospital,department):
#         self.hospital=hospital
#         self.department=department
#         print("Doctor object")
#         super().__init__(id,name,gender)
#     def dispD(self):
#         print("hospital:",self.hospital)
#         print("department",self.department)
#
# a=Employees(1,"sakib","male","gmr","excavation")
# a.disp()
# a.dispE()
# print()
# b=Doctor(1,"reema","female","aiims","eye")
# b.disp()
# b.dispD()

                                 ## multiple inheritance ##
#eg
# class Father():
#     def __init__(self):
#         super().__init__()
#         print("father class constructor")
#     def dispF(self):
#         print("father class method")
# class Mother():
#     def __init__(self):
#         super().__init__()
#         print("mother class constructor")
#     def dispM(self):
#         print("Mother class method")
# class son(Mother,Father):
#     def __init__(self):
#         super().__init__()
#         print("son class constructor")
#     def dispS(self):
#         print("son class method")
# a=son()

#eg