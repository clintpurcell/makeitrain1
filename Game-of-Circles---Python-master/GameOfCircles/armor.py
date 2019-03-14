from Sprite import Sprite
import SpriteManager

class armor:
    def display(self):
        fill(self.c)
        stroke(0)
        strokeWeight(self.sw)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        noStroke()
    
    def handleCollision(self):
        self.sw -= 1
        if self.sw < 1:
            SpriteManager.destroy(self)
            
