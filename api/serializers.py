from django.contrib.auth.models import User,Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''
    定义User表格里的相关字段
    '''
    class Meta:
        '''
        指向user表格，定义表格字段，关联group
        '''
        model=User
        fields=('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=('url','name')