class add:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,object1):
        return add(self.x+object1.x,self.y+object1.y)

first = add(3,7)
second = add(5,7)
third = first+second
print(third.x)
print(third.y)
