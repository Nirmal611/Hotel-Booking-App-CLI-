import inspect


class Parent:
    def __init__(self,x=0,y='a'):
        self.x=x
        self.y=y
        print(x,y,'from parent')


class Child(Parent):
    def __init__(self,x=0, y='a',z='heyy'):
        super().__init__(x, y)
        self.z= z


x=Child(x=1,z='aight',y='bruh')
argspec = inspect.signature(Parent.__init__)
print(argspec)
print(x.x,'  ',x.y,'   ',x.z)