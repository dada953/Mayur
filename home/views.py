from django.shortcuts import render
from rest_framework.views import APIView
from home.serilizers import StudentSerilizer
from rest_framework.response import Response
# Create your views here.
class StudentView(APIView):
    def post(self,request):
        serilizer=StudentSerilizer(data=request.data)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return Response(serilizer.validated_data) 
