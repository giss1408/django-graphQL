import graphene
from graphene_django import DjangoObjectType
from .models import Category, Description, Tenant

''' CategoryType'''
class CategoryType(DjangoObjectType): 
    class Meta:
        model = Category
        fields = ('id', 'title')

class UpdateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to update category
        title = graphene.String( required=True)
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate( cls, root, info, title, id):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()

        return UpdateCategory(category=category)

class CreateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        title = graphene.String(required=True)

    # Class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category()
        category.title = title
        category.save()

        return CreateCategory(category=category)


''' BookType'''
class DescriptionType(DjangoObjectType):
    class Meta:
        model = Description
        fields = (
            'id',
            'title',
            'tenant',
            'country',
            'city',
            'district',
            'isbn',
            'rooms',
            'price',
            'description',
            'status',
            'date_created',
            'date_toEnter',
            'category',
            'imageurl',
            'product_tag',
            'bailleur',
            'surface_m2',
        )

class DescriptionInput(graphene.InputObjectType):
    title = graphene.String()
    country = graphene.String()
    city = graphene.String()
    district = graphene.String()
    bailleur = graphene.String()
    status = graphene.String()
    price = graphene.Int()

class CreateDescription(graphene.Mutation):
    class Arguments:
        input = DescriptionInput(required=True)

    description = graphene.Field(DescriptionType)

    @classmethod
    def mutate(cls, root, info, input):
        description = Description()
        description.title = input.title
        description.country = input.country
        description.city = input.city
        description.district = input.district
        description.bailleur = input.bailleur
        description.status = input.status
        description.price = input.price
        description.save()

        return CreateDescription(description=description)

class UpdateDescription(graphene.Mutation):
    class Arguments:
        input = DescriptionInput(required=True)
        id = graphene.ID()

    description = graphene.Field(DescriptionType)

    @classmethod
    def mutate(cls, root, info, input, id):
        description = Description.objects.get(pk=id)
        description.title = input.title
        description.bailleur = input.bailleur
        description.country = input.country
        description.city = input.city
        description.district = input.district
        description.status = input.status
        description.price = input.price
        description.save()

        return UpdateDescription(description=description)


''' GroceryType'''
class TenantType(DjangoObjectType):
    class Meta:
        model = Tenant
        fiels = (
            'id',
            'nomPrenoms',
            'isbn',
            'quantity',
            'date_created',
            'status_payment',
            'expire_date',
        )

class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    descriptions = graphene.List(DescriptionType)
    tenants = graphene.List(TenantType)

    def resolve_categories( root, info, **kwargs):
        return Category.objects.all()

    def resolve_descriptions( root, info, **kwargs):
        return Description.objects.all()

    def resolve_tenants( root, info, **kwargs):
        return Tenant.objects.all()

class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    create_description = CreateDescription.Field()
    update_description = UpdateDescription.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)