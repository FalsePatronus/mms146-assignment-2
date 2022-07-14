class Coffee:
    ##attributes
    def __init__(self,a,b,c,t,s,m,sy,cr):
        self.aroma = a
        self.beanType = b
        self.colorRoast = c 
        self.taste = t 
        self.state = s ## unbrewed, iced, or hot (default is unbrewed until coffee has been brewed)
        self.additionMilk = m ## tells us if milk has been added
        self.additionSyrup = sy ## tells us if syrup has been added
        self.additionCreamer = cr ## tells us if creamer has been added
    ## methods
    def drink_coffee(self):
        self.state = "coffee has been drank"
    def brew_coffee(self):
        self.state = "hot"
    def add_ice(self):
        self.state = "iced"
    def add_milk(self):
        self.additionMilk = "has milk"
    def add_syrup(self):
        self.additionSyrup = "has syrup" 
    def add_creamer(self):
        self.additionCreamer = "has creamer"
    def add_ice(self):
        self.state = "iced"

coffee1 = Coffee("strong","Arabica","dark roast", "smooth and sweet", "unbrewed", "no milk", "no syrup","no creamer")

## prints out coffee1's attributes
print("coffee1 is made of", coffee1.beanType, "beans." )
print("coffee1 has", coffee1.aroma, "aroma, and tastes", coffee1.taste)
print("coffee1 is currently", coffee1.state)
print("additions:", "\n", coffee1.additionMilk,"\n" , coffee1.additionSyrup, "\n",coffee1.additionCreamer) 

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

##adds milk, creamer, and syrup
coffee1.add_milk()
coffee1.add_syrup()
coffee1.add_creamer()
print ("additions:", "\n", coffee1.additionMilk, "\n",coffee1.additionSyrup,"\n", coffee1.additionCreamer)

##cold coffee
coffee1.add_ice()
print ("coffee is", coffee1.state)

## now that the coffee is hot or iced, it may now be drank
coffee1.drink_coffee()
print (coffee1.state)