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
from Pwr import Pwr

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(900, 900)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, 1)
    SpriteManager.setPlayer(player)
    
    SpriteManager.spawn(Pwr(20, 400, 3))
    SpriteManager.spawn(shoot(20, 400, 2))
    
                           
def draw():
    background(255)
    SpriteManager.animate()    
    
def keyPressed():
    SpriteManager.getPlayer().keyDown()    
        
def keyReleased():
    SpriteManager.getPlayer().keyUp()
