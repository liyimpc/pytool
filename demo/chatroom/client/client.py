'''
聊天室客户端
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
dialog.geometry("400x700+200+20")

ck = None

# 接收数据
def recvMsg():
    while True:
        data = ck.recv(1024)
        data = data.decode("utf-8")
        text.insert(tkinter.INSERT, data+"\n")


def start():
    global ck
    ipStr = eip.get()
    portStr = eport.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipStr, int(portStr)))
    userStr = euser.get()
    # 发送用户名
    client.send(userStr.encode("utf-8"))
    # 全局设置client
    ck = client
    # 等待接收数据
    t = threading.Thread(target=recvMsg)
    t.start()

# 连接服务
def connectServer():
    s = threading.Thread(target=start)
    s.start()

def sendMsg():
    friend = efriend.get()
    sendStr = esend.get()
    sendStr = friend + ":" + sendStr
    # 发送内容本地显示
    text.insert(tkinter.INSERT, sendStr+"\n")
    # 发送消息
    ck.send(sendStr.encode("UTF-8"))


labelUser = tkinter.Label(dialog,
                      text="用户名",
                      font=("黑体", 20),
                      width = 10,
                      height = 1).grid(row=0, column=0)

labelIp = tkinter.Label(dialog,
                      text="ip",
                      font=("黑体", 20),
                      width = 10,
                      height = 1).grid(row=1, column=0)
labelPort = tkinter.Label(dialog,
                      text="port",
                      font=("黑体", 20),
                      width = 10,
                      height = 1).grid(row=2, column=0)

# 绑定变量
euser = tkinter.Variable()
eip = tkinter.Variable()
eport = tkinter.Variable()

entryUser = tkinter.Entry(dialog,
                     textvariable=euser).grid(row=0, column=1)
entryIp = tkinter.Entry(dialog,
                     textvariable=eip).grid(row=1, column=1)
entryPort = tkinter.Entry(dialog,
                     textvariable=eport).grid(row=2, column=1)


button = tkinter.Button(dialog,
                        text="连接",
                        command=connectServer,
                        width=10,
                        height=2).grid(row=3, column=1)

text = tkinter.Text(dialog,
                    width=30,
                    height=25,
                    background="pink",
                    borderwidth=1)
text.grid(row=4, column=1)

labelSend = tkinter.Label(dialog,
                      text="发送内容",
                      font=("黑体", 20),
                      width = 10,
                      height = 1).grid(row=5, column=0)

labelFriend = tkinter.Label(dialog,
                      text="好友",
                      font=("黑体", 20),
                      width = 10,
                      height = 1).grid(row=6, column=0)

esend = tkinter.Variable()
entrySend = tkinter.Entry(dialog,
                     textvariable=esend).grid(row=5, column=1)

efriend = tkinter.Variable()
entryFriend = tkinter.Entry(dialog,
                     textvariable=efriend).grid(row=6, column=1)

buttonSend = tkinter.Button(dialog,
                        text="发送",
                        command=sendMsg,
                        width=10,
                        height=2).grid(row=7, column=1)

# 进入消息循环
dialog.mainloop()