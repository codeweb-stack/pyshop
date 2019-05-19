from django.contrib import admin

# Register your models here.
from .models import Product, Offer





class OfferAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount']


admin.site.register(Product)
admin.site.register(Offer, OfferAdmin)