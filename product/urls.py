from django.urls import path, include

from .views import LatestProductView, ProductView, CategoryDetail, search

urlpatterns = [
    path('latest-products/', LatestProductView.as_view(), name='latest-products'),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductView.as_view(), name='product'),
    path('products/<slug:category_slug>/', CategoryDetail.as_view(), name='product-category'),
    path('search/', search, name='search')
]
