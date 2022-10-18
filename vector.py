import math
import random

# class and fucntions taken from 
# https://github.com/Mar19845/Graficas/blob/main/Proyecto1/lib.py
class Vector:
    def __init__(self, x:int =0, y:int =0):
        self.initialize(x,y)
    # initialize x,y coordinates
    def initialize(self,x:int,y:int)-> None:
        self.x,self.y = x,y
    # randomize a new position coordinate x,y by a multiplier value
    def randomize(self,multiplier:int )-> None:
        self.x,self.y = int(random.random() * multiplier),int(random.random() * multiplier)
    
    # calculate the distance from the orginal vector to another
    # expected a vector object
    def distance(self,other_vector ) -> float:
        return math.sqrt((self.x - other_vector.x) ** 2 + (self.y - other_vector.y) ** 2)
    
    # retunrs the lenght of the vector
    def lenght(self)-> int:
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    # returns Vector object 
    def normal(self):
        l = self.lenght()
        # if lenght of the vector is 0 return 
        #vector = Vector(self.x / l, self.y / l) if l > 0 else Vector()
        return Vector(self.x / l, self.y / l) if l > 0 else Vector()
    
    # calculate de direction to another vector
    # expected a vector object
    # return new Vector normal
    def direction_to(self,other_vector):
        new_v = Vector(other_vector.x - self.x, other_vector.y - self.y)
        return new_v.normal()
    
    # expected a vector object
    # returns the angle from the vector to another vector
    def angle(self,other_vector)-> float:
        dot = self.x * other_vector.x + self.y * other_vector.y
        return math.acos(dot / (self.lenght() * other_vector.lenght()))
    
    # sums two vectors
    # expected a vector object
    # return new Vector normal
    def add(self,other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)
    
    # substracte two vectors
    # expected a vector object
    # return new Vector normal
    def substracte(self,other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)
    
    # scalar multiplication
    # expected a vector object
    # return new Vector normal
    def scalar_mult(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)