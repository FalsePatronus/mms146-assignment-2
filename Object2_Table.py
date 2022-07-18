class Table:
  def __init__(self, s, m, h, w, g, p):
    self.size = s
    self.material = m
    self.height = h
    self.weight = w
    self.glass = g
    self.position = p
    
  def remove_glass(self):
    self.glass = "glass removed."

  def moveto_North(self):
    self.position = "North."
    
  def moveto_East(self):
    self.position = "East."
    
  def moveto_West(self):
    self.position = "West."
    
  def moveto_South(self):
    self.position = "South."

#Let's assign the attributes to two objects
table1 = Table("large", "Metal", "1 meter", "20 KG", "No glass", "Center")
table2 = Table("small", "Wood", "0.50 meter", "15 KG", "With glass", "Center")

print ("table1 is made of " + table1.material)
print ("table2 is " + table2.height + " tall.")

print ("table2 is " + table2.glass)
table2.remove_glass()
print ("table2 has now its " + table2.glass)

print ("table1 is at " + table1.position)
table1.moveto_North()
print ("table1 is moved to " + table1.position)
