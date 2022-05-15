from rest_framework import generics
from django.shortcuts import render

from blog.models import Women
from blog.serializer import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
