#!/bin/python3

class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __bool__(self):
        if self.age<31:
            return True
        else:
            return False
    def __str__(self):
        return("name is {}, age is {}".format(self.name,self.age))
    def __add__(self,other):
        return (self.age+other.age)
    def __len__(self):
        return len(self.name)
    def __lt__(self,other):
        return(self.age < other.age)

a = A('zr',35)
b = A('lhy',30)
c = a

if c is a:
    print("c is a")
else:
    print("not")
print(a+b)
print (len(a))
print (a<b)
