import random
import time

from applications import public_builder
from applications import display_builder
from applications import product_details_builder
from applications import loading_builder
from applications import shopping_cart_builder
from applications import ad_builder
from applications import start_builder
from applications import notification_builder

if __name__ == '__main__':
    # # 公共字段
    # print(public_builder())
    # # 商品展示事件
    # print(display_builder())
    # # 商品详情页
    # print(product_details_builder())
    # # 商品列表
    # print(loading_builder())
    # # 购物车
    # print(shopping_cart_builder())
    # # 广告相关字段
    # print(ad_builder())
    # # 启动日志
    # print(start_builder())
    # # 消息通知
    # print(notification_builder())
    # # 错误日志数据

    # 为各个事件类型的公共字段（时间、事件类型、Json数据）拼接
    for _ in range(10):
        et = (display_builder(), product_details_builder(),
              loading_builder(), shopping_cart_builder(),
              ad_builder(), start_builder(), notification_builder())
        # print(random.sample(et, random.randint(1, len(et))))

        app = {
            'app': 'app',
            'version': '0.1',
            'cm': public_builder(),
            'et': random.sample(et, random.randint(1, len(et)))
        }
        print(int(time.time() * 1000), app, sep='|')
