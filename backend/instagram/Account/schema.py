import graphene
from instagram.Account.type import UserListType
from instagram.Account.query import get_user_list


class Query(graphene.ObjectType):
    get_user_list = graphene.Field( 
        UserListType,
        name=graphene.String(description='이름'),
        age=graphene.String(description='나이'),
        resolver=get_user_list,
    )