#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:ShoppingCart.py
#  Date:9/13/21, 8:40 PM
#  Author:wfy
import random
import time

from .case import AppShoppingCart


def shopping_cart_builder():
    shopping_cart = AppShoppingCart()
    # item id 商品 更改为 good id
    shopping_cart.good_id = random.randint(1, 1000)
    # 操作类型：1 添加购物车；2 改变商品数量；3 移除商品
    shopping_cart.action = random.randint(1, 3)
    # 加减数量
    shopping_cart.change_num = random.randint(1, 3)
    # 更改前数量
    shopping_cart.before_num = random.randint(1, 3)
    # 更改后数量
    shopping_cart.after_num = random.randint(1, 3)
    # 商品单价
    shopping_cart.price = random.randint(0, 1000)
    data = {
        'ett': int(time.time() * 1000),
        'en': 'shopping_cart',
        'kv': shopping_cart.__str__()
    }
    return data
