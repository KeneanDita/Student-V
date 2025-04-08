from rest_framework import generics
from rest_framework.views import APIView
from studentregisterapi.forms import StudentForm
from .models import School, Teacher, Subject, Status, Homeroom, Student, StudentSubject
from django.shortcuts import get_object_or_404, redirect, render,redirect
from .serealizers import (
    SchoolSerializer,
    TeacherSerializer,
    SubjectSerializer,
    StatusSerializer,
    HomeroomSerializer,
    StudentSerializer,
    StudentSubjectSerializer
)

# School Views
class SchoolListCreateView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

# Teacher Views
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# Subject Views
class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# Status Views
class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

# Homeroom Views
class HomeroomListCreateView(generics.ListCreateAPIView):
    queryset = Homeroom.objects.all()
    serializer_class = HomeroomSerializer

class HomeroomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Homeroom.objects.all()
    serializer_class = HomeroomSerializer

# Student Views
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# StudentSubject Views
class StudentSubjectListCreateView(generics.ListCreateAPIView):
    queryset = StudentSubject.objects.all()
    serializer_class = StudentSubjectSerializer

class StudentSubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentSubject.objects.all()
    serializer_class = StudentSubjectSerializer
class StudentRosterView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def table_view(request):
    # Fetch all students (you can add filtering, ordering, etc. as needed)
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'table.html', context)

def upload_profile_image(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = StudentForm()
    return render(request, 'upload.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')
