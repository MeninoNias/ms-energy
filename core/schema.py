import graphene
import supplier.schema


class Query(supplier.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
