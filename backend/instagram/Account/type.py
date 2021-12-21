import graphene
from graphene_django import DjangoObjectType
from instagram.models import User

class UserType(DjangoObjectType):

    class Meta:
        model = User
        fields = ('id', 'name')


class UserListType(graphene.ObjectType):
    result = graphene.Boolean()
    objects = graphene.List(UserType)