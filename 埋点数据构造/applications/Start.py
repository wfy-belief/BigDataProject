#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:Start.py
#  Date:9/13/21, 9:01 PM
#  Author:wfy
import random
import time

from .case import AppStart


def start_builder():
    start = AppStart()
    # 入口： push=1 ， widget=2 ， icon=3 ， notification=4, lockscreen_widget =5
    start.entry = random.randint(1, 5)
    # 开屏广告类型: 开屏原生广告=1, 开屏插屏广告=2
    start.open_ad_type = random.randint(1, 2)
    # 状态：成功=1 失败=2
    start.action = random.randint(1, 2)
    # 加载时长：计算下拉开始到接口返回数据的时间，（开始加载报 0，加载成功或加载失败才上报时间）
    start.loading_time = random.randint(1, 1000 * 2)
    # 失败码（没有则上报空）
    start.detail = random.choice(["404", "200", "201", "325", "102"])
    # 失败的 message（没有则上报空）
    start.extend1 = ''
    # 日志类型 start
    start.en = ''
    data = {
        'ett': int(time.time() * 1000),
        'en': 'start',
        'kv': start.__str__()
    }
    return data
