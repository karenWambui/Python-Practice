
# class User:
#     def sign_in(self):
#         print('logged in')
# class Wizard(User):
#     def __init__(self,name,power):
#        self.name = name
#        self.power = power

#     def attack(self):
#       print(f'attacking with power of{self.power}')          

# class Archer(User):
#     def __init__(self,name,num_arrows):
#        self.name = name
#        self.num_arrows = num_arrows
    
#     def attack(self):
#         print(f'attacking with arrows: arrows
#         left-{self.num_arrows}')

# wizard1 = Wizard('Merlin',50)
# archer1 = Archer('Ron',500)
# (wizard1.sign_in())
# archer1.attack()
# class Cats:
#     def __init__(self,name,age):
#         self.name = name
#         self.name = age

# c1 = Cats('Lunar',2)
# print(c1.name)
# print(c1.age)


# class Cats:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#     def __str__(self):
#        return f'{self.name}({self.age})'

# p1 = Cats("John", 36)
# print(dir(Cats))

# print(p1) 



#polymorphism
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Drive!')

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Youre too fast')
       
class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
      print('Fly smoothly')  

c1 = Car('G-Wagon','Mercedes')
b1=  Boat('kataru','canoe')
a1 = Plane('KQ','jet')
# print(c1.brand,c1.model)
# print(b1.model,b1.brand)
# print(a1.brand,b1.model)
for x in(c1,b1,a1):
    x.move()