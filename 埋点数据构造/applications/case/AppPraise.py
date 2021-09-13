#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:AppPraise.py
#  Date:9/13/21, 2:35 PM
#  Author:wfy
class AppPraise(object):

    def __init__(self):
        # 主键 id
        self.id = None
        # 用户 id
        self.user_id = None
        # 点赞的对象 id
        self.target_id = None
        # 点赞类型 1 问答点赞 2 问答评论点赞 3 文章点赞数 4 评论点赞
        self.type = None
        # 添加时间
        # fixme
        self.add_time = None
