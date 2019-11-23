from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status

# Create your views here.


def index(request):
    
    return render(request, 'index.html')

@api_view(['GET','POST'])
def product_list_of_my_site(request):
    if request.method == "GET":
        obj = Product.objects.all()
        serializer = ProductSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def submit(request):
    if request.method=="POST":
        data = request.POST
        a = Product()
        a.name = data['name']
        a.description = data['description']
        a.price = data['price']
        a.save()
        
    return render(request, 'submit.html')


@api_view(['GET'])
def product_list(request, id):
    id = int(id)
    
    obj = Product.objects.get(id=id)
    if obj:
        serializer = ProductSerializer(obj)   
        return Response(serializer.data) 
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
   


    
    
   