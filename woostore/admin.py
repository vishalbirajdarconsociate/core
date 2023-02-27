from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(ProductCategory)
admin.site.register(ProductImages)
admin.site.register(Reviews)
admin.site.register(Modifier)
admin.site.register(ModifierGroup)
admin.site.register(ProductModGroup)
admin.site.register(ModifierModGroup)