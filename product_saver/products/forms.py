from django.forms import ModelForm
from product_saver.products.models import Supplier, Category, Product, Image

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('url', 'product', )

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',  )

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'url', )

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'url','rating', 'reviews', 'positive_reviews', 
        'orders', 'price', 'price_long', 'shipping_options', 'epacket_available', 
        'supplier', 'category', 'tags' )
