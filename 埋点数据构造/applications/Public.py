#  Copyright(c)2021-2021, A citrus.cn by wfy
#  项目名称:SanicProject
#  文件名称:Public.py
#  Date:9/13/21, 3:08 PM
#  Author:wfy
import random
import time
import uuid
from faker import Faker

from .case import AppPublic


def public_builder():
    public = AppPublic()
    # 设备 id
    public.mid = uuid.uuid4().hex
    # 用户 id
    public.user_id = random.randint(0, 10000)
    # 程序版本号
    public.version_code = random.randint(0, 20)
    # 版本名
    public.version_name = f'V1.{random.randint(1, 5)}.{random.randint(0, 9)}'
    # 安卓系统版本
    public.os = f'V{random.randint(8, 12)}.{random.randint(0, 9)}'
    # 语言
    public.language = random.choice(["en", 'zh'])
    # 渠道号，从那个渠道来的
    public.sr = random.randint(0, 5)
    # 区域 粒度为 省级
    fake = Faker(locale='zh_CN')
    public.ar = fake.province()
    # 手机品牌
    public.ba = random.choice(["huawei", "xiaomi", "apple"])
    # 手机型号
    public.md = public.ba + f"{random.randint(0, 20)}"
    # 嵌入sdk的版本
    public.sv = f"V2.{random.randint(0, 10)}.{random.randint(0, 10)}"
    # gmail
    public.g = fake.email()
    # 屏幕宽高 hw
    public.hw = random.choice(["640*960", "640*1136", "750*1134", "1080*1920"])
    # 客户端产生日志时间
    public.t = time.time()
    # 手机网络模式 3G,4G,5G,WIFI
    public.nw = random.choice(["3G", "4G", "5G", "WIFI"])
    # ip 地址
    public.ip = fake.ipv4()

    return public.__str__()
