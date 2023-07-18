from django.contrib.auth.models import User, Group
from jobs.models import Advertisement
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AdvertisementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['title', 'desc', 'salary', 'pub_date']
