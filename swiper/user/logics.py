import re
import random

from django.core.cache import cache

# from libs.sms import send_sms
from common import keys

P_PHONENUM = re.compile(r'^1[3456789]\d{9}$')


def is_phonenum(phonenum):
    ''' 正则检查手机号合法性 '''
    return True if P_PHONENUM.match(phonenum) else False


def gen_randcode():
    ''' 生成验证码'''
    chars = random.choices('0123456789', k=4)
    return ''.join(chars)


def send_vcode(phonenum):
    '''发送验证码'''
    key = keys.VCODE_K % phonenum
    if cache.get(key):
        return True

    vcode = gen_randcode()
    print(vcode)
    if vcode:
        cache.set(key, vcode, 500)
        return True
    else:
        return False