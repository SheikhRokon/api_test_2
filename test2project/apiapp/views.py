from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status




@api_view(['GET','POST','PUT','PATCH','DELETE'])
def  student_api(request, pk=None):
    if request.method == 'GET':
        
        if pk is not None:
            stu = Student.objects.get(id=pk)
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
            return Response({'message': 'Post created successfull.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)
    
    
    if request.method == 'PUT':
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(data=request.data, instance=student)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'PUT Update successfull.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    if request.method == 'PATCH':
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(data=request.data, instance=student)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'PATCH Update successful.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
    if request.method == 'DELETE':
        try:
            stu = Student.objects.get(id=pk)
            stu.delete()
            return Response({'message': 'DELETE operation successful.'}, status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({'message': 'Student not found.'}, status=status.HTTP_404_NOT_FOUND) 
        