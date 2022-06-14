from django.contrib import admin
from .models import HealthInsurance, Product, Province, Address, User, Order, OrderDetail

# Register your models here.

admin.site.register(HealthInsurance)
admin.site.register(Product)
admin.site.register(Province)
admin.site.register(Address)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderDetail)
