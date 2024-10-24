class Triangle():
    def __init__(self,base,area):
        self.base = base
        self.area = area

    def calculate_area(self):
        area = 0.5*self.base*self.area
        print(area)

t1 = Triangle(10,12)
t1.calculate_area()
t1 = Triangle(20,12)
t1.calculate_area()