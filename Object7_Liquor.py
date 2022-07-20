class Liquor:
    def __init__(self,b,t,a,p,c,s):
        self.brand = b
        self.type = t 
        self.alcoholContent = a
        self.price_oneBottle = p
        self.color = c
        self.stock = s

    def sell_one_glass(self):
        self.price = round(self.price_oneBottle/14, 2)
        print("a shot of ",self.brand, " has been sold for PHP", self.price)
    def pour(self):
        print("you have poured a shot of ", self.brand)
    def drink(self):
        print("you have drank a shot of ", self.brand)
    def add_garnish(self):
        print("added a garnish!!")
    def buy_stock(self):
        self.stock = self.stock + 1
        print ("you have", self.stock, "bottle of ", self.brand)

liquor1 = Liquor("Cuervo", "Tequila","38%",1390,"clear/golden/dark",1)

print("you have", liquor1.stock, "bottle of ", liquor1.brand)
liquor1.pour()
liquor1.buy_stock()
liquor1.pour()
liquor1.add_garnish()
liquor1.drink()
liquor1.sell_one_glass()