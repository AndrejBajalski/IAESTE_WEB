from rest_framework import serializers
from .models import Company, Internship, Application, Candidate


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class InternshipSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Internship
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    internship = InternshipSerializer(read_only=True)
    intern = CandidateSerializer(read_only=True)
    class Meta:
        model = Application
        fields = '__all__'
