import graphene
from graphene_django import DjangoObjectType
from .models import Category, Description, Tenant

# Category Type
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'title')

class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id, title):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()
        return UpdateCategory(category=category)

class CreateCategory(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category.objects.create(title=title)
        return CreateCategory(category=category)

# Description Type
class DescriptionType(DjangoObjectType):
    class Meta:
        model = Description
        fields = (
            'id', 'title', 'tenant', 'country', 'city', 'district', 'isbn',
            'rooms', 'price', 'description', 'status', 'date_created',
            'date_toEnter', 'category', 'imageurl', 'product_tag', 'bailleur', 'thumbnail', 'image_1', 'image_2', 'image_3', 'image_4', 'main_image',
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
        description = Description.objects.create(
            title=input.title,
            country=input.country,
            city=input.city,
            district=input.district,
            bailleur=input.bailleur,
            status=input.status,
            price=input.price,
        )
        return CreateDescription(description=description)

class UpdateDescription(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = DescriptionInput(required=True)

    description = graphene.Field(DescriptionType)

    @classmethod
    def mutate(cls, root, info, id, input):
        description = Description.objects.get(pk=id)
        for field in ['title', 'bailleur', 'country', 'city', 'district', 'status', 'price']:
            setattr(description, field, getattr(input, field, getattr(description, field)))
        description.save()
        return UpdateDescription(description=description)

# Tenant Type
class TenantType(DjangoObjectType):
    class Meta:
        model = Tenant
        fields = (
            'id', 'nomPrenoms', 'isbn', 'quantity',
            'date_created', 'status_payment', 'expire_date',
        )

class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    descriptions = graphene.List(DescriptionType)
    tenants = graphene.List(TenantType)

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_descriptions(self, info, **kwargs):
        return Description.objects.all()

    def resolve_tenants(self, info, **kwargs):
        return Tenant.objects.all()

class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    create_description = CreateDescription.Field()
    update_description = UpdateDescription.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
