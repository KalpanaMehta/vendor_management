from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .api import VendorViewSet
from vendor import views

# router = DefaultRouter()
# router.register(r'api/vendors',VendorViewSet,basename = 'vendor')

urlpatterns = [
    
    path('api/vendors/', views.create_vendor),
]
