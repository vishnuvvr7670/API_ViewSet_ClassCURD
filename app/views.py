from django.shortcuts import render

# Create your views here.
from app.serializers import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class ProductCurd(ViewSet):
    def list(self,request):
        LPO=Product.objects.all()
        JPO=ProductSerializer(LPO,many=True)
        return Response(JPO.data)
    
    def retrieve(self,response,pk):
        PO=Product.objects.get(pk=pk)
        JPO=ProductSerializer(PO)
        return Response(JPO.data)
    
    def create(self,request):
        JD=request.data
        PDO=ProductSerializer(data=JD)
        
        if PDO.is_valid():
            PDO.save()
            return Response({'create':'Data Is Inserted'})
        
    def update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JD=request.data
        PDO=ProductSerializer(PO,data=JD)

        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated'})
        else:
            return Response({'Error':'Data is Not Updated'})
        
    def partial_update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JD=request.data
        PDO=ProductSerializer(PO,data=JD,partial=True)

        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated'})
        else:
            return Response({'Error':'Data is Not Updated'})

    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'deleted':'Data is deleted'})


    