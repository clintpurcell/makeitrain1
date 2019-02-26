class Screensaver:
    
    xspeed = 10
    yspeed = 5
    diameter = 50
    c = color(0,0,255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.y < 0 or self.y > width:
            self.yspeed *= -1
        if self.x < 0 or self.x > height:
            self.xspeed *= -1
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
