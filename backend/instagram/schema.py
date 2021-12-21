import graphene
from instagram.Account.schema import Query as accountQuery

class Query(accountQuery, graphene.ObjectType):
    pass


