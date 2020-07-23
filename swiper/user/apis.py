import json
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

from common import keys, stat
from user import logics

from user.models import User, UserProfile


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
            user_profile = UserProfile.objects.create(uid=user.id)
        # 记录uid 保存登录状态
        request.session['uid'] = user.id

        # print('======================')
        # print(user.userprofile.to_dict())
        # print('======================')
        return JsonResponse({'code': 0, 'data': user.to_dict()})

    else:
        return JsonResponse({'code': stat.OK,
                             'data': None})


def show_profile(request):
    """
    获取配置信息
    :param request:
    :return:
    """
    user = User.objects.get(id=request.session['uid'])

    return JsonResponse({'code':stat.OK, 'data':user.userprofile.to_dict()})


def update_profile(request):

    # user
    nickname = request.POST.get('nickname')
    # phonenum = request.POST.get('phonenum')
    birthday = request.POST.get('birthday')
    print(birthday)
    gender = request.POST.get('gender')
    avatar = request.POST.get('avatar')
    location = request.POST.get('location')

    # user_profile
    dating_gender = request.POST.get('dating_gender')
    dating_location = request.POST.get('dating_location')
    max_distance = request.POST.get('max_distance')
    min_distance = request.POST.get('min_distance')
    max_dating_age = request.POST.get('max_dating_age')
    min_dating_age = request.POST.get('min_dating_age')
    vibration = request.POST.get('vibration')
    only_matched = request.POST.get('only_matched')
    auto_play = request.POST.get('auto_play')

    print(request.session['uid'])
    User.objects.filter(id=request.session['uid']).update(nickname=nickname,
                                                                 birthday=birthday,
                                                                 gender=gender,
                                                                 avatar=avatar,
                                                                 location=location
                                                                )
    # print(user.userprofile.dating_gender)



    UserProfile.objects.filter(uid=request.session['uid']).update(dating_gender=dating_gender,
                                                                       dating_location=dating_location,
                                                                       max_distance=max_distance,
                                                                       min_distance=min_distance,
                                                                       max_dating_age=max_dating_age,
                                                                       min_dating_age=min_dating_age,
                                                                       vibration=vibration,
                                                                       only_matched=only_matched,
                                                                       auto_play=auto_play
                                                                        )
    # json.load(request.body)
    # print(data['nickname'])
    # User.objects.update()
    return JsonResponse({'code':stat.OK,'data':None})