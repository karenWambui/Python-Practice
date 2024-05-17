# Inheritance
class  Vehicle: 

  def __init__(self,name,mileage):
    self.name = name
    self.mileage= mileage
  def hoot(self): #static
    print('PIPIIPIII')
  def speed(self,speed):
    self.speed = speed
    self.name = 'GG-wagon'

class Lorry(Vehicle):
    def __init__(self,name,mileage):
      Vehicle.__init__ (self,name,mileage)#calling the Vehicle's constructor(parent)      
Canter =Lorry(name = 'UBV', mileage=100) 
print(Canter.name,Canter.mileage)
Canter.hoot()
 



 #Attributes
# Mercedes = Vehicle(name='G-Wagon',mileage=0)
# print(Mercedes.name,Mercedes.mileage)
# Mercedes.hoot()
# Mercedes.speed(100)
# print(Mercedes.speed)
# Audi = Vehicle(name ='RS8',mileage=2000)
# Audi.speed(80)
# print(Audi.name,Audi.mileage,Audi.speed)
