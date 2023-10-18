class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(person):
        print(self.fnamr,self.lname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)         #super() function
        self.graduationyear=year
    
    def welcome(self):
        print("welcome",self.fname,self.lname,"to the class of ",self.graduationyear)
#object
x=student("rajesh","n",2024)
x.welcome()
