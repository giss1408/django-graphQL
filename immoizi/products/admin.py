from django.contrib import admin
from .models import Landlord, Property, Tenant, Lease, AfricanLocation

# Register your models here.
admin.site.register(Landlord)
admin.site.register(Property)
admin.site.register(Tenant)
admin.site.register(Lease)
admin.site.register(AfricanLocation)
