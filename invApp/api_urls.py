from django.urls import path
from .api_views import ProductAPIView, ProductDetailAPIView

urlpatterns = [
    path('products/',ProductAPIView.as_view(),name='api_products'),

    path('products/<int:product_id>/',ProductDetailAPIView.as_view(),name="product_detail")
]   