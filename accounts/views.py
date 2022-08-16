from django.contrib.auth.tokens import default_token_generator
from django.http import JsonResponse
from djoser.conf import settings
from djoser.utils import encode_uid
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
import accounts.db_communication as db
from accounts import utils


class CustomUserViewSet(UserViewSet):

    def get_permissions(self):
        if self.action == "check_code":
            self.permission_classes = settings.PERMISSIONS.check_code
        if self.action == "change_photo":
            self.permission_classes = settings.PERMISSIONS.change_photo
        return super().get_permissions()

    @action(["post"], detail=False)
    def check_code(self, request, *args, **kwargs):
        data = request.data
        try:
            user = db.get_user(email=data["email"])
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Please, enter email for validate your code?")
        if user.code == '0':
            return Response(status=status.HTTP_400_BAD_REQUEST, data="You can't sending code now")
        try:
            code = utils.encode(data["code"])
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Please, enter code?")
        if code == user.code:
            user.code = "0"
            user.counts_of_type = 0
            user.save()
            return JsonResponse(
                {
                    "uid": encode_uid(user.pk),
                    "token": default_token_generator.make_token(user)
                }
            )
        else:
            user.counts_of_type += 1
            if user.counts_of_type == 3:
                user.code = "0"
                user.counts_of_type = 0
                user.save()
                return Response(status=status.HTTP_400_BAD_REQUEST, data="Try to send another code,"
                                                                         " that was the last try for you")
            user.save()
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Wrong code")

    @action(["put"], detail=False)
    def change_photo(self, request, *args, **kwargs):
        user = self.get_instance()
        user.photo = request.FILES["photo"]
        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data)