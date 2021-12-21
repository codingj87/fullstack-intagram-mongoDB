import graphene
from instagram.schema import Query as instagramQuery


class Query(
    instagramQuery,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query)