class className:
    def __init__(self, name):
        self.name = name
    
    def setData(self, data):
        self.info = data

    def getData(self):
        print("Name: ", self.name,"\nInfo: ", self.info)


obj = className('Parent Class')
obj.setData(1)
obj.getData()

