from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from internship_app.views import InternshipViewSet, ApplicationsList, InternshipDetailView

router = DefaultRouter()
router.register('internships', InternshipViewSet)

urlpatterns = [
    path('backend/admin', admin.site.urls),
    path('backend/api/', include(router.urls)),
    path('backend/api/applications', ApplicationsList.as_view(), name='applications-list'),
    path('backend/api/internships/<int:pk>', InternshipDetailView.as_view()),
]
