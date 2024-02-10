class VivoMobile:
    def __init__(self): #some properities
        self.model="model"
        self.ram="ram"
        self.rom="rom"

    def info(self):
        print("Vivo",self.model,"info:")
        print("model",self.model)
        print("ram",self.ram)     #self.ram,
        print("rom",self.rom)#  self.rom)
        print("")

#crerate object
mobile1=VivoMobile()
mobile1.model="v20"   #override means take new values or give the values
mobile1.ram="8gb"
mobile1.rom="64gb"
mobile1.info()

mobile2=VivoMobile()
mobile2.info()
