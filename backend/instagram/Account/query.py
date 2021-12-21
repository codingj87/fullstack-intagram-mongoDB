from instagram.models import User
from instagram.Account.type import UserListType


def get_user_list(parnet, info, **kwargs):

    result = 'success'
    objects = User.objects.all()

    return UserListType(result=result, objects=objects)

