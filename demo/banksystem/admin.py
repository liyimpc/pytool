import time

class Admin(object):
    admin = "1"
    passwd = "1"

    def printAdminView(self):
        print("**********************************************************************************")
        print("*                                                                                *")
        print("*                                                                                *")
        print("*                               欢迎登陆鸣人银行                                   *")
        print("*                                                                                *")
        print("*                                                                                *")
        print("**********************************************************************************")


    def sysFunctionView(self):
        print("**********************************************************************************")
        print("*            开户(1)                        查询(2)                       *")
        print("*            取款(3)                        存款(4)                       *")
        print("*            转账(5)                        改密(6)                       *")
        print("*            锁定(7)                        解锁(8)                       *")
        print("*            补卡(9)                        销户(0)                       *")
        print("*                           退出(t)                                       *")
        print("*                                                                        *")
        print("**************************************************************************")

    def adminLogin(self):
        inputAdmin = input("请输入管理员账号：")
        if self.admin != inputAdmin:
            print("输入账号有误")
            return -1
        inputPasswd = input("请输入管理员密码:")
        if self.passwd != inputPasswd:
            print("输入密码有误")
            return -1

        # 能执行到这里说明账号密码正确
        print("操作成功!请稍后……")
        time.sleep(2)
        return 0

    def adminQuit(self):
        code = self.adminLogin()