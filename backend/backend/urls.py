from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from internship_app.views import InternshipViewSet, ApplicationViewSet

router = DefaultRouter()
router.register('internships', InternshipViewSet)
router.register('applications', ApplicationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
