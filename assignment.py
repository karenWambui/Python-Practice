class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self,distance):
        self.distance = distance
          
    def slope(self,slope):
        self.slope = slope
li = Line(coor1=(4,6),coor2=(8,9))
print(li.coor1,li.coor2)
li.distance()
print(li.distance())
li.slope()
print(li.slope()) 