
from django.contrib import admin
from django.urls import path
from blog.views import WomenlViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/womenlist/', WomenlViewSet.as_view({'get': 'list'})),
    path('api/v1/womenlist/<int:pk>/', WomenlViewSet.as_view({'put': 'update'})),
]
