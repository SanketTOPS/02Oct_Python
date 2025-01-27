from django.contrib import admin
from .models import *


# Register your models here.
class productData(admin.ModelAdmin):
    list_display = ["pname", "modelname", "price"]


admin.site.register(product)
admin.site.register(subcategory, productData)
