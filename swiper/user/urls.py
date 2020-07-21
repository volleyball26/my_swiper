from django.conf.urls import url

from user import apis

urlpatterns = [
    url('vcode/fetch', apis.fetch)
]