from django.contrib.auth import get_user_model
from rest_framework import serializers

from recipes.models import FavoriteRecipe, ShoppingCart, Recipe, RecipeIngredient
from tags.serializers import TagSerializer
from users.models import Subscription

User = get_user_model()


class RecipesUserSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name', 'is_subscribed')

    def get_is_subscribed(self, obj):
        request_user = self.context.get('request').user.id
        queryset = Subscription.objects.filter(author=obj.id, subscriber=request_user).exists()
        return queryset


class RecipeIngredientSerializer(serializers.ModelSerializer):
    """Возвращает ингридиент, его единицу измерения и количество в рецепте."""
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(source='ingredient.measurement_unit')

    class Meta:
        model = RecipeIngredient
        fields = ["id", "name", "measurement_unit", "amount", ]


class RecipeSerializer(serializers.ModelSerializer):
    """Возвращает рецепт, либо список рецептов. Создает и изменяет рецепт."""
    tags = TagSerializer(many=True)
    author = RecipesUserSerializer()
    ingredients = RecipeIngredientSerializer(source="recipeingredient_set", many=True)
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = (
            'id',
            'tags',
            'author',
            'ingredients',
            'is_favorited',
            'is_in_shopping_cart',
            'name',
            'image',
            'text',
            'cooking_time'
        )
        read_only_fields = ('id',)

    def get_is_favorited(self, obj):
        """
        Добавляет поле избранного - есть ли данный рецепт у
        текущего пользователя в избранном: true/false.
        """
        request_user = self.context.get('request').user.id
        queryset = FavoriteRecipe.objects.filter(user=request_user, recipe=obj).exists()
        return queryset

    def get_is_in_shopping_cart(self, obj):
        """
        Добавляет поле списка покупок - есть ли данный рецепт у
        текущего пользователя в списке покупок: true/false.
        """
        request_user = self.context.get('request').user.id
        queryset = ShoppingCart.objects.filter(user=request_user, recipe=obj).exists()
        return queryset


class ShortRecipeSerializer(serializers.ModelSerializer):
    """Выводит нужные свойства рецепта."""
    image = serializers.URLField

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class ShoppingCartSerializer(serializers.ModelSerializer):
    """Выводит список рецептов, добавленных в список покупок."""

    class Meta:
        model = ShoppingCart
        fields = '__all__'