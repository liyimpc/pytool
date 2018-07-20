class Person(object):
    def __init__(self, gun):
        self.gun = gun

    def fire(self):
        self.gun.shoot()

    def fillBullet(self):
        self.gun.bulletBox.bulletCount += 1