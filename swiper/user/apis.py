import json
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

from common import keys
from user import logics
from user.models import User


def fetch_vcode(request):
    phonenum = request.GET.get('phonenum').strip()
    print(phonenum)
    if logics.is_phonenum(phonenum):
        if logics.send_vcode(phonenum):
            return JsonResponse({"code": 0, "data": None})
    return JsonResponse({"code": 10555, "data": None})


def submit_vcode(request):
    """
    提交vcode， 登陆 | 注册
    :param request:
    :return:
    """
    # data = json.loads(request.data)
    # phonenum = data['phonenum']
    # vcode = data['vcode']
    phonenum = request.POST.get('phonenum', '').strip()
    vcode = request.POST.get('vcode', '').strip()

    key = keys.VCODE_K % phonenum
    cached_vcode = cache.get(key)

    # 检查vcode
    if vcode and vcode == cached_vcode:
        # 获取User or 创建User
        try:
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum,
                                       nickname='sunliren')
        # 记录uid 保存登录状态
        request.session['uid'] = user.id

        return JsonResponse({'code': 0, 'data': user.to_dict()})

    else:
        return JsonResponse({'code': 1001,
                             'data': None})