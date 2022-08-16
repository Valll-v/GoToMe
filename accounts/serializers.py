from .models import UserProfile
from djoser.serializers import *


User = get_user_model()


class UserAuthSerializer(UserCreateSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'password', 'email', 'gender', 'birthday', 'name', 'age', 'country', 'city',
                  'description')


class UserProfileSerializer(UserSerializer):
    class Meta:
        model = UserProfile
        fields = ('photo', 'username', 'registration_date', 'name', 'age', 'birthday', 'country', 'city', 'description')



