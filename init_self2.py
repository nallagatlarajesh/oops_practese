class VivoMobile:
    def __init__(self): #some properities
        self.model="model"
        self.ram="ram"
        self.rom="rom"

    def info(self):
        print(self.model)
        print(self.ram)     #self.ram,
        print(self.rom)#  self.rom)
        print("")

#crerate object
mobile1=VivoMobile()
mobile1.info()

mobile2=VivoMobile()
mobile2.info()
