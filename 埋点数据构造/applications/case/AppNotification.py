#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:AppNotification.py
#  Date:9/13/21, 2:08 PM
#  Author:wfy
class AppNotification(object):
    """
    事件 消息通知
    """
    def __init__(self):
        # 动作：通知产生=1，通知弹出=2，通知点击=3，常驻通知展示（不重复上报，一天之内只报一次）=4
        self.action = None
        # 通知 id：预警通知=1，天气预报（早=2，晚=3），常驻=4
        # fixme 类型不匹配 = = 字段命令略显 敷衍
        self.type = None
        # 客户端弹出时间
        # fixme 同上 字段名含义不明显
        self.ap_time = None
        # 备用字段 = =
        # fixme 这是实习生写的代码吧
        self.content = None

    def __str__(self):
        return self.__dict__