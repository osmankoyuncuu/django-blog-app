from django.urls import path, include
from rest_framework import routers
from .views import CategoryMVS, PostMVS

router = routers.DefaultRouter()
router.register('blog', PostMVS)
router.register('category', CategoryMVS)

urlpatterns = [
    path('', include(router.urls) )
]