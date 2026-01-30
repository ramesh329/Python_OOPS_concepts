#initiate a class
class employee:
    #special method/magic method/dunder method -- constructor
    def __init__(self):  #method-1
        #attritbutes
        print("started executing attributes")
        self.id = 123
        self.salary =  25000
        self.designation =  "Datacientist"
        print('attributes initiation is completed')

    def travel(self,destination):  #method-2
        print("this travel function was called manually")
        print(f'employee is travelling to {destination}')

 
#creating an object/instance of the class
ramesh = employee()


print(type(ramesh))



