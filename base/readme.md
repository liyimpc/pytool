# 元素类型
> list
* 有序集合
* 可变

> tuple
* 有序集合
* 不可变

> dict
* 无序集合
* key不可变，value可变

> set
* 无序集合
* 无序
* 无重复

# 鼠标事件
* <ButtonPress-n>     <Button-n>      <n>                         鼠标按钮n被按下，n为1左键，2中键，3右键
* <ButtonRelease-n>                                               鼠标按钮n被松开
* <Double-Button-n>                                               鼠标按钮n被双击
* <Triple-Button-n>                                               鼠标按钮n被三击
* <Motion>                                                        鼠标被按下，同时，鼠标发生移动
* <Bn-Motion>                                                     鼠标按钮n被按下，同时，鼠标发生移动
* <Enter>                                                         鼠标进入
* <Leave>                                                         鼠标离开
* <MouseWheel>                                                    鼠标滚轮滚动

# 键盘事件
* <Any-KeyPress>      <KeyPress>      <Key>                       任意键按下
* <KeyRelease>                                                    任意键松开
* <KeyPress-key>      <Key-key>       <key>                       特定键按下
* <KeyRelease-key>                                                特定键松开
* <Control-Shift-Alt-KeyPress-key>    <Control-Shift-Alt-key>     组合键按下（Alt，Shift，Control任选一到三个）

# 根据事件，查看按键
* event.char          可见字符，甚至中文
* event.keysym        用字符串命名了按键
* event.keycode       用按键码命名了按键，但是它不能反映事件前缀：Alt、Control、Shift、Lock，并且它不区分大小写写按键，即输入a和A是相同的键码。
* event.keysym_num    用数字代码命名了按键
* event.Key           描述了键盘上的按键名，方便一一对应