import platform
import SpriteManager

from Raindrop import Raindrop
from Screensaver import Screensaver
from Jiggle import Jiggle
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from shoot import shoot
from BigShooter import BigShooter

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(900, 900)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    SpriteManager.setPlayer(player)

    SpriteManager.spawn(Raindrop(50, 50, enemyTeam))
    SpriteManager.spawn(Raindrop(100, 100, enemyTeam))
    SpriteManager.spawn(Raindrop(150, 150, enemyTeam))
    SpriteManager.spawn(Raindrop(200, 200, enemyTeam))
    SpriteManager.spawn(Raindrop(250, 250, enemyTeam))
    SpriteManager.spawn(Raindrop(300, 300, enemyTeam))
    SpriteManager.spawn(Raindrop(350, 350, enemyTeam))
    SpriteManager.spawn(Raindrop(400, 400, enemyTeam))
    SpriteManager.spawn(Raindrop(500, 400, enemyTeam))
    SpriteManager.spawn(Raindrop(550, 350, enemyTeam))
    SpriteManager.spawn(Raindrop(600, 300, enemyTeam))
    SpriteManager.spawn(Raindrop(650, 250, enemyTeam))
    SpriteManager.spawn(Raindrop(700, 200, enemyTeam))
    SpriteManager.spawn(Raindrop(750, 150, enemyTeam))
    SpriteManager.spawn(Raindrop(800, 100, enemyTeam))
    SpriteManager.spawn(Raindrop(850, 50, enemyTeam))
    SpriteManager.spawn(Screensaver(50, 50, enemyTeam))
    SpriteManager.spawn(Jiggle(100, 100, enemyTeam))
    SpriteManager.spawn(shoot(200, 300, enemyTeam))
    SpriteManager.spawn(BigShooter(50, 100, enemyTeam))
    
                           
def draw():
    background(255)
    SpriteManager.animate()    
    
def keyPressed():
    global player
    SpriteManager.getPlayer().keyDown()    
        
def keyReleased():
    global player
    SpriteManager.getPlayer().keyUp()
