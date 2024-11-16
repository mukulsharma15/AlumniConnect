from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
import os
from rest_framework import viewsets
from .models import AlumniInfo, AlumniPhone, AcademicHistory, Achievement, ProfessionalHistory, SocialMedia
from .serializers import AlumniInfoSerializer, AlumniPhoneSerializer, AcademicHistorySerializer, AchievementSerializer, ProfessionalHistorySerializer, SocialMediaSerializer

class AlumniInfoViewSet(viewsets.ModelViewSet):
    queryset = AlumniInfo.objects.all()
    serializer_class = AlumniInfoSerializer

class AlumniPhoneViewSet(viewsets.ModelViewSet):
    queryset = AlumniPhone.objects.all()
    serializer_class = AlumniPhoneSerializer

class AcademicHistoryViewSet(viewsets.ModelViewSet):
    queryset = AcademicHistory.objects.all()
    serializer_class = AcademicHistorySerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class ProfessionalHistoryViewSet(viewsets.ModelViewSet):
    queryset = ProfessionalHistory.objects.all()
    serializer_class = ProfessionalHistorySerializer

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def alumni_form(request):
    if request.method == 'POST':
        # Save Alumni Info
        alumni_info = AlumniInfo.objects.create(
            first_name=request.POST.get('first_name'),
            middle_name=request.POST.get('middle_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            grad_year=request.POST.get('graduation_year'),
            date_of_birth=request.POST.get('dob'),
            current_city=request.POST.get('current_city')
        )

        # Save Alumni Phone
        for country_code, mobile_number in zip(request.POST.getlist('country_code[]'), request.POST.getlist('mobile_number[]')):
            AlumniPhone.objects.create(
                alumni=alumni_info,
                country_code=country_code,
                mobile_number=mobile_number
            )

        # Save Academic History
        for degree_name, cgpa, start_year, end_year in zip(request.POST.getlist('degree_name[]'), request.POST.getlist('cgpa[]'), request.POST.getlist('start_year[]'), request.POST.getlist('end_year[]')):
            AcademicHistory.objects.create(
                alumni=alumni_info,
                degree_name=degree_name,
                cgpa=cgpa,
                start_year=start_year,
                end_year=end_year
            )

        # Save Achievements
        for award_title, description, date_awarded in zip(request.POST.getlist('award_title[]'), request.POST.getlist('description[]'), request.POST.getlist('date_awarded[]')):
            Achievement.objects.create(
                alumni=alumni_info,
                award_title=award_title,
                description=description,
                date_awarded=date_awarded
            )

        # Save Professional History
        for company_name, job_title, start_date, end_date, skills in zip(request.POST.getlist('company_name[]'), request.POST.getlist('job_title[]'), request.POST.getlist('start_date[]'), request.POST.getlist('end_date[]'), request.POST.getlist('skills[]')):
            ProfessionalHistory.objects.create(
                alumni=alumni_info,
                company_name=company_name,
                job_title=job_title,
                start_date=start_date,
                end_date=end_date,
                skills=skills
            )

        # Save Social Media
        for platform, username in zip(request.POST.getlist('platform[]'), request.POST.getlist('username[]')):
            SocialMedia.objects.create(
                alumni=alumni_info,
                platform=platform,
                username=username
            )

        return redirect('alumni_form')

    return render(request, 'alumni_form.html')

def custom_query(request):
    # Implement your custom query logic here
    return render(request, 'custom_query.html')
