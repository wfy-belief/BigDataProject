#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:Loading.py
#  Date:9/13/21, 8:34 PM
#  Author:wfy
import random

from .case import AppLoading


def loading_builder():
    loading = AppLoading()
    # 动作：开始加载=1，加载成功=2，加载失败=3
    loading.action = random.randint(1, 3)
    # 加载时长：计算下拉开始到接口返回数据的时间，（开始加载报0，加载成功或加载失败才上报时间）
    loading.loading_time = random.randint(1, 1000 * 2)
    # 加载类型：1-读取缓存，2-从接口拉新数据   （加载成功才上报加载类型）
    loading.loading_way = random.randint(1, 2)
    # 加载类型：自动加载=1，用户下拽加载=2，底部加载=3（底部条触发点击底部提示条/点击返回顶部加载）
    loading.type = random.randint(1, 3)
    # type1 加载失败码：把加载失败状态码报回来（报空为加载成功，没有失败）
    # fixme 优化 商品列表加载的状态码
    loading.status_code = random.choice(["404", "200", "201", "325", "102"])
    loading.extend1 = ''
    loading.extend2 = ''
    # todo 重传次数
    # todo 加载的数据条数
    return loading.__str__()
