from django.shortcuts import render
from .models import Lecture
from .serializers import LectureSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class LectureList(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save()



