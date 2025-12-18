from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(null=True, max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.city}, {self.country}"


class Internship(models.Model):
    FIELD_CHOICES = [
        ('IT', 'IT'),
        ('Mechanical', 'Mechanical Engineering'),
        ('Electrical', 'Electrical Engineering'),
        ('Architecture', 'Architecture'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Biomedical', 'Biomedical Engineering'),
        ('Marketing', 'Marketing'),
        ('Finance', 'Finance'),
    ]
    referent_number = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    field = models.CharField(max_length=50, choices=FIELD_CHOICES)
    description = models.TextField()
    internship_start = models.DateField()
    internship_end = models.DateField()
    monthly_salary = models.IntegerField(validators=[MinValueValidator(300)])
    duration_in_weeks = models.IntegerField(default=6, validators=[MinValueValidator(4)])

    def __str__(self):
        return f"{self.referent_number} {self.company.__str__()}"


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Application(models.Model):
    applicationStatus = [
        ('Applied', 'Applied'),
        ('Nominated', 'Nominated'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed internship'),
    ]
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    intern = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=applicationStatus)

    def __str__(self):
        return (f"Applicant: {self.intern.__str__()}\n"
                f"Company: {self.internship.__str__()}\n"
                f"Status: {self.status}")
