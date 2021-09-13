#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:AppShoppingCart.py
#  Date:9/13/21, 2:03 PM
#  Author:wfy
class AppShoppingCart(object):
    """
    业务数据：购物车
    """

    def __init__(self):
        # item id 商品 更改为 good id
        self.good_id = None
        # 操作类型：1 添加购物车；2 改变商品数量；3 移除商品
        self.action = None
        # 加减数量
        self.change_num = None
        # 更改前数量
        self.before_num = None
        # 更改后数量
        self.after_num = None
        # 商品单价
        self.price = None
        # todo 添加时间？
        # todo 更新时间？
        # todo ......？

    def __str__(self):
        return self.__dict__
