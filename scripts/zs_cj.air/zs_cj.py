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

# 点击进入成就界面
touch((317, 183)) # 左上角的等级
touch(Template(r"tpl1608865072815.png", record_pos=(-0.366, -0.01), resolution=(2340, 1079)))

cj_list = [Template(r"tpl1608865104744.png", record_pos=(-0.218, -0.159), resolution=(2340, 1079)),Template(r"tpl1608865118506.png", record_pos=(-0.09, -0.158), resolution=(2340, 1079)),Template(r"tpl1608865127686.png", record_pos=(0.031, -0.158), resolution=(2340, 1079)),Template(r"tpl1608865139127.png", record_pos=(0.154, -0.16), resolution=(2340, 1079))]

for temp in cj_list:
    touch(temp)
    for _ in range(5):
        swipe((1666,838),(1666,451))
        
# c测试展示功能
touch(Template(r"tpl1608868083949.png", record_pos=(-0.365, 0.05), resolution=(2340, 1079)))

touch((1792,195)) # 取消全角色 展示
touch(Template(r"tpl1608867809886.png", record_pos=(0.036, -0.072), resolution=(2340, 1079)))
touch(Template(r"tpl1608867816512.png", record_pos=(0.316, 0.083), resolution=(2340, 1079)))

touch(Template(r"tpl1608867719637.png", record_pos=(-0.194, 0.207), resolution=(2340, 1079)))
touch(Template(r"tpl1608867732383.png", record_pos=(-0.261, 0.033), resolution=(2340, 1079)))
touch(Template(r"tpl1608867737525.png", record_pos=(-0.262, 0.078), resolution=(2340, 1079)))
touch(Template(r"tpl1608867742211.png", record_pos=(-0.258, 0.123), resolution=(2340, 1079)))
touch(Template(r"tpl1608867748415.png", record_pos=(0.362, -0.184), resolution=(2340, 1079)))

touch((1792,195)) # 选中全角色展示

touch(Template(r"tpl1608867997143.png", record_pos=(0.016, -0.073), resolution=(2340, 1079)))
touch(Template(r"tpl1608868003215.png", record_pos=(0.147, -0.034), resolution=(2340, 1079)))
touch(Template(r"tpl1608868010574.png", record_pos=(0.276, 0.205), resolution=(2340, 1079)))
sleep(2)

# 收藏
touch(Template(r"tpl1608868137852.png", record_pos=(-0.368, 0.109), resolution=(2340, 1079)))

touch(Template(r"tpl1608868157287.png", record_pos=(-0.285, -0.205), resolution=(2340, 1079)))

stop_app("com.kurogame.haru.hero")
    
    