
#Polymorphism
class Dogs:
    def __init__(self,breed,bark):
      self.breed = breed
      self.bark= bark

    def __str__(self):
        return "cats are meowing"
   
    def bite(self):
       print(self.bark + 'barking')

class Cats:
       
    def __init__(self,name,fur):
      self.name = name
      self.fur = fur

    def  __str__(self):
       return "The bark is loud"
    # def __len__(self):
    #    return self.bark
    def bite(self):
     print(self.name + 'Meowing')

Shepherd = Dogs(bark = 'gugugu',breed ='Mutina')
print(Shepherd)
Puss = Cats(name ='Karen', fur ='hairy')
print(Puss)
pets= [Puss,Shepherd]
for pet in pets:
   pet.bite()