class Math:
    def __init__(self, x, y):
        self._x = x 
        self._y = y 
    def sum(self):
        return self._x + self._y 

math = Math(2, 4)
print(math._x)