from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def  student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is None:
            stu = Student.objects.get(id=id)
            serializer= StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer= StudentSerializer(stu ,many=True)
            return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
        
    if request.method == 'PUT':
        serializer = StudentSerializer(data=request.data, instance=pk)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=201)
        else:
            return Response(serializer.errors, status=400)
        
    if request.method == 'PATCH':
        serializer = StudentSerializer(data=request.data, instance=pk)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
        
    if request.method == 'DELETE':
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response(status=204) 
        
            


            
    


