from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import render

from .permission import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Category, Women
from .serializer import WomenSerializer


class WomenSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class WomenListView(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = (WomenSetPagination,)


class WomenUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class WomenDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)





#class WomenAPIViews(APIView):
#    def get(self, request):
#        women = Women.objects.all().values()
#        return Response({'posts': list(women)})
#
#    def post(self, request):
#        serializer = WomenSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response({'post': serializer.data})
#
#    def put(self, request, *args, **kwargs):
#        pk = kwargs.get('pk', None)
#        if not pk:
#            Response({'error': 'Method PUT not allowed'})
#        try:
#            instance = Women.objects.get(pk=pk)
#        except:
#            return Response({'error': 'Object des not exist'})
#        serializer = WomenSerializer(data=request.data, instance=instance)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response({'post': serializer.data})
#
#    def delete(self, request, *args, **kwargs):
#        pk = kwargs.get('pk', None)
#        if not pk:
#            Response({'error': 'Method DELETE not allowed'})
#        try:
#            instance = Women.objects.get(pk=pk)
#        except:
#            return Response({'error': 'Object does not exist'})
#        instance.delete()
#        return Response({'post': 'Post deleted'})
#
#
#
#class WomenlViewSet(viewsets.ModelViewSet):
#    queryset = Women.objects.all()[:3]
#    serializer_class = WomenSerializer
#
#    @action(methods=['get'], detail=True)
#    def category(self, request, pk=None):
#        cats = Category.objects.get(pk=pk)
#        return Response({'cats': cats.name}) 
#
#     @action(methods=['get'], detail=False)
#    def category(self, request):
#        cats = Category.objects.all()
#        return Response({'cats': [category.name for category in cats]})

