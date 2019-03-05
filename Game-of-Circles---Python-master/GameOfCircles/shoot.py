import SpriteManager
import math
from Player import Player
from Sprite import Sprite
from Bullet import Bullet

class shoot(Sprite):
    
    speed = 5
    diameter = 50
    c = color(0,0,255)
    
    def move(self):
        self.x += self.speed
        if(self.x < 0 or self.x > width):
            self.speed *= -1
        
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
    def aim(self, target):
        d = ((self.x - target.x)**2 + (self.y - target.y)**2)**.5
        xComp = target.x - self.x
        yComp = target.y - self.y
        xVec = xComp/2 * .1
        yVec = yComp/2 * .1
        return PVector(xVec, yVec)
    
    def fire(self, vector):
        SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
            
