class Money:
  def __init__(self, a, f, c, l, o): #Don't forget the colon here!
    self.amount = a
    self.form = f
    self.currency = c
    self.location = l
    self.owner = o

  def spend(self, a):
    self.amount = a

  def changeForm(self, f):
    self.form = f

  def give(self, o):
    self.owner = o

  def convert(self, c):
    self.currency = c

  def transfer(self, l):
    self.location = l
    
  def number(self, a):
    self.amount = a
    
    

money1 = Money("1 million", "Cash", "US Dollars", "Philippines", "Me")

#Let's try the original attributes first.
print ( "I am " + money1.owner + " and I have " + money1.amount + " " + money1.currency + " in " + money1.form + ". " + \
       "I hid it in the " + money1.location + ".")

#I want to convert it to peso
money1.convert("Philippine Peso/s")
print ("I converted my money to " + money1.currency)
money1.number("54 000 000")
print ("I have " + money1.amount + " " + money1.currency)

#Let's convert it from Cash to Check
money1.changeForm("Check")
print ("I have " + money1.amount + " " + money1.currency + " in the form of " + money1.form )

#Let's give this money to  You!
money1.give("You")
print ("I have " + money1.amount + " " + money1.currency + " in the form of " + money1.form + " for " + money1.owner)

#But you have to find the money somewhere
money1.transfer("somewhere")
print (("I have " + money1.amount + " " + money1.currency + \
        " in the form of " + money1.form + " for " + money1.owner + " hidden " + money1.location))

#let's spend it!
money1.spend("You spent the money!")
print (money1.amount)

