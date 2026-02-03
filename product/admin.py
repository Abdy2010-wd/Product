from django.contrib import admin
from .models import Category, Product, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    search_fields = ['title']
    list_filter = ['price', 'category']
    list_display = ['title', 'price', 'category', 'owner']
    list_editable = ['price']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)













# from django.contrib import admin
# from .models import Category, Product, Review


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'price', 'category')
#     list_filter = ('category',)
#     search_fields = ('title',)


# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('id', 'product', 'stars', 'short_text')
#     list_filter = ('stars',)
#     search_fields = ('text',)

#     def short_text(self, obj):
#         return obj.text[:40]

