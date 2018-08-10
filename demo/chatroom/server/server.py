'''
聊天室服务端
'''
import tkinter, socket, threading

# 创建主窗口
dialog = tkinter.Tk()

# 设置标题
dialog.title("tkinter")

'''
设置大小和位置
400x400 width,height
200+20  left+top
'''
dialog.geometry("400x400+200+20")

# 用户信息保存
users = {}

def run(ck, ca):
    userName = ck.recv(1024)
    userName = userName.decode("utf-8")
    users[userName] = ck
    printStr = userName + "连接\n"
    text.insert(tkinter.INSERT, printStr)

    while True:
        rData = ck.recv(1024)
        dataStr = rData.decode("utf-8")
        infoList = dataStr.split(":")
        msg = infoList[0]+": "+infoList[1]
        users[infoList[0]].send(msg.encode("utf-8"))


def start():
    ipStr = eip.get()
    portStr = eport.get()
    # 开启服务监听
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ipStr, int(portStr)))
    # 监听个数
    server.listen(10)
    printStr = "服务器启动成功\n"
    text.insert(tkinter.INSERT, printStr)
    while True:
        ck, ca = server.accept()
        t = threading.Thread(target=run, args=(ck,ca))
        t.start()

# 启动服务监听
def startServer():
    s = threading.Thread(target=start)
    s.start()


labelIp = tkinter.Label(dialog,
                      text="ip",
                      font=("黑体", 20),
                      width = 10,
                      height = 1).grid(row=0, column=0)
labelPort = tkinter.Label(dialog,
                      text="port",
                      font=("黑体", 20),
                      width = 10,
                      height = 1).grid(row=1, column=0)
# 绑定变量
eip = tkinter.Variable()
eport = tkinter.Variable()

entryIp = tkinter.Entry(dialog,
                     textvariable=eip).grid(row=0, column=1)
entryPort = tkinter.Entry(dialog,
                     textvariable=eport).grid(row=1, column=1)


button = tkinter.Button(dialog,
                        text="启动服务",
                        command=startServer,
                        width=10,
                        height=2).grid(row=2, column=1)

text = tkinter.Text(dialog,
                    width=30,
                    height=15,
                    background="pink",
                    borderwidth=1)
text.grid(row=3, column=1)

# 进入消息循环
dialog.mainloop()