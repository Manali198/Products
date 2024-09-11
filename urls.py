from django import path,include
from rest_framework.routers import DefaultRouter
from .views import ProdView

router = DefaultRouter()
router.registry(r'products',ProdViewSet)

urlpattern = [
    path(' ',include(router.urls)),
    ]