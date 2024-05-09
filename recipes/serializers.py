from collections import defaultdict
from rest_framework import serializers

from authors.validators import AuthorRecipeValidator
from recipes.models import Category, Recipe
from tag.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Recipe
        exclude = ['id',]

    """
    id = serializers.UUIDField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    public = serializers.BooleanField(source='is_published')
    preparation = serializers.SerializerMethodField(method_name='any_method_name')
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    category_name = serializers.StringRelatedField(
        source='category'
    )
    author = serializers.StringRelatedField()
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True
    )
    tag_links = serializers.HyperlinkedRelatedField(
        many=True,
        source='tags',
        queryset=Tag.objects.all(),
        view_name='recipes:api_recipes_detail'
    )

    tags = TagSerializer(many=True)
    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
    """

    def any_method_name(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
    
    def validate(self, attrs):
        super_validate = super().valida(attrs)
        AuthorRecipeValidator(
            data=attrs,
            ErrorClass=serializers.ValidationError,
        )

        # cd = attrs

        # _my_errors = defaultdict(list)

        # title = cd.get('title')
        # description = cd.get('description')

        # if title == description:
        #     _my_errors['title'].append('Cannot be equal to description')
        #     _my_errors['description'].append('Cannot be equal to title')

        # if _my_errors:
        #     raise serializers.ValidationError(_my_errors)

        return super_validate
    
    def validate_title(self, value):
        title = value

        if len(title) < 5:
            raise serializers.ValidationError('Must have at least 5 chars.')

        return title
    
    def save(self, **kwargs):
        return super().save(**kwargs)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
        