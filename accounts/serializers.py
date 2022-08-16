from .models import UserProfile
from djoser.serializers import *


User = get_user_model()


class UserAuthSerializer(UserCreateSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSerializer(UserSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'age', 'country', 'city', 'description')
