from ..models.user                  import User
from rest_framework                 import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model       = User
        fields      = ['id', 'username', 'password', 'name', 'email']
    
    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self,obj):
        user = User.objects.get(id=obj.id)

        return {
            'username'      : user.username,
            'name'          : user.name,
            'email'         : user.email,
        }