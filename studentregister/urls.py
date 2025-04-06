from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from studentregisterapi.views import (
    StudentRosterView, SchoolListCreateView, SchoolDetailView,
    TeacherListCreateView, TeacherDetailView, SubjectListCreateView,
    SubjectDetailView, StatusListCreateView, StatusDetailView,
    HomeroomListCreateView, HomeroomDetailView, StudentListCreateView,
    StudentDetailView, StudentSubjectListCreateView, StudentSubjectDetailView
)
from django.http import HttpResponse

# Home view for root path
def home(request):
    return HttpResponse("Welcome to the Student Register Management API!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('roster/', StudentRosterView.as_view(), name='student-roster'),
    path('schools/', SchoolListCreateView.as_view(), name='school-list-create'),
    path('schools/<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),
    path('statuses/', StatusListCreateView.as_view(), name='status-list-create'),
    path('statuses/<int:pk>/', StatusDetailView.as_view(), name='status-detail'),
    path('homerooms/', HomeroomListCreateView.as_view(), name='homeroom-list-create'),
    path('homerooms/<int:pk>/', HomeroomDetailView.as_view(), name='homeroom-detail'),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student-subjects/', StudentSubjectListCreateView.as_view(), name='student-subject-list-create'),
    path('student-subjects/<int:pk>/', StudentSubjectDetailView.as_view(), name='student-subject-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
