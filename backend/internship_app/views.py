from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, filters, generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Internship, Application
from .serializers import InternshipSerializer, ApplicationSerializer
from django.utils.decorators import method_decorator

class InternshipViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Internship.objects.select_related('company').all()
    serializer_class = InternshipSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'company__name', 'location', 'field']

class InternshipDetailView(generics.RetrieveAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer

class ApplicationsList(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)
    @method_decorator(csrf_exempt, name='dispatch')
    def post(self, request, format=None):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)