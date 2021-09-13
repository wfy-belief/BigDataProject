#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:AppError.py
#  Date:9/13/21, 2:45 PM
#  Author:wfy
class AppError(object):
    def __init__(self):
        # 错误摘要
        self.errorBrief = None
        # 错误详情
        self.errorDetails = None
