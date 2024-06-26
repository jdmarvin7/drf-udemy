from django.urls import path
from .views import site, api
from .views.class_based_view import mixins

app_name = 'recipes'

urlpatterns = [
    path(
        '',
        site.RecipeListViewHome.as_view(),
        name="home"
    ),
    path(
        'recipes/search/',
        site.RecipeListViewSearch.as_view(),
        name="search"
    ),
    path(
        'recipes/tags/<slug:slug>/',
        site.RecipeListViewTag.as_view(),
        name="tag"
    ),
    path(
        'recipes/category/<int:category_id>/',
        site.RecipeListViewCategory.as_view(),
        name="category"
    ),
    path(
        'recipes/<int:pk>/',
        site.RecipeDetail.as_view(),
        name="recipe"
    ),
    path(
        'recipes/api/v1/',
        site.RecipeListViewHomeApi.as_view(),
        name="recipes_api_v1",
    ),
    path(
        'recipes/api/v1/<int:pk>/',
        site.RecipeDetailAPI.as_view(),
        name="recipes_api_v1_detail",
    ),
    path(
        'recipes/theory/',
        site.theory,
        name='theory',
    ),
    path(
        'api/recipes/',
        # view usando @api_view()
        # api.recipe_list,

        # view usando APIView
        # api.RecipesView.as_view(),

        # view usando generics views
        mixins.RecipeMixinsView.as_view(),
        name='api_list_recipes'
    ),
    path(
        'api/v2/recipes/',
        # view usando @api_view()
        # api.recipe_list,

        # view usando APIView
        # api.RecipesView.as_view(),

        # view usando generics views
        # mixins.RecipeMixinsView.as_view(),

        # Viewsets
        mixins.RecipeViewset.as_view({
            'get': 'list',
            'post': 'create',
            'patch': 'partial_update',
            'delete': 'destroy',
        }),
        name='api_list_recipes_v2'
    ),
    path(
        'api/recipes/<int:pk>/',
        # @api_view()
        # api.recipe_api_detail,

        # APIView
        # api.RecipesDetailView.as_view(),

        # generics view
        mixins.RecipeMixinsDetailView.as_view(),
        name='api_recipes_detail'
    )
]
