from Sprite import Sprite
class BigShot(Sprite):
    
    diameter = 50
    c = color(200, 200, 100)
    
    
    
    def __init__(self, x, y, vector, team):
        self.x = x
        self.y = y
        self.vector = vector
        self.team = team
        
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
