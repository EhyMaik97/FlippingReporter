from django.contrib import admin
from django.utils.html import format_html

from .models import Purchase, Sale, Category, Channel


def mark_as_sold(modeladmin, request, queryset):
    queryset.update(is_sold=True)
mark_as_sold.short_description = "Mark selected purchases as sold"

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date', 'channel', 'price', 'is_sold')
    actions = [mark_as_sold]
    
class SaleAdmin(admin.ModelAdmin):
    list_display = ('purchase', 'date', 'channel', 'fee', 'shipping_cost', 'price', 'get_profit')
    readonly_fields = ('purchase_link', 'get_profit')

    def purchase_link(self, obj):
        url = f'/admin/flippingmanager/purchase/{obj.purchase.id}/change/'
        return format_html(
            '<a href="{}">{}</a>: {}',
            url,
            obj.purchase.name,
            obj.purchase.price
        )
    
    def get_profit(self, obj):
        return f'{obj.profit}'
    
    purchase_link.short_description = 'Product Link - Purchase Price'
    get_profit.short_description = 'Profit'

admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Category)
admin.site.register(Channel)
