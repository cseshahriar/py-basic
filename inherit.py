# inheritence 
class Math: # parent class 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def sum(self):
        return self.x + self.y 

class MathExtended1(Math): # child class 
    def __init__(self, x, y):
        super().__init__(x, y)
    
    # override 
    def sum(self):
        return self.x + self.y + 100
    # overloading not support
    
    def substract(self):
        return self.x - self.y
    
    def show_all(self):
        print('Sum : ', str(super().sum()))
        print( 'Subtract: ', str(self.substract()) )

class MathExtra:
    def division(self, x, y):
        return x / y 
# multiple inheritence 
class MathExtended2(MathExtended1, MathExtra):
    def __init__(self, x, y):
        super().__init__(x, y)

    def multiplication(self):
        return self.x * self.y 

math_ext2 = MathExtended2(10, 2)
'''
print('Sun ', str(math_ext2.sum()))
print('Sun ', str(math_ext2.substract()))
print('Sun ', str(math_ext2.multiplication()))
print('Sun ', str(math_ext2.division(x=math_ext2.x, y=math_ext2.y)))
'''
math_ext2.show_all()