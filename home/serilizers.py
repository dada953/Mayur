from rest_framework import serializers
from .models import Student
class StudentSerilizer(serializers.ModelSerializer):
   # name=serializers.CharField()
    def validate_mobileno(self, value):
        return value
      
    class Meta:
        model=Student
        fields=['mobileno','lastName','firstName']
        extra_kwargs = {'firstName': {'required': False}} 