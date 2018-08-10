'''
人
类名：Person
属性：姓名，身份证号，电话号，卡
行为:

卡
类名：CardId
属性：卡号，密码，余额
行为：

银行
类名：Bank
属性：用户列表，提款机
行为：

提款机
类名：ATM
属性：
行为：开户，查询，取款，存储，转账，改密码，锁定，解锁，补卡，销户

管理员
类名：Admin
属性：
行为：管理员界面，管理员验证，系统功能界面
'''

from demo.banksystem.admin import Admin
import time
import pickle
import os

from demo.banksystem.atm import ATM


def main():
    # 界面对象
    admin = Admin()

    # 读取用户数据
    filePath = os.path.join(os.getcwd(), "allUser.json")
    f = open(filePath, "rb")
    #allUser = pickle.load(f)
    allUser = f.read()
    print("初始数据:", allUser)

    if allUser == '':
        allUser = {}

    # 初始化提款机
    atm = ATM(allUser)

    admin.printAdminView()

    # 管理员开机
    if admin.adminLogin():
        return -1

    while True:
        admin.sysFunctionView()
        # 等待用户操作
        option = input("请输入您的操作：")
        print(option)
        if option == "1":
            print("开户")
            atm.createUser()

        elif option == "2":
            print("查询")
            atm.searchUserInfo()

        elif option == "3":
            print("取款")


        elif option == "4":
            print("存款")


        elif option == "5":
            print("转账")


        elif option == "6":
            print("改密")


        elif option == "7":
            print("锁定")
            atm.lockUser()

        elif option == "8":
            print("解锁")
            atm.unlockUser()

        elif option == "9":
            print("补卡")


        elif option == "0":
            print("销户")


        elif option == "t":
            if not admin.adminLogin():
                # 持久化到本地文件
                filePath = os.path.join(os.getcwd(), "allUser.json")
                f = open(filePath, "wb")
                #f.write(str(atm.allUser))
                pickle.dump(atm.allUser, f)
                f.close()
                return -1

        time.sleep(2)

if __name__ == '__main__':
    main()