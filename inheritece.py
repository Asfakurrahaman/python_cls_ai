class Phone:

    def call(self):
        print("call")

    def massege(self):
        print("massage")

class Mobile(Phone):

    def photo(self):
        print("photo")

a = Mobile()
a.photo()
a.call()
a.massege()
print(issubclass(Mobile,Phone))