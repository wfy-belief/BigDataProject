#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:AppPublic.py
#  Date:9/13/21, 3:09 PM
#  Author:wfy
class AppPublic(object):
    def __init__(self):
        #  设备唯一标识
        self.mid = None
        # 用户 user id
        self.user_id = None
        # 版本号
        self.version_code = None
        # 版本名字
        self.version_name = None
        # 系统语言
        self.language = None
        # 渠道号
        self.sr = None
        # Android 系统版本
        self.os = None
        # 区域
        self.ar = None
        # 手机型号
        self.md = None
        # 手机品牌
        self.ba = None
        # sdkVersion
        self.sv = None
        # gmail
        self.g = None
        # height X width，屏幕宽高
        self.hw = None
        # 客户端日志产生时的时间
        self.t = None
        # 网络模式
        self.nw = None
        # 经纬度
        self.ln = None
        self.la = None
        # ip 地址
        self.ip = None

    def __str__(self):
        return self.__dict__
