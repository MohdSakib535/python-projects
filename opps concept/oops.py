#eg
# class person:
#     species='human'
#     def __init__(self,first_name,last_name,age):
#         self.person_first_name=first_name
#         self.last_name=last_name
#         self.age=age
# p1=person("sakib",'khan',22)
# p2=person("ram","sharma",23)
# print(p1.__class__.species)
# print(p1.person_first_name)
# print(p2.age)

#eg
# class Parrot:
#     # class attribute
#     species = "bird"
#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# instantiate the Parrot class
# p1 = Parrot("blu", 10)
# p2 = Parrot("Woo", 15)

##  access the class attribute
# print(f"blu is a {p1.__class__.species}")
# print(f"woo is a {p2.__class__.species}")

##access the instance attribute
# print(f"{p1.name} is {p1.age} year old")
# print(f"{p2.name} is {p2.age} year old")

#exersice
# class Laptop:
#     def  __init__(self,Brand_name,model_name,price):
#         #instance variable
#         self.Brand_name=Brand_name
#         self.model_name=model_name
#         self.price=price
#         self.laptop_name=Brand_name +model_name
# p1=Laptop('Dell',"vostro",50000)
# p2=Laptop('hp','node',45000)
# print(p1.Brand_name)
# print(p1.laptop_name)
# print(p2.price)


# class mobile:
#     def __init__(self,m):
#         self.model=m
#     def show_model(self):
#         print('model:',self.model)
#
# p1=mobile("realme")
# print(p1.model)

#eg
# class person():
#     def __init__(self):
#         self.name='sakib'
#         self.age=22
#     def show_name(self):
#         id=23
#         print("Name:",self.name,",",id)
# p1=person()
# print(p1.name)
# p1.show_name()
# p1.name="arif"
# print(p1.name)
# p1.show_name()

#eg
# class Mobile:
#     def __init__(self,m,v=50):
#         self.model=m
#         self.volume=v
#
#     def show_model(self,p):
#         price=p
#         print("model:",self.model,",","price:",price)
#         print('volume:',self.volume)
# realme=Mobile('realme x')
# realme.show_model(2000)
# print()
# readmi=Mobile("readmi z+",30)
# readmi.show_model(5000)


# class Mobile:
#     def __init__(self):
#         self.model='redmi'
#     def show_model(self):
#         print(self.model)
# redmi=Mobile()
# redmi.show_model()
#
# redmi.model="realme"
# print(redmi.model)

# class person:
#     species='human'
#     def __init__(self):
#         self.a='sakib'
# o=person()
# print(o.a)
# # print(o.__class__.species)
# print(o.species)


#eg
# class Mobile:
#     fp="yes"
#     def __init__(self):
#         self.model="realme"
#     def show_model(self):
#         print(self.model)
#
#     @classmethod
#     def is_fp(cls):
#         print( "inside:",cls.fp)
# p1=Mobile()
# Mobile.is_fp()

#eg
# class Mobile:
#     fp="yes"
#     def __init__(self):
#         self.model="realme"
#     def show_model(self):
#         print("model:",self.model)
#     @classmethod
#     def is_fp(cls):
#         print("finger print:",cls.fp)
# readmi=Mobile()
# readmi.show_model()
# Mobile.is_fp()

# class Students:
#     hobby="coding"
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#     @classmethod
#     def show(cls):
#         print(cls.hobby)
#
# a=Students.show()
# print(a)



#eg
class Students:
    gender="male"                             ## gender=class variable where male value stored
    def __init__(self,name,id,):
        self.name=name
        self.id=id

    @staticmethod
    def pt():
        print("this is student class")

    def disp1(self):
        print("name:",self.name,"and id:",self.id)

    @classmethod
    def showS(cls):
        print("gender:",cls.gender)

    @staticmethod
    def show1(address,locality):
        address=address
        locality=locality
        print("address:",address,"locality:",locality)
        print("this is student class")

class faculty(Students):
    hod="physics"
    def __init__(self,name,id):
        super().__init__(name,id)

        self.subject="maths"
    def disp2(self):
        print("name:",self.name,"id:",self.id,"subject",self.subject)

    @classmethod
    def shows(cls):
        print("hod:",cls.hod)

    @staticmethod
    def showF(married):
        married=married
        print("faculty status:",married)
        print("this is faculty class")


a=Students("sakib",22)
a.pt()
a.disp1()
a.showS()
a.show1("delhi","indian")
print()
c=Students("reema",20)
c.disp1()
Students.gender="female"            ## calling class anme with class vlaue
print("gender:",c.gender)
c.show1("mumbai","indian")

print()
b=faculty("rajesh",23)
b.disp2()
b.shows()
b.showF("married")
print()

d=faculty("sita",34)
d.disp2()
faculty.hod="chemistry"
print("hod:",d.hod)
d.showF("unmarried")





#eg
# class person:
#     gender="male"
#     def __init__(self,n,r):
#         self.n=n
#         self.r=r
#     def showS(self):
#         print(self.n,self.r)
#     @classmethod
#     def disp(cls):
#         print(cls.gender)
# a=person("sakib",22)
# a.showS()
# a.disp()
# print()
# b=person("reema",21)
# b.showS()
# # person.disp()
# # print(b.gender)
# person.gender="female"
# print(b.gender)
# print()
# c=person("sameer",12)
# c.showS()
# person.gender="shemail"
# print(c.gender)





