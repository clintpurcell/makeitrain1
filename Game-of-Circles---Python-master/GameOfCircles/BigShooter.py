import SpriteManager
import math
from Player import Player
from Sprite import Sprite
from BigShot import BigShot

class BigShooter(Sprite):
    
    speed = 2
    diameter = 90
    c = color(250,20,10)
    mark = 0
    wait = 2000
    go = True
    sw = 3
    
    def handleCollision(self):
        self.sw -= 1
        if self.sw < 1:
            SpriteManager.destroy(self)
    
    def display(self):
        fill(self.c)
        stroke(0)
        strokeWeight(self.sw)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        noStroke()
        
    def __init__(self, x, y, team):
        self.x = random(0, 900)
        self.y = random(0,50)
        self.team = team
    
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
        magnitude = 4
        xVec = xComp/d * magnitude
        yVec = yComp/d * magnitude
        return PVector(xVec, yVec)
    
    def fire(self, vector):
        if(millis() - self.mark > self.wait):
            self.go = not self.go
            self.mark = millis()
            
        if(self.go):
            self.go = False
            SpriteManager.spawn(BigShot(self.x, self.y, vector, self.team))
