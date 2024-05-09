from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Recipe
from ..serializers import RecipeSerializer
from django.shortcuts import get_object_or_404

@api_view(http_method_names=['get', 'post'])
def recipe_list(request):
    if request.method == 'GET':
        model = Recipe.objects.all()
        serializer = RecipeSerializer(model, many=True).data
        return Response(serializer)
    
    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.validated_data,
                status=status.HTTP_201_CREATED,
            )
        
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(http_method_names=['get', 'patch', 'delete'])
def recipe_api_detail(request, pk):
    model = get_object_or_404(
        Recipe.objects.get_published(),
        pk=pk
    )

    if request.method == 'GET':
        serializer = RecipeSerializer(
            model,
            many=False,
            context={'request': request}
        ).data
        return Response(serializer)
    elif request.method == 'PATCH':
        serializer = RecipeSerializer(
            model,
            many=False,
            data=request.data,
            context={'request': request},
            partial=True,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data
        )
    elif request.method == 'DELETE':
        model.delete()
        return Response('DELETE', status=status.HTTP_200_OK)