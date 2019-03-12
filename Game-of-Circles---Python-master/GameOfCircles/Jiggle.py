from Sprite import Sprite
class Jiggle(Sprite):
    
    speed = 8
    diameter = 50
    c = color(0,0,255)
    
    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.y = constrain (self.y, 0, height)
