from rest_framework import viewsets, filters
from .models import Internship, Application
from .serializers import InternshipSerializer, ApplicationSerializer

class InternshipViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Internship.objects.select_related('company').all()
    serializer_class = InternshipSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'company__name', 'location', 'field']


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
