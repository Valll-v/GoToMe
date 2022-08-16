from accounts import utils
from accounts.models import UserProfile


def get_user(**kwargs) -> UserProfile:
    return UserProfile.objects.filter(
        **kwargs
    ).first()


def set_code(code: str, user: UserProfile):
    user.code = utils.encode(code)
    user.save()
