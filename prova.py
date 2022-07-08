class MyClass:
    variabile="cane"
    def MyFunction(self):
        return self.variabile
     
y=MyClass()
x=MyClass()

x.variabile="gatto"

print(x.MyFunction())
