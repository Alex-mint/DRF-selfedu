from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

from .models import Women
from .serializer import WomenSerializer


class WomenlViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


""" class WomenAPIView(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenCRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIViews(APIView):
    def get(self, request):
        women = Women.objects.all().values()
        return Response({'posts': list(women)})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            Response({'error': 'Method PUT not allowed'})
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error': 'Object des not exist'})
        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            Response({'error': 'Method DELETE not allowed'})
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})
        instance.delete()
        return Response({'post': 'Post deleted'}) """

