from django.urls import path
from .views import HomeView, ProductListCreateView, ProductUpdateView, InventoryValueView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products', ProductListCreateView.as_view(), name='add-product'),
    path('products/<int:id>', ProductUpdateView.as_view(), name='update-product'),
    path('inventory/value', InventoryValueView.as_view(), name='inventory-value'),
]
