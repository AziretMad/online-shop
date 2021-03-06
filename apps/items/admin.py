from django.contrib import admin
from .models import ParentCategory, Category, Item


@admin.register(ParentCategory)
class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')
