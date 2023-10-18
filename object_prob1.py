#insert a function that prints a greting and excute it on the p1 object:
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("hello my name is ",self.name)
#object
p1=person("rajesh",30)
p1.myfunc()
