
'''
__name__属性：
模块就是一个可执行的py文件，一个模块被另一个程序引用。我不想让模块中的某些代码执行，可以使用__name__属性来使程序仅调用模块中的一部分
每一个模块都有一个__name__属性。
'''

def func(num, dev):
    assert (dev!=0), "div不能为0"
    return num / dev

if __name__ == '__main__':
    print("这是主程序")
else:
    func(10.0)
