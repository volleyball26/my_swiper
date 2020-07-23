from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from common import stat


# class AuthMiddleware(MiddlewareMixin):
#
#     white_ip_list = ['/',
#                     'api/user/vcode/fetch',
#                     'api/user/vcode/submit',]
#
#     black_ip_list = ['api/user/profile/show',
#                      'api/user/profile/update']
#
#     def process_requests(self, request):
#         if request.get_full_path in self.white_ip_list:
#             return
#         else:
#             uid = request.session.get['uid']
#             if uid is None:
#                 return JsonResponse({'code':stat.LOGIN_REQUIRED})
#             else:
#                 request.uid = uid
