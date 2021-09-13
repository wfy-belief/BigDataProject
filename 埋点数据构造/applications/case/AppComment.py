#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:AppComment.py
#  Date:9/13/21, 2:12 PM
#  Author:wfy
class AppComment(object):
    def __init__(self):
        # 评论表
        self.comment_id = None
        # 用户 id
        self.user_id = None
        # 父级评论 id(为 0 则是一级评论,不为 0 则是回复)
        self.p_comment_id = None
        # 评论内容
        self.content = None
        # 创建时间
        # fixme 👇 这难道是实习生命名的字段名
        self.addtime = None
        # todo 待添加更新日期（最后一次修改日期）
        # 评论的相关 id
        self.other_id = None
        # 点赞数量
        self.praise_count = None
        # 回复数量
        self.reply_count = None
        # todo 评论过滤 is_show 可以不展示该评论
        # todo ......？
