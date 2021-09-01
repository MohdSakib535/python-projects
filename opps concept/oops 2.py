#eg
# class Mobile:
#     fp="yes"
#     def __init__(self,m):
#         self.model=m
#     def show_model(self,p=15000):
#         self.price=p
#         print("model:",self.model,"and price:",self.price)
#
#     @classmethod
#     def is_fp(cls):
#        print("fingerprint:",cls.fp)
#
# p1=Mobile("realmi")
# p2=Mobile("readmi")
# p3=Mobile("vivo")
#
# p1.show_model()
# p2.show_model(12000)
# p3.show_model(22000)
#
# p1.is_fp()

# Mobile.fp="no"
# print("realmi:",Mobile.fp)
# print("redmi:",Mobile.fp)
# print("vivo:",Mobile.fp)


#eg
class Mobile:
    fp="yes"
    def __init__(self,m):
        self.model=m
    def show_model(self,p=15000):
        self.price=p
        print("model:",self.model,"and price:",self.price)

    @classmethod
    def is_fp(cls):
       print("fingerprint:")

realmi=Mobile("realmi")
redmi=Mobile("readmi")
vivo=Mobile("vivo")

realmi.show_model()
redmi.show_model(12000)
vivo.show_model(22000)

Mobile.is_fp()
print("realmi:",realmi.fp)
print("redmi:",redmi.fp)
print("vivo:",vivo.fp)
print()

Mobile.fp="no"
print("realmi:",realmi.fp)
print("redmi:",redmi.fp)
print("vivo:",vivo.fp)
print()

realmi.fp='damage'
print("realmi:",realmi.fp)
print("redmi:",redmi.fp)
print("vivo:",vivo.fp)
print()

vivo.fp='technical falt'
print("realmi:",realmi.fp)
print("redmi:",redmi.fp)
print("vivo:",vivo.fp)

# eg
# class student:
#     def __init__(self,n,r):
#         self.name=n
#         self.roll=r
#
#     def disp(self):
#         print("students name:",self.name," and student roll",self.roll)
#
# class User:
#     @staticmethod
#     def show(s):
#         print("user name:",s.name,"user roll:",s.roll)
#         s.disp()
#
# stu=student('sakib',535)
# User.show(stu)

#eg
# class Mobile:
#     @staticmethod
#     def show():
#         print("realmi")
#
# a=Mobile()
# Mobile.show()


#eg
# class Army:
#     def __init__(self):
#         self.name='sakib'
#         self.gn= self.Gun()
#
#     def disp(self):
#         print("name:",self.name)
#
#     class Gun:
#         def __init__(self):
#          self.name='Ak47'
#          self.type='auto'
#          self.capacity='78 round'
#
#         def show(self):
#          print("gun name:",self.name)
#          print("gun type:",self.type)
#          print("gun capicity:",self.capacity)
#
# a=Army()
# print(a.name)
# a.disp()
# print()
# print(a.gn.name)
# g=a.gn
# print(g.type)
# g.show()


#eg
# class Outer:
#     """Outer Class"""
#     def __init__(self):
#         self.first_inner = self.Inner()
#         self.second_inner = self.Innerinner()
#     def show_classes(self):
#         print("This is Outer class")
#     class Inner:
#         """First Inner Class"""
#         def inner_display(self, msg):
#             print("This is Inner class")
#             print(msg)
#     class Innerinner:
#         """Second Inner Class"""
#         def innerinner_display(self, msg):
#             print("This is Innerinner class")
#             print(msg)
# a=Outer()
# a.show_classes()
# print()
# g=a.first_inner
# g.inner_display("hello")
# print()
# z=a.second_inner
# z.innerinner_display("world")


#eg
# class person:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#
#     def display(self):
#         print("ur name is :",self.name)
#         print("ur id id :",self.id)
#
# a=person("sakib",23)
# a.display()

#eg
# from datetime import date
# random Person
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromBirthYear(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)
#     def display(self):
#         print(self.name + "'s age is: " + str(self.age))
#
# person = Person('Adam', 19)
# person.display()
#
# person1 = Person.fromBirthYear('John',  2000)
# person1.display()

#eg
# class Person:
#     age = 25
#
#     def printAge(cls):
#         print('The age is:', cls.age)


#eg
# class student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
#     def show(self):
#         print("student name:",self.name)
#         print("student roll no:",self.roll)
#         # print("your name is :",self.name,"and roll no:",self.roll)
#
# class user:
#     @staticmethod
#     def disp(self):
#         print("user name:",self.name,"roll no:",self.roll)
#         self.show()
# a=student("sakib",535)
# user.disp(a)