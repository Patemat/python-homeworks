import math
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def radius(self):
        return self.radius
    def diametr(self):
        return 2*self.radius
    def __len__(self):
        return 2*math.pi*self.radius
    def square(self):
        return math.pi*(self.radius**2)
    def f(self,k):
        self.radius*=k
    def __mul__(self,n):
        return self.radius * n
r= 3
k= 2
n= 4
obj=Circle(r)
print(r)
print(obj.diametr())
print(obj.__len__())
print(obj.square())
print(r*k)
print(r*n)
