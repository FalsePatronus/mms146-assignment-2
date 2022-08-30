class Coffee:
    ##attributes
    def __init__(self,n,b,c,t,s):
        self.name = n
        self.__beanType = b ## bean type can't be changed in the middle of brewing - can be changed before brewing
        self.__colorRoast = c ## beans get roasted before brewing - can't be changed in the brewing process 
        self.__taste = t 
        self.state = s ## unbrewed, iced, or hot (default is unbrewed until coffee has been brewed)

    ## getter-setter methods - COFFEE BEAN TYPE
    def set_beanType(self,b):
        self.__beanType = b
        print("changed beans to", self.__beanType)

    def get_beanType(self):
        print(self.name, "beans are",self.__beanType, "beans")

    ## getter-setter methods - COLOR OF ROAST
    def set_colorRoast(self,c):
        self.__colorRoast = c
        
    ## getter-setter methods - TASTE
    def set_taste(self,t):
        self.__taste = t
        print("taste of brew is", self.__taste)
        
    def get_taste(self):
        print(self.name, "'s taste of brew is", self.__taste)
        

    def get_colorRoast(self):
        print(self.name,"color of beans:",self.__colorRoast)

    ## methods
    def drink_coffee(self):
        self.state = self.name + " " + "has been drank"
        print(self.state)
        
    def brew_coffee(self):
        self.state = "hot"
        print(self.name, "has been brewed and is", self.state)
        
    def add_ice(self):
        self.state = "iced"
        print("added ice to", self.name)

class Frappe(Coffee):
    def __init__(self,n,b,c,s,t,fl,m):
        super().__init__(n,b,c,t,s)
        self.__flavor = fl ## flavor is stated in name - cannot be changed
        self.milk = m

    def get_flavor(self):
        print ("Flavor is ", self.__flavor)

coffee1 = Coffee("coffee1","Robusta", "light roast", "bitter", "unbrewed")

frappe1 = Frappe("Caramel Frappe", "Elcesca", "dark roast","iced", "smooth and sweet", "Caramel","Soy Milk")

## testing getter-setter methods
coffee1.get_beanType()
coffee1.get_taste()

coffee1.set_beanType("Arabica")
coffee1.set_taste("smooth and sweet")
## prints out coffee1's attributes'
coffee1.get_beanType()
print("coffee1 is currently", coffee1.state)

## coffee will be drank, unless it is unbrewed
if coffee1.state != "hot":
   print("coffee cannot be drank as it is unbrewed.")
elif coffee1.state == "hot":
   coffee1.drink_coffee()
   print (coffee1.state)
elif coffee1.state == "iced":
   coffee1.drink_coffee()
   print (coffee1.state)

## shows us that coffee may not be taken as it has yet to be made
coffee1.drink_coffee()

## brews coffee to be drank
coffee1.brew_coffee()

##cold coffee
coffee1.add_ice()
print ("coffee is", coffee1.state)

## now that the coffee is hot or iced, it may now be consumed
coffee1.drink_coffee()

## Printing out frappe1's attributes
frappe1.get_beanType()
frappe1.set_beanType("Arabica") ## changes bean type to another bean
print(frappe1.name)
print(frappe1.state)

## Getting the taste and flavor of frappe1
frappe1.get_taste()
frappe1.get_flavor()

## frappe has been consumed!
frappe1.drink_coffee()
