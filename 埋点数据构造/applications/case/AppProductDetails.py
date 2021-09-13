#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:AppProductDetails.py
#  Date:9/13/21, 1:52 PM
#  Author:wfy
class AppProductDetails(object):
    """
    商品详情信息
    """

    def __init__(self):
        # fixme 页面入口来源：应用首页=1、push=2、详情页相关推荐=3
        # fixme 是否使用refer更加合适？
        self.entry = None
        # 动作：开始加载=1，加载成功=2（pv），加载失败=3, 退出页面=4
        self.action = None
        # 商品 ID（服务端下发的 ID）
        self.good_id = None
        # 商品样式：0、无图、1、一张大图、2、两张图、3、三张小图、4、一张小图、5、
        # 一张大图两张小图
        self.show_style = None
        #  页面停留时长：从商品开始加载时开始计算，到用户关闭页面所用的时间。若中途
        #  用跳转到其它页面了，则暂停计时，待回到详情页时恢复计时。或中途划出的时间
        #  超过 10 分钟，则本次计时作废，不上报本次数据。如未加载成功退出，则报空。
        self.page_stay_time = None
        # 加载时长：计算页面开始加载到接口返回数据的时间 （开始加载报 0，加载成功或加载失败才上报时间）
        # fixme 如何定义加载失败的时长
        self.loading_time = None
        # 加载失败码：把加载失败状态码报回来（报空为加载成功，没有失败）
        # self.type1 = None
        # todo 加载状态码 修复命令 如何规定？
        self.status_code = None
        # 分类 ID（服务端定义的分类 ID）
        # fixme 需要修复 category 表示 id 是否单词命名具有歧义了？
        self.category = None

    def __str__(self):
        return self.__dict__
