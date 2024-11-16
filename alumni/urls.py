from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'alumniinfo', views.AlumniInfoViewSet)
router.register(r'alumniphone', views.AlumniPhoneViewSet)
router.register(r'academichistory', views.AcademicHistoryViewSet)
router.register(r'achievement', views.AchievementViewSet)
router.register(r'professionalhistory', views.ProfessionalHistoryViewSet)
router.register(r'socialmedia', views.SocialMediaViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('alumni_form/', views.alumni_form, name='alumni_form'),
    path('custom_query/', views.custom_query, name='custom_query'),
    path('', include(router.urls)),
]