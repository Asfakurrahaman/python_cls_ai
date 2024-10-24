class Students:
    name = ""
    roll = ""
    gpa = ""
    rg = ""

    def __init__(self,name,roll,gpa,rg):
        self.name= name
        self.roll = roll
        self.rg = rg
        self.gpa = gpa
    def display(self):
        print(f"Name : {self.name},Roll : {self.roll}, GPA : {self.gpa}, RG : {self.rg}")

Rohim = Students("asfak",101,4.08,1012)
Rohim.display()

Korin = Students("rony",102,3.39,1013)
Korin.display()

asfak = Students("sayed",103,4.00,12456)
asfak.display()

joshim = Students("Joshim",104,3.58,1144422)
joshim.display()