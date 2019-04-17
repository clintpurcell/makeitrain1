from Sprite import Sprite
import SpriteManager

class burstShot:
    def keyDown(self):
            SpriteManager.spawn(Bullet(getPlayer().x, getPlayer().y, PVector(0, 10), 100))
            SpriteManager.spawn(Bullet(getPlayer().x, getPlayer().y, PVector(0, -10), 100))
            SpriteManager.spawn(Bullet(getPlayer().x, getPlayer().y, PVector(10, 0), 100))
            SpriteManager.spawn(Bullet(getPlayer().x, getPlayer().y, PVector(-10, 0), 100))
            SpriteManager.spawn(Bullet(getPlayer().x, getPlayer().y, PVector(10, 10), 100))
            SpriteManager.spawn(Bullet(getPlayer().x, getPlayer().y, PVector(10, -10), 100))
            SpriteManager.spawn(Bullet(getPlayer().x, getPlayer().y, PVector(-10, 10), 100))
            SpriteManager.spawn(Bullet(getPlayer().x, getPlayer().y, PVector(-10, -10), 100))
