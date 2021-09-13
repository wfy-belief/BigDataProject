#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:ProductDetails.py
#  Date:9/13/21, 8:24 PM
#  Author:wfy
import random
import time

from .case import AppProductDetails


def product_details_builder():
    product_details = AppProductDetails()

    product_details.entry = random.randint(1, 3)
    # 动作：开始加载=1，加载成功=2（pv），加载失败=3, 退出页面=4
    product_details.action = random.randint(1, 4)
    # 商品 ID（服务端下发的 ID）
    product_details.good_id = random.randint(1, 1000)
    # 商品样式：0、无图、1、一张大图、2、两张图、3、三张小图、4、一张小图、5、
    # 一张大图两张小图
    product_details.show_style = random.randint(0, 5)
    #  页面停留时长：从商品开始加载时开始计算，到用户关闭页面所用的时间。若中途
    #  用跳转到其它页面了，则暂停计时，待回到详情页时恢复计时。或中途划出的时间
    #  超过 10 分钟，则本次计时作废，不上报本次数据。如未加载成功退出，则报空。
    product_details.page_stay_time = random.randint(0, 20)
    # 加载时长：计算页面开始加载到接口返回数据的时间 （开始加载报 0，加载成功或加载失败才上报时间）
    # fixme 如何定义加载失败的时长
    product_details.loading_time = random.randint(1, 1000 * 2)
    # 加载失败码：把加载失败状态码报回来（报空为加载成功，没有失败）
    # self.type1 = None
    # todo 加载状态码 修复命令 如何规定？
    product_details.status_code = random.choice(["404", "200", "201", "325", "102"])
    # 分类 ID（服务端定义的分类 ID）
    # fixme 需要修复 category 表示 id 是否单词命名具有歧义了？
    product_details.category = random.randint(1, 100)
    data = {
        'ett': int(time.time() * 1000),
        'en': 'product_details',
        'kv': product_details.__str__()
    }
    return data
