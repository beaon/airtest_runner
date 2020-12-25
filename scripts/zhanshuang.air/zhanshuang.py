# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)


# 打开并进入游戏
start_app("com.kurogame.haru.hero")
sleep(20)    # 初始化游戏，计时发现需要15秒
while not exists(Template(r"tpl1608792787978.png", record_pos=(0.23, -0.078), resolution=(2340, 1079))):
    touch((137, 510), times=2)  # 点击任意处进入游戏
    sleep()

# 测试等级显示是否正常
touch((317, 183)) # 左上角的等级
sleep()
snapshot(msg="等级是否正常显示.")

# 测试昵称修改和冷却功能
touch((2170, 92))    # 修改标志
sleep()
touch((706, 512))   # 点击输入框焦点
text("abc昵称2")
touch(Template(r"tpl1608704684902.png", record_pos=(0.176, 0.107), resolution=(2340, 1079)))
sleep()
snapshot(msg="第二次点击会提示冷却时间.")
sleep()

if exists(Template(r"tpl1608793985079.png", record_pos=(0.36, -0.183), resolution=(2340, 1079))):
    touch(Template(r"tpl1608793985079.png", record_pos=(0.36, -0.183), resolution=(2340, 1079)),times=1) # 第二次输入昵称时点确定 需要手动关闭昵称框
    
# 测试头像 
touch((1666,143)) # 点击头像
position = {
    '1': (743,366),
    '2': (947,391),
    '3': (1140,386),
    '4': (738,580),
    '5': (947,590),
    '6': (1140,575),
    '7': (733,798),
    '8': (942,778),
    '9': (1145,788)
}

i = 0
while i <= 10:
    for touxiang in position.values():
        touch(touxiang)
    swipe((1135,748),(1135,466)) # 头像滑动3个位置
    i += 1
touch(Template(r"tpl1608801909479.png", record_pos=(-0.339, 0.036), resolution=(2340, 1079)))

touch(Template(r"tpl1608801270417.png", record_pos=(0.36, -0.185), resolution=(2340, 1079)))


# 复制识别吗，然后粘贴到个性签名
touch(Template(r"tpl1608862247566.png", record_pos=(0.422, -0.119), resolution=(2340, 1079)))
sleep(2)
touch((1653,352)) # 点击个性签名
touch((781,495))
touch((238,938), duration=3)
touch(Template(r"tpl1608804105769.png", record_pos=(-0.418, 0.117), resolution=(2340, 1079)))
keyevent("KEYCODE_ENTER")
touch(Template(r"tpl1608804241271.png", record_pos=(0.182, 0.109), resolution=(2340, 1079)))


# 设定支援角色，若重复，则设定第二个
touch(Template(r"tpl1608804770426.png", record_pos=(0.417, 0.057), resolution=(2340, 1079)))
touch(Template(r"tpl1608804832427.png", record_pos=(-0.049, -0.039), resolution=(2340, 1079)))
if exists(Template(r"tpl1608805112987.png", record_pos=(-0.009, -0.013), resolution=(2340, 1079))):
    sleep(2)
    touch((343,377)) #第二个角色
    touch(Template(r"tpl1608804930684.png", record_pos=(-0.055, -0.042), resolution=(2340, 1079)))


stop_app("com.kurogame.haru.hero")
    
    

    






















# touch(Template(r"tpl1608535319951.png", record_pos=(0.408, -0.203), resolution=(2340, 1079)))

# touch(Template(r"tpl1608535350331.png", record_pos=(0.127, 0.081), resolution=(2340, 1079)))

# sleep(1.0)

# touch(Template(r"tpl1608535397844.png", record_pos=(0.119, 0.162), resolution=(2340, 1079)))

# swipe((400,800),(400,600), duration=3)
# touch(Template(r"tpl1608535594112.png", record_pos=(0.39, 0.175), resolution=(2340, 1079)),times=3)
# touch(Template(r"tpl1608535633325.png", record_pos=(0.405, 0.097), resolution=(2340, 1079)))
# touch(Template(r"tpl1608535594112.png", record_pos=(0.39, 0.175), resolution=(2340, 1079)),times=3)
# touch(Template(r"tpl1608535679286.png", record_pos=(0.335, 0.097), resolution=(2340, 1079)))
# touch(Template(r"tpl1608535696942.png", record_pos=(0.3, 0.175), resolution=(2340, 1079)))
# touch(Template(r"tpl1608535713326.png", record_pos=(0.405, 0.097), resolution=(2340, 1079)))
# swipe((400,800),(400,600), duration=9)
# touch(Template(r"tpl1608535679286.png", record_pos=(0.335, 0.097), resolution=(2340, 1079)))

# touch(Template(r"tpl1608535594112.png", record_pos=(0.39, 0.175), resolution=(2340, 1079)),times=11)
# swipe((400,800),(400,600), duration=9)
# touch(Template(r"tpl1608535966021.png", record_pos=(0.409, -0.204), resolution=(2340, 1079)))
# touch(Template(r"tpl1608535972762.png", record_pos=(0.128, 0.081), resolution=(2340, 1079)))
