from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from api.serializers import UserSerializer,GroupSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            返回用户实例。

        list:
            返回最近加入的所有用户。

        create:
            创建一个新用户。

        delete:
            删除现有用户

        partial_update:
            更新现有用户的一个或多个字段。

        update:
            更新用户。


    """
    #django指定查询User视图的表语句
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
            retrieve:
                返回一个组实例。

            list:
                返回最近加入的所有团体。

            create:
                返回最近加入的所有团体。

            delete:
                删除现有组

            partial_update:
                更新现有组中的一个或多个字段。

            update:
                更新组。
        """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer