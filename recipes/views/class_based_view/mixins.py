from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import mixins

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer

#Pagination
class RecipeAPIPagination(PageNumberPagination):
    page_size = 10

# Generics views
class RecipeMixinsView(ListCreateAPIView):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIPagination

class RecipeMixinsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIPagination

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        recipe = self.get_queryset().filter(pk=pk).first()

        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            many=True,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data
        )

    
