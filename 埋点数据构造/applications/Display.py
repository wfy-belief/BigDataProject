#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:Display.py
#  Date:9/13/21, 7:53 PM
#  Author:wfy
import random
import time

from .case import AppDisplay


def display_builder():
    display = AppDisplay()
    # 动作：曝光商品=1，点击商品=2
    display.action = random.randint(1, 2)
    # 商品 ID（服务端下发的 ID）
    display.good_id = random.randint(1, 1000)
    # 顺序（第几条商品，第一条为 0，第二条为 1，如此类推）
    display.place = random.randint(1, 6)
    # 分类 ID（服务端定义的分类 ID）
    display.category = random.randint(1, 100)
    # 曝光类型：1 - 首次曝光 2-重复曝光
    display.type = random.randint(1, 2)

    data = {
        'ett': int(time.time() * 1000),
        'en': 'display',
        'kv': display.__str__()
    }
    return data
