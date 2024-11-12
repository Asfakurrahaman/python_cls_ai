class GoldRate:

    def __init__(self, xauusdm, weight, tk):
        self.xauusdm = xauusdm
        self.weight = weight
        self.tk = tk

    def ounce(self):
        Tk = (self.weight / 31.1035) * self.xauusdm * self.tk
        return Tk

price = GoldRate(2737, 11.66, 124)
gold_price_in_tk = price.ounce()
print(gold_price_in_tk)