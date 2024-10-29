class Bike:
    def __init__(self,name,coler):
        self.name = name
        self.color = coler

    def __eq__(self, other):
        return self.name == other.name and self.color == other.color

    def __str__(self):
        return (f"Name = {self.name},color = {self.color}")
    def display(self):
        print(f"Name = {self.name},color = {self.color}")

bike = Bike("Yamaha R15","Blue")
bike2 = Bike("Yamaha R15","Blue")
# print(bike)
print(bike==bike2)