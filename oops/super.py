class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width



class Square(Rectangle):
    def __init__(self, length=None,width=None):
        super().__init__(length, width)


    def Area(self):
        return self.length*self.width






class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height


    def volume(self):
        return self.length*self.width*self.height


class ubuntu(Rectangle):
    def __init__(self, length, width):
        super(ubuntu, self).__init__(length, width)

    def capacity(self):
        return self.length*self.width


cl= Square(3, 4)
print(cl.Area())

ck= Cube(4, 5, 6)
print(ck.volume())

bl= ubuntu(9, 6)
print(bl.capacity())