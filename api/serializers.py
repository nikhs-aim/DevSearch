# serializers are used to convert python objects into json objects


from rest_framework import serializers
from projects.models import Project,Tag
from projects.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'


class ProjectSerializer(serializers.ModelSerializer):
    owner=ProfileSerializer(many=False)
    tags=TagSerializer(many=True)
    class Meta:
        model=Project
        fields='__all__'
