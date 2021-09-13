#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:Notification.py
#  Date:9/13/21, 9:05 PM
#  Author:wfy
import random
import time

from .case import AppNotification


def notification_builder():
    notification = AppNotification()
    # 动作：通知产生=1，通知弹出=2，通知点击=3，常驻通知展示（不重复上报，一天之内只报一次）=4
    notification.action = random.randint(1, 4)
    # 通知 id：预警通知=1，天气预报（早=2，晚=3），常驻=4
    # fixme 类型不匹配 = = 字段命令略显 敷衍
    notification.type = random.randint(1, 4)
    # 客户端弹出时间
    # fixme 同上 字段名含义不明显
    notification.ap_time = time.time()
    # 备用字段 = =
    # fixme 这是实习生写的代码吧
    notification.content = ''

    data = {
        'ett': int(time.time() * 1000),
        'en': 'notification',
        'kv': notification.__str__()
    }

    return data
