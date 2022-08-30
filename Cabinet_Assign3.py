class Cabinet:
    def __init__(self, s, c, ht, m, sh):
        self.__size = s # This is needed to be encapsulated because we should avoid changing the size of the cabinet, unless needed.
        self.color = c
        self.handleType = ht
        self.__material = m #This should also be encapsulated because, irl, this is constant.
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

#Let's test our encapsulated codes
    def set_size(self, s): #Remember, it is only valid to change the size/material of the cabinet if necessary, which is rarely done irl
        self.__size = s
        
    def get_size(self):
        print ("cabinet is", self.__size)
        
    def set_material(self, m): 
        self.__material = m
        
    def get_material(self):
        print (self.__material)
        

       #This class is the child class
class CenterTable(Cabinet):
    def __init__(self, s, c, ht, m, sh, g):
        super().__init__(s, c, ht, m, sh)
        self.glass = g

    def countertop(self):
        print("The drawer countertop is made of " + self.glass)

  #### Main Program ####   
  # Okay, let's start reviewing if our code is working properly.
  # Our Cabinet is 5 meters tall, paint is dark brown, handles are gold, made of narra, and all shelves are closed.
  # The Centertble has a fiberglass countertop.

cabinet1 = Cabinet("5 meters tall ", "Dark Brown", " Gold handles, ", "made of Narra, ", "Shelves are closed.")
centertable1 = CenterTable("1 meter tall, ", "Oak White", " Four handles, ", "made of Bamboo, ", "Shelves are closed.", "Fiber Glass")
  
  #This is for calling all the attributes of the Cabinet.
print ("The changeable attributes of our cabinet is " + cabinet1.color + "," + cabinet1.handleType + "all of " + cabinet1.shelves)
cabinet1.get_size() 



  #Let's repaint the color to pink.
print ("because I don't like a " + cabinet1.color + " cabinet")
cabinet1.change_Color("pink")
print ("let's paint it to " + cabinet1.color)

  #Let's open and close the shelves.
print ("Before changing the code, all the " + cabinet1.shelves)
cabinet1.open_shelf(" ")
print ("after changing the code, " + cabinet1.shelves)
cabinet1.close_shelf(" ")
print ("By changing the code again, " + cabinet1.shelves)

  #Now let's change the handle type
print ("The original handle of the cabinet is " + cabinet1.handleType)
cabinet1.change_handles("diamond")
print ("Now it has " + cabinet1.handleType + " handles.")

  #This one is an experiment code. We would like to display every changes made.
print ("The changed attributes would display that our cabinet has "+  cabinet1.color + " paint, "+ cabinet1.handleType + ", "  + cabinet1.shelves)

  #Let's try to add an item to the cabinet
cabinet1.open_shelf(" ")
print ("To add an item, first, " + cabinet1.shelves)
cabinet1.add_item(" ")
print ("By putting an item, " + cabinet1.shelves)
cabinet1.close_shelf(" ")
print ("Then, of course, push the drawer so that " + cabinet1.shelves)


#Now, let's try if our CenterTable code is working.
print ("Meanwhile, the Center Table has " + centertable1.handleType)
print ("It is painted " + centertable1.color)
centertable1.countertop()

#This part is for testing out our encapsulated code, which is "size", into a child class, which is CenterTable
centertable1.get_size()
centertable1.set_size(".5 meter tall")
centertable1.get_size()



