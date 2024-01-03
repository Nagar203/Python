class parentClassOne:
    def __init__(self, name):
        self.name = name

    def setData(self, info):
        self.data = info

    def getData(self):
        print("Name: ", self.name, "\nInfo: ", self.data)

class parentClassTwo:
    def setRollNum(self, roll):
        self.roll = roll

class childClass(parentClassOne, parentClassTwo): # muutiple Inheritance
    def __init__(self, name):
        super().__init__(name) #parent constructor call

    def printData(self):
        super().setRollNum(10) # parent class function call
        super().setData(28) # parent function call
        super().getData() #parent function call
        print("Roll Number: ", self.roll) # Acess parent varialbes
        
obj = childClass('Chandra')
obj.printData()