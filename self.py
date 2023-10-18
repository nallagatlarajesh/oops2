#without self name and we use  another name instead of self 
class person:
    def __init__(mysillyobject,name,age):   #self ==mysilly object
        mysillyobject.name=name
        mysillyobject.age=age
    def myfunc(abc):
        return f"hello my name is {abc.name} "
        #print("hello my name is ",abc.name)
p1=person("rajesh",30)
p1.myfunc()
