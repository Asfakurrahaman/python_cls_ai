class Phone:
    def __init__(self):
        print("call")


class massege(Phone):

    def __init__(self):
        super().__init__()
        print("ringing")

m = massege()