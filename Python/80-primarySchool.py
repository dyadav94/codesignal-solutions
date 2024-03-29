class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return '{} x {} = {}'.format(self.height, self.width, self.area)

    @property
    def area(self):
        return self.area
    
    @area.getter
    def area(self):
        return self.width*self.height
    
    
        
def primarySchool(height, width):
    return str(Rectangle(height, width))