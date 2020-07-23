from django.db import models


class User(models.Model):
    SEX_CHOICE = (
        ('male', '男'),
        ('female', '女')
    )

    LOCATIONS = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('成都', '成都'),
        ('深圳', '深圳'),
    )

    # __tablename__ = 'user'
    # id = models.SmallIntegerField('主键', primary_key=True)
    nickname = models.CharField('昵称', db_index=True, max_length=32, default='jack')
    phonenum = models.CharField('手机', unique=True, max_length=11)
    birthday = models.DateField('生日', default='2000-01-1')
    gender = models.CharField('性别', max_length=10, default='male')
    avatar = models.CharField('个人头像', max_length=256, default='')
    location = models.CharField('常居地', choices=LOCATIONS, max_length=32, default='北京')

    def to_dict(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'phonenum': self.phonenum,
            'birthday': self.birthday,
            'gender': self.gender,
            'avatar': self.avatar,
            'location': self.location
        }

    @property
    def userprofile(self):
        if not hasattr(self, '_user'):
            self._userprofile = UserProfile.objects.get(uid=self.id)
            return self._userprofile


class UserProfile(models.Model):
    SEX_CHOICE = (
        ('male', '男'),
        ('female', '女')
    )
    uid = models.SmallIntegerField('关联User键', unique=True)
    dating_gender = models.CharField('匹配的性别', max_length=6, default='female')
    dating_location = models.CharField('目标城市', max_length=16, default='北京')
    max_distance = models.FloatField('最大查找范围', default='10')
    min_distance = models.FloatField('最小查找范围', default='1')
    max_dating_age = models.SmallIntegerField('最大交友年龄', default='80')
    min_dating_age = models.SmallIntegerField('最小交友年龄', default='20')
    vibration = models.BooleanField('开启震动', default=False)
    only_matched = models.BooleanField('不让未匹配的人看我的相册', default=False)
    auto_play = models.BooleanField('自动播放视频', default=False)

    def to_dict(self):
        return {
            'uid': self.uid,
            'dating_gender': self.dating_gender,
            'dating_location': self.dating_location,
            'max_distance': self.max_distance,
            'min_distance': self.min_distance,
            'max_dating_age': self.max_dating_age,
            'min_dating_age': self.min_dating_age,
            'vibration': self.vibration,
            'only_matched': self.only_matched,
            'auto_play': self.auto_play,
        }

