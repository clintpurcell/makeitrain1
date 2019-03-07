from Sprite import Sprite
class Raindrop(Sprite):
    speed = 3
    diameter = 20
    c = color(0,0,255)
    
    def __init__(self, x, y, team):
        self.x = random(0,900)
        self.y = random(0,50)
        self.team = team
        
    def move(self):
        self.y += self.speed
        if self.y < 0 or self.y > width:
            self.speed *= -1
            if self.y > width:
                self.y = 0
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
