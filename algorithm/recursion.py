'''
递归调用：一个函数，调用了自身，称为递归调用

方式：
1、写出临界条件
2、找出这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果

'''

import os

# 输入一个数（大于等于1），求1+2+3+……+n的和
def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n - 1)

res = sum2(5)
print(res)


# 递归遍历目录
def getAllDir(path, sp = ""):
    fileList = os.listdir(path)
    sp += " "
    for fileName in fileList:
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "目录:", fileAbsPath)
            getAllDir(fileAbsPath, sp)
        else:
            print("文件:", fileName)

#getAllDir('/opt')

# 栈模拟递归遍历
def getAllDirStack(path):
    stack = []
    # 数据压入栈
    stack.append(path)
    # 当栈为空的时候，停止循环
    while len(stack) > 0:
        # 从栈里取数据
        dirPath = stack.pop()
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                print("目录:", fileAbsPath)
                # 发现是目录，压入栈
                stack.append(fileAbsPath)
            else:
                print("文件:", fileName)

getAllDirStack('/opt')