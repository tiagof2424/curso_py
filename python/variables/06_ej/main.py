eje_ax =0
eje_ay =0
eje_bx =1
eje_by =1
d = (eje_ax-eje_bx)**2+(eje_ay-eje_by)**2/0.5
print (d)
class APC:
    def __init__(self,name,age):
        self.name = name
        self.age = age
persone = APC ("tiago",16)

class Empleado(APC):
    def __init__(self,name,age,money):
        super().__init__(name,age)
        self.money