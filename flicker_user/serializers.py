from rest_framework import serializers
from flicker_user.models import FlickerUser
import code


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # code.interact(local=dict(globals(), **locals()))
        user = FlickerUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = FlickerUser
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlickerUser
        fields = ('id', 'username', 'email', 'password')