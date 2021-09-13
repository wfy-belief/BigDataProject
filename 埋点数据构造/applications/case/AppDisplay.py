#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:AppDisplay.py
#  Date:9/13/21, 1:46 PM
#  Author:wfy
class AppDisplay(object):
    """
    商品曝光
    """

    def __init__(self):
        # 动作：曝光商品=1，点击商品=2
        self.action = None
        # 商品 ID（服务端下发的 ID）
        self.good_id = None
        # 顺序（第几条商品，第一条为 0，第二条为 1，如此类推）
        self.place = None
        # 分类 ID（服务端定义的分类 ID）
        self.category = None
        # 曝光类型：1 - 首次曝光 2-重复曝光
        self.type = None

    def __str__(self):
        return self.__dict__
