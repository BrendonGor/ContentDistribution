from django.shortcuts import render
from rest_framework import viewsets
from .models import Subject, Course, Topic
from .permissions import UpdateIfStaffPermission
from .serializers import SubjectSerializer, CourseSerializer, TopicSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    """
    https://testdriven.io/blog/drf-views-part-3/
    Can be used to create, update, delete, and retrieve subjects.
    """

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [UpdateIfStaffPermission]


class CourseViewSet(viewsets.ModelViewSet):
    """
    Can be used to create, update, delete, and retrieve courses.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [UpdateIfStaffPermission]


class TopicViewSet(viewsets.ModelViewSet):
    """
    Can be used to create, update, delete, and retrieve topics.
    """

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [UpdateIfStaffPermission]
