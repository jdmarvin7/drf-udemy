from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Recipe
from ..serializers import RecipeSerializer
from django.shortcuts import get_object_or_404

@api_view(http_method_names=['get'])
def recipe_list(request):
    model = Recipe.objects.all()
    serializer = RecipeSerializer(model, many=True).data
    return Response(serializer)

@api_view(http_method_names=['get'])
def recipe_api_detail(request, pk):
    model = get_object_or_404(
        Recipe.objects.all(),
        pk=pk
    )
    serializer = RecipeSerializer(model, many=False).data
    return Response(serializer)