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
    candidate = CandidateSerializer()
    internship = InternshipSerializer(read_only=True)
    class Meta:
        model = Application
        fields = ['internship', 'candidate']

    def create(self, validated_data):
        candidate_data = validated_data.pop('candidate')
        print("Candidate data: ", candidate_data)
        internship = validated_data.pop('internship')
        print("Internship data: ", internship)
        candidate = Candidate.objects.create(**candidate_data)
        application = Application.objects.create(internship=internship, candidate=candidate, status='Applied')
        print("Successfully created application", application)
        return application
