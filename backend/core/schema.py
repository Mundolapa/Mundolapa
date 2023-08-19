import graphene
import faq.schema


class Query(faq.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
