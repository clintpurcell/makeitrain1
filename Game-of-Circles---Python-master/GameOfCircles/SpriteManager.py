import math
import SpriteManager
from Player import Player
from Pwr import Pwr

sprites = []
destroyed = []
    
playerTeam = 1
enemyTeam = 2
AromorPwr = 3
QuadPwr = 4

PlayerBulletTeam = 100

def setPlayer(playerInstance):
    global player
    player = playerInstance
    spawn(player)
    
def getPlayer():
    global player
    return player
        
def destroy(target):
    destroyed.append(target)
        
def spawn(obj):
    sprites.append(obj)
        
def animate():
    for sprite in sprites:
        sprite.animate()
    checkCollisions()
    bringOutTheDead()
        
def checkCollisions():
    for i in range(0, len(sprites)):
        for j in range(i + 1, len(sprites)):
            a = sprites[i]
            b = sprites[j]
            if a.team == 1 and b.team == 3 and collision(a, b):
                b.handleCollision(a)
                Player.sw += 10
                SpriteManager.spawn(Pwr(20, 400, 3))
            elif a.team == 1 or a.team == 3 and b.team == 100 and collision(a, b):
                pass
            elif a.team != b.team and collision(a, b):
                a.handleCollision(b)
                b.handleCollision(a)
                
def collision(a, b):
    r1 = a.diameter / 2
    r2 = b.diameter / 2
    return r1 + r2 > math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))

                
def bringOutTheDead():
    for sprite in destroyed:
        if sprite in sprites:
            sprites.remove(sprite)
        destroyed.remove(sprite)
