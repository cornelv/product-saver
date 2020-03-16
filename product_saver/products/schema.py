import graphene
from graphene import relay, ObjectType, Field
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation

from product_saver.products.models import Supplier, Category, Product, Image
from product_saver.products.forms import SupplierForm, CategoryForm, ProductForm, ImageForm


class ImageNode(DjangoObjectType):
    class Meta:
        model = Image
        interfaces = (relay.Node, )
        fiels = ('url', )

class ImageMutation(DjangoModelFormMutation):
    pet = Field(ImageNode)

    class Meta:
        form_class = ImageForm


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        interfaces = (relay.Node, )
        filter_fields = ['name', 'category',]

class ProductMutation(DjangoModelFormMutation):
    pet = Field(ProductNode)

    class Meta:
        form_class = ProductForm


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (relay.Node, )
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        fields = ('name', 'products', )
        

class CategoryMutation(DjangoModelFormMutation):
    pet = Field(CategoryNode)

    class Meta:
        form_class = CategoryForm



class SupplierNode(DjangoObjectType):
    class Meta:
        model = Supplier
        interfaces = (relay.Node, )
        filter_fields = ['name', 'products']

class SupplierMutation(DjangoModelFormMutation):
    pet = Field(SupplierNode)

    class Meta:
        form_class = SupplierForm


class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    supplier = relay.Node.Field(SupplierNode)
    all_suppliers = DjangoFilterConnectionField(SupplierNode)

    image = relay.Node.Field(ImageNode)
    all_suppliers = DjangoFilterConnectionField(ImageNode)

    product = relay.Node.Field(ProductNode)
    all_suppliers = DjangoFilterConnectionField(ProductNode)


class Mutation(graphene.ObjectType):
    update_supplier = SupplierMutation.Field()
    update_image = ImageMutation.Field()
    update_category = CategoryMutation.Field()
    update_product = ProductMutation.Field()