from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductInLineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInLineAdmin]

admin.site.register(Order, OrderAdmin)

# Register your models here.
