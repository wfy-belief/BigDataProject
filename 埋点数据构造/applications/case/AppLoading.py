#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:AppLoading.py
#  Date:9/13/21, 1:19 PM
#  Author:wfy
class AppLoading(object):
    """
    商品列表
    """

    def __init__(self):
        # 动作：开始加载=1，加载成功=2，加载失败=3
        self.action = None
        # 加载时长：计算下拉开始到接口返回数据的时间，（开始加载报0，加载成功或加载失败才上报时间）
        self.loading_time = None
        # 加载类型：1-读取缓存，2-从接口拉新数据   （加载成功才上报加载类型）
        self.loading_way = None
        # 加载类型：自动加载=1，用户下拽加载=2，底部加载=3（底部条触发点击底部提示条/点击返回顶部加载）
        self.type = None
        # type1 加载失败码：把加载失败状态码报回来（报空为加载成功，没有失败）
        # fixme 优化 商品列表加载的状态码
        self.status_code = None
        self.extend1 = None
        self.extend2 = None
        # todo 重传次数
        # todo 加载的数据条数

    def __str__(self):
        return self.__dict__
