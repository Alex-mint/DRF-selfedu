
from django.contrib import admin
from django.urls import include, path
from blog.views import WomenlViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'women', WomenlViewSet)
#print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
