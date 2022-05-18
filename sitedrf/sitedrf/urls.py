
from django.contrib import admin
from django.urls import include, path, re_path
from blog.views import WomenListView, WomenUpdateView, WomenDestroyView
from rest_framework import routers


#router = routers.DefaultRouter()
#router.register(r'women', WomenlViewSet)
#print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/v1/', include(router.urls)),
    path('api/v1/auth', include('rest_framework.urls')),
    path('api/v1/women/', WomenListView.as_view()),
    path('api/v1/women/<int:pk>/', WomenUpdateView.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenDestroyView.as_view()),
    path(r'api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
