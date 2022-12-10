from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Certificate
from .serializers import CertificateSerializer

# Create your views here.
class CertificatesViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.certificates.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)