import SpriteManager
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
        #solve unit vector
        return PVector(0, 10) #use vector value here
    
    def fire(self, vector):
        SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
