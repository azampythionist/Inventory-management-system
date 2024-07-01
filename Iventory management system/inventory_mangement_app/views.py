from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer

class HomeView(APIView):
    def get(self, request):
        return Response("Inventory Management System")


class ProductListCreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateView(APIView):
    def put(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        product.quantity = request.data.get('quantity', product.quantity)
        product.save()
        return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)


class InventoryValueView(APIView):
    def get(self, request):
        total_value = sum(product.quantity * product.price for product in Product.objects.all())
        return Response({'total_value': total_value}, status=status.HTTP_200_OK)
