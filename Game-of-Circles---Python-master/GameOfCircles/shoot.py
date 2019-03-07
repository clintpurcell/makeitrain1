import SpriteManager
import math
from Player import Player
from Sprite import Sprite
from Bullet import Bullet

class shoot(Sprite):
    
    xspeed = 3
    yspeed = 3
    diameter = 50
    c = color(250,200,10)
    mark = 0
    wait = 500
    go = True
    
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.y < 0 or self.y > width:
            self.yspeed *= -1
        if self.x < 0 or self.x > height:
            self.xspeed *= -1
            
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
    def aim(self, target):
        d = ((self.x - target.x)**2 + (self.y - target.y)**2)**.5
        xComp = target.x - self.x
        yComp = target.y - self.y
        magnitude = 10
        xVec = xComp/d * magnitude
        yVec = yComp/d * magnitude
        return PVector(xVec, yVec)
    
    def fire(self, vector):
        if(millis() - self.mark > self.wait):
            self.go = not self.go
            self.mark = millis()
            
        if(self.go):
            self.go = False
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
