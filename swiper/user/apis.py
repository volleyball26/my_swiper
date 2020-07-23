import json
from django.core.cache import cache
from common import keys
from common import stat

from libs.http import render_json

from user import logics
from user.models import User, UserProfile
from user.forms import UserForm
from user.forms import UserProfileForm


def fetch_vcode(request):
    phonenum = request.GET.get('phonenum').strip()
    print(phonenum)
    print(request.path_info)
    if logics.is_phonenum(phonenum):
        if logics.send_vcode(phonenum):
            return render_json()
    return render_json()


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
            print(user.id)
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum,
                                       nickname='sunliren')
            user_profile = UserProfile.objects.get_or_create(id=user.id)
        # 记录uid 保存登录状态
        request.session['uid'] = user.id

        return render_json(data=user.to_dict())

    else:
        return render_json(code=stat.VOCDE_ERR)


def show_profile(request):
    """
    获取配置信息
    :param request:
    :return:
    """
    userprofile = UserProfile.objects.get(id=request.session['uid'])
    # print(userprofile.to_dict())

    return render_json(data=userprofile.to_dict())


def update_profile(request):

    # user
    userform = UserForm(data=request.POST)
    userfileform = UserProfileForm(data=request.POST)
    print(userform.is_valid(), userfileform.is_valid())
    print('form is valid')
    if userform.is_valid() and userfileform.is_valid():
        # 获取session.uid
        uid = request.session.get('uid')
        print('**userform.cleaned_data', type(userform.cleaned_data))
        print(userfileform.cleaned_data['dating_location'])
        User.objects.filter(id=uid).update(**userform.cleaned_data)
        UserProfile.objects.filter(id=uid).update(**userfileform.cleaned_data)
        # userform.change_date()
        return render_json()
    else:
        return render_json(code=stat.PROFILE_ERR)
