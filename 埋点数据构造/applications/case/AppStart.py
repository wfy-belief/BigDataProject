#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:AppStart.py
#  Date:9/13/21, 2:47 PM
#  Author:wfy
class AppStart(object):
    def __init__(self):
        # 入口： push=1 ， widget=2 ， icon=3 ， notification=4, lockscreen_widget =5
        self.entry = None
        # 开屏广告类型: 开屏原生广告=1, 开屏插屏广告=2
        self.open_ad_type = None
        # 状态：成功=1 失败=2
        self.action = None
        # 加载时长：计算下拉开始到接口返回数据的时间，（开始加载报 0，加载成功或加载失败才上报时间）
        self.loading_time = None
        # 失败码（没有则上报空）
        self.detail = None
        # 失败的 message（没有则上报空）
        self.extend1 = None
        # 日志类型 start
        self.en = None

    def __str__(self):
        return self.__dict__
