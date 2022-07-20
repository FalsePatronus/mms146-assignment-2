class Plant:
    def __init__(self,t,n,a,c,w,r,f,s):
        self.name = t
        self.num_Leaves = n 
        self.age = a
        self.color_Leaves = c
        self.watered = w
        self.recieved_Sunlight = r
        self.fertilized = f
        self.state = s

    def remove_Leaf(self):
        self.num_Leaves = self.num_Leaves - 1
    def water(self):
        self.watered = 1 
    def move_to_sunlight(self):
        self.recieved_Sunlight = 1
    def add_fertilizer(self):
        self.fertilized = 1
    def dispose(self):
        print(self.name + " has been disposed of")
        self.state = "dead"

plant1 = Plant("Monstera 1",6,1,"green",0,0,0,"healthy")

##before
print (plant1.name)
print ("num of leaves: ",plant1.num_Leaves)
print ("age: ", plant1.age)
print ("color of leaves: ", plant1.color_Leaves)
if plant1.watered == 0:
   print ("watered? - no")
elif plant1.watered == 1:
   print ("watered? - yes")
if plant1.recieved_Sunlight == 0:
   print ("sunlight? - no")
elif plant1.recieved_Sunlight  == 1:
   print ("sunlight? - yes")
if plant1.fertilized == 0:
   print ("fertilized? - no")
elif plant1.fertilized  == 1:
   print ("fertilized? - yes")
print (plant1.state)
print ("\n")

## methods applied
print ("\n")
plant1.water()
if plant1.watered == 0:
   print ("watered? - no")
elif plant1.watered == 1:
   print ("watered? - yes")
plant1.remove_Leaf()
print("num of leaves", plant1.num_Leaves)
plant1.move_to_sunlight()
if plant1.recieved_Sunlight == 0:
   print ("sunlight? - no")
elif plant1.recieved_Sunlight  == 1:
   print ("sunlight? - yes")
plant1.add_fertilizer()
if plant1.fertilized == 0:
   print ("fertilized? - no")
elif plant1.fertilized  == 1:
   print ("fertilized? - yes")
plant1.dispose()