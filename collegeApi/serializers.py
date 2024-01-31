from rest_framework import serializers
from collegeApi.models import Course, Department, Student,Faculty

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

