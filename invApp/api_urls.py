from django.urls import path
from .api_views import ProductAPIView

urlpatterns = [
    path('products/',ProductAPIView.as_view(),name='api_products'),
]   