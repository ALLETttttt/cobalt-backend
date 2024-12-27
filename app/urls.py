from django.urls import path

from app.views import ProductListView, ProductDetailView, \
    ToggleLikeView, CategoryListView, CategoryProductsView, LikedProductListView, OfferListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('offers/', OfferListView.as_view(), name='offer_list'),
    path('products/liked/', LikedProductListView.as_view(), name='liked_product'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:product_id>/like/', ToggleLikeView.as_view(), name='toggle_like'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:category_id>/products/', CategoryProductsView.as_view(), name='category_products'),
]
