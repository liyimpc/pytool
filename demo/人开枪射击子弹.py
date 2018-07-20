#!/usr/bin/python3

'''
人
类名：Person
属性：gun
行为：fire

枪
类名：Gun
属性：bulletBox
行为：shoot

弹夹
类名：BulletBox
属性：bulletCount
行为：
'''

from demo.person import Person
from demo.gun import Gun
from demo.bulletBox import BulletBox

# 弹夹
bulletBox = BulletBox(5)

# 枪
gun = Gun(bulletBox)

# 人
p = Person(gun)
p.fire()
p.fire()
p.fire()
p.fire()
p.fillBullet()
p.fillBullet()
p.fire()
