'''
assert:断言

作用：
1、错误提醒，方便定位问题
'''

def func(num, dev):
    assert (dev!=0), "div不能为0"
    return num / dev

func(10, 0)