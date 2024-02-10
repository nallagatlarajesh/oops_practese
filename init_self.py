class VivoMobile:
    def __init__(self,rom,model,ram): #some properities
        self.model=model
        self.ram=ram
        self.rom=rom

    def info(self):
        print(self.model,self.ram,self.rom)

    def example(self):
        print("example is working....")
#we create objects
mob1=VivoMobile("8gb","x50","256")


#accesing the attributes
mob1.info()

mob2=VivoMobile("4gb","4xb","128gb")
mob2.info()

#accesing the attributes
#mob1.example()
