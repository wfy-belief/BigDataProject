#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:AppAd.py
#  Date:9/13/21, 1:11 PM
#  Author:wfy

class AppAd(object):
    """
    广告类
    """

    def __init__(self):
        # 入口：商品列表页=1  应用首页=2 商品详情页=3
        self.entry = None
        # 动作：请求广告=1 取缓存广告=2  广告位展示=3 广告展示=4 广告点击=5
        self.action = None
        # 状态：成功=1  失败=2
        self.content = None
        # 失败码（没有则上报空）
        self.detail = None
        # 广告来源:admob=1 facebook=2  ADX（百度）=3 VK（俄罗斯）=4
        self.source = None
        # 用户行为：    主动获取广告=1    被动获取广告=2
        self.behavior = None
        # Type: 1- 图文 2-图集 3-段子 4-GIF 5-视频 6-调查 7-纯文 8-视频+图文  9-GIF+图文  0-其他
        self.news_type = None
        # 内容样式：无图(纯文字)=6 一张大图=1  三站小图+文=4 一张小图=2 一张大图两张小图+文=3 图集+文 = 5
        #     //一张大图+文=11   GIF大图+文=12  视频(大图)+文 = 13
        # 来源于详情页相关推荐的商品，上报样式都为0（因为都是左文右图）
        self.show_style = None

    def __str__(self):
        return self.__dict__
