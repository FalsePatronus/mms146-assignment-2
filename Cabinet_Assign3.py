class Cabinet:
    def __init__(self, s, c, ht, m, sh):
        self.size = s
        self.color = c
        self.handleType = ht
        self.material = m
        self.shelves = sh
    
  #Let's Repaint the Cabinet!
    def change_Color(self, c):
        self.color = c
   
  #For Opening and closing the cabinet
    def open_shelf(self, sh):
        self.shelves = "A shelf is opened."
  
    def close_shelf(self, sh):
        self.shelves = "the shelf is now closed."
    
  #changing the handles
    def change_handles(self, ht):
        self.handleType = ht
    
 #Let's experiment by opening the shelf, adding an item, then closing it again.
  
    def add_item(self, sh):
        self.shelves =  "You stored an item."
    
  #Okay, let's start reviewing our code! 
  #Our Cabinet is 5 meters tall, paint is dark brown, handles are gold, made of narra, and all shelves are closed.

cabinet1 = Cabinet("5 meters tall, ", "Dark Brown", " Gold handles, ", "made of Narra, ", "Shelves are closed.")
  
  #This is for calling all the attributes of the Cabinet.
print ("The original attributes of our cabinet is " + cabinet1.size + cabinet1.color + "," + cabinet1.handleType + cabinet1.material + "all of " + cabinet1.shelves)

  #Let's repaint the color to pink.
print ("But I don't like a " + cabinet1.color + " cabinet")
cabinet1.change_Color("pink")
print ("let's paint it to " + cabinet1.color)

  #Let's open and close the shelves.
print ("Before changing the code, all the " + cabinet1.shelves)
cabinet1.open_shelf(" ")
print ("after changing the code, " + cabinet1.shelves)
cabinet1.close_shelf(" ")
print ("By changing the code again, " + cabinet1.shelves)

  #Now let's change the handle type
print ("The original attribute of the cabinet is " + cabinet1.handleType)
cabinet1.change_handles("diamond handles")
print ("Now it is " + cabinet1.handleType + ".")

  #This one is an experiment code. We would like to display every changes made.
print ("The new attributes of our cabinet are " + cabinet1.size + cabinet1.color + " paint, "+ cabinet1.handleType + ", " + cabinet1.material + cabinet1.shelves)

  #Let's try to add an item to the cabinet
cabinet1.open_shelf(" ")
print ("TO add an item, first, " + cabinet1.shelves)
cabinet1.add_item(" ")
print ("If you put an item, " + cabinet1.shelves)
cabinet1.close_shelf(" ")
print ("Then, of course, push the drawer so that " + cabinet1.shelves)
