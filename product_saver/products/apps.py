from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'product_saver.products'
    verbose_name = "Products"

    def ready(self):
        try:
            import product_saver.products.signals  # noqa F401
        except ImportError:
            pass