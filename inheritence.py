class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
    def speak(self):
        return f"he can speaks three lanuages"
class student(person):                        #student is chikld class
                                              #person is parent or base class like 
    pass
#object (instance) of class 
x=student("rajesh","n")
#access attributes
x.printname()
x.speak()
