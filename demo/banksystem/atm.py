'''
atm机
'''
import random
import simplejson

from demo.banksystem.card import Card
from demo.banksystem.user import User


class ATM(object):

    def __init__(self, allUser):
        self.allUser = allUser

    # 开户
    def createUser(self):
        # 向用户字典中添加键值对（卡号-用户）
        name = input("请输入您的姓名：")
        idcard = input("请输入您的身份证号：")
        iphone = input("请输入您的电话号码：")

        prestoreMoney = int(input("请输入预存款金额："))
        if prestoreMoney < 0:
            print("预存款金额输入有误!开户失败……")
            return -1

        onePasswd = input("请设置密码：")
        # 验证密码
        if not self.validPwd(onePasswd):
            print("密码输入错误！！开户失败……")

        # 所有需要的信息就齐全了
        cardNum = self.generalCardNum()

        card = Card(cardNum, onePasswd, prestoreMoney)
        user = User(name, idcard, iphone, card)

        # 存到字典
        self.allUser[cardNum] = user
        print("开户成功！您的卡号是:", user.card.cardId)

    # 查询
    def searchUserInfo(self):
        cardNum = input("请输入您的卡号:")
        # 验证卡号是否存在
        user = self.allUser.get(cardNum)
        if not user:
            print("该卡号不存在！查询失败……")
            return -1
        # 验证密码
        if not self.validPwd(user.card.cardPasswd):
            print("密码输入错误！查询失败……")
            user.card.cardLock = True
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定,请解锁后再执行其它操作")
            return -1

        print("账号：%s 余额：%d" % (user.card.cardId, user.card.cardMoney))

    # 取款
    def getMoney(self):
        cardNum = input("请输入您的卡号:")
        # 验证卡号是否存在
        user = self.allUser.get(cardNum)
        if not user:
            print("该卡号不存在！查询失败……")
            return -1

        # 验证密码
        if not self.validPwd(user.card.cardPasswd):
            print("密码输入错误！查询失败……")
            user.card.cardLock = True
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定,请解锁后再执行其它操作")
            return -1

        # 开始取款
        money = int(input("请输入取款金额："))
        if money <= 0:
            print("输入错误,取款失败！")
            return -1

        if money > user.card.cardMoney:
            print("余额不足，取款失败！")
            return -1

        user.card.cardMoney -= money
        print("取款成功，余额=%d" % (user.card.cardMoney))


    # 存款
    def saveMoney(self):
        pass

    # 转账
    def moveMoney(self):
        pass

    # 改密
    def changePwd(self):
        pass

    # 锁定
    def lockUser(self):
        cardNum = input("请输入您的卡号:")
        # 验证卡号是否存在
        user = self.allUser.get(cardNum)
        if not user:
            print("该卡号不存在, 锁定失败")
            return -1

        if user.card.cardLock:
            print("该卡号已锁定")
            return -1

        # 验证密码
        if not self.validPwd(user.card.cardPasswd):
            print("密码输入错误！锁定失败……")
            return -1

        # 验证身份证号
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证号输入错误！锁定失败")
            return -1

        # 锁定
        user.card.cardLock = True
        print("锁定成功")

    # 解锁
    def unlockUser(self):
        cardNum = input("请输入您的卡号:")
        # 验证卡号是否存在
        user = self.allUser.get(cardNum)
        if not user:
            print("该卡号不存在, 解锁失败")
            return -1

        if not user.card.cardLock:
            print("该卡号未锁定，无需解锁")
            return -1

        # 验证密码
        if not self.validPwd(user.card.cardPasswd):
            print("密码输入错误！解锁失败……")
            return -1

        # 验证身份证号
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证号输入错误！解锁失败")
            return -1

        # 锁定
        user.card.cardLock = False
        print("解锁成功")

    # 办卡
    def newCard(self):
        pass

    # 销户
    def logoutUser(self):
        pass

    # 验证密码
    def validPwd(self, onePasswd):
        for i in range(3):
            tempPasswd = input("请输入密码：")
            if tempPasswd == onePasswd:
                return True
        return False

    # 生成卡号
    def generalCardNum(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch

            # 判断重复
            if not self.allUser.get(str):
                return str

