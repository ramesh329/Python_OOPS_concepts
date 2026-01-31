#initiate a class
class employee:
    #special method/magic method/dunder method -- constructor
    def __init__(self):  #method-1
        #attritbutes
        #print("started executing attributes")
        print(id(self))
        self.id = 123
        self.salary =  25000
        self.designation =  "Datacientist"
        #print('attributes initiation is completed')

    def travel(self):  #method-2
        print("this travel function was called manually")
        print(f'employee is travelling to delhi')

 
#creating an object/instance of the class
ramesh = employee()
print(id(ramesh))


#print(type(ramesh))


ramesh.travel()
