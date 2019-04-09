from Sprite import Sprite
import SpriteManager

class Pwr(Sprite):
    
    diameter = 40
    c = color(150, 30, 125)
    speed = 2
    
    def __init__(self, x, y, team):
        self.x = random(0, 900)
        self.y = random(0,900)
        self.team = team
    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        
    def handleCollisions(self, other):
        player = SpriteManager.getPlayer()
        r1 = self.diameter / 2
        r2 = self.diameter / 2
        if r1 + r2 >dist(self.x, self.y, player.x, player.y):
            println("BANG")
            SpriteManager.destroy(self)
