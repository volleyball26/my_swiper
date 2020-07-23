from django import forms

from user.models import User, UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['nickname', 'birthday', 'gender', 'location']

        '''update `User` set filed=filed where id=user_id'''


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = ['dating_gender',
                  'dating_location',
                  'max_distance',
                  'min_distance',
                  'max_dating_age',
                  'min_dating_age',
                  'vibration',
                  'only_matched',
                  'auto_play', ]
