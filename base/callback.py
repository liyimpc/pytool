'''
回调函数
'''
from lib.csv.dealFile import DealFile

d = DealFile()

def func(str):
    print(str + "!")

path = "/opt/1.csv"
d.readCsv(path, func)