class Students:
    name = ""
    roll = ""
    gpa = ""
    rg = ""

    def set_valu(self,name,roll,gpa,rg):
        self.name= name
        self.roll = roll
        self.rg = rg
        self.gpa = gpa
    def display(self):
        print(f"Name : {self.name},Roll : {self.roll}, GPA : {self.gpa}, RG : {self.rg}")

Rohim = Students()
Rohim.set_valu("asfak",101,4.08,1012)
Rohim.display()

Korin = Students()
Korin.set_valu("rony",102,3.39,1013)
Korin.display()

asfak = Students()
asfak.set_valu("sayed",103,4.00,12456)
asfak.display()