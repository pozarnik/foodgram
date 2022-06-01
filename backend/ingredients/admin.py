from django.contrib import admin

from ingredients.models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_editable = ('name', 'measurement_unit')
    list_filter = ('measurement_unit',)
    ordering = ('name',)
