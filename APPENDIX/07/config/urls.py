from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from posts import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
