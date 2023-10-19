# inheritence with polimorphism 
#different ckasses with the sane methode
#parent class =vehicle 
#child class = car ,boat, plane
#same methode is move 
#attributes are drive,sail,fly

class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("drive!")
class car(vehicle):
    pass
    #def move(self):
        #print("drive!")

class boat(vehicle):
    def move(self):
        print("sail!")

class plane(vehicle):
    def move(self):
        print("fly")
        
#object
car1=car("ford","mustang")
boat1=boat("ibiza","touring 20")
plane1=plane("boeing",747)

#access attributes
car1.move()
plane1.move()
boat1.move()
print(car1.brand,car1.model,"and",)

print("GAP 1   ,      2     ,    3")

#extra use with for loop
#extra
for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
