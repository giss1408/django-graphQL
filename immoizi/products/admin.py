from django.contrib import admin
from .models import Category, Description, Tenant

# Register your models here.
admin.site.register(Category)
admin.site.register(Description)
admin.site.register(Tenant)
