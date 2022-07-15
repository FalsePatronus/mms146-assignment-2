class Chair:
    def __init__(self, c, m, co, b, h):
        self.cushion = c
        self.material = m
        self.color = co
        self.backrest = b
        self.height = h
    
    def adjustHeight (self, h):
        self.height = h
    
    def removeCushion(self):
        self.cushion = ("Cushion Removed")

    def addCushion(self):
        self.cushion = ("You added another Cushion.")

   #Never forget colons! All def must end with colon!
    def recolor(self, co): 
        self.color = co

#Assigning the values
chair1 = Chair("Cushion Present", "Made of Wood", "Blue", "Backrest Absent", "1")


#Program proper
print ("Is there a cushion? Answer: " + chair1.cushion)
chair1.addCushion()
print (chair1.cushion)
chair1.removeCushion()
print (chair1.cushion)

print ("The original color of the chair is " + chair1.color)
chair1.recolor("pink")
print ("The new color is " + chair1.color)

print ("The original height is " + chair1.height + " meters")
chair1.adjustHeight("2")
print ("You added another " + chair1.height + " inches to the chair's height.")
