from django.contrib import admin

from app.models import Product, Category, Offer


# Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name', 'product_price', 'product_discount', 'product_rating', 'product_is_liked', 'category')
    list_filter = ('product_is_liked', 'category', 'product_discount')
    search_fields = ('product_name', 'product_description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('description_text', 'hours', 'minutes', 'seconds', 'percent', 'countdown', 'image_name')
    search_fields = ('description_text', 'percent', 'image_name')  # Add a search bar for these fields
    list_filter = ('percent',)  # Filter by percentage discount
    ordering = ('-countdown',)  # Order by countdown in descending order


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
