from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
import os

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def alumni_form(request):
    data = []
    if os.path.exists('alumni_data.json'):
        with open('alumni_data.json', 'r') as f:
            for line in f:
                data.append(json.loads(line))

    if request.method == 'POST':
        alumni_info = {
            'first_name': request.POST.get('first_name'),
            'middle_name': request.POST.get('middle_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'graduation_year': request.POST.get('graduation_year'),
            'dob': request.POST.get('dob'),
            'current_city': request.POST.get('current_city'),
        }

        alumni_phone = []
        for country_code, mobile_number in zip(request.POST.getlist('country_code[]'), request.POST.getlist('mobile_number[]')):
            alumni_phone.append({
                'country_code': country_code,
                'mobile_number': mobile_number,
            })

        academic_history = []
        for degree_name, cgpa, start_year, end_year in zip(request.POST.getlist('degree_name[]'), request.POST.getlist('cgpa[]'), request.POST.getlist('start_year[]'), request.POST.getlist('end_year[]')):
            academic_history.append({
                'degree_name': degree_name,
                'cgpa': cgpa,
                'start_year': start_year,
                'end_year': end_year,
            })

        achievements = []
        for award_title, description, date_awarded in zip(request.POST.getlist('award_title[]'), request.POST.getlist('description[]'), request.POST.getlist('date_awarded[]')):
            achievements.append({
                'award_title': award_title,
                'description': description,
                'date_awarded': date_awarded,
            })

        professional_history = []
        for company_name, job_title, start_date, end_date, skills in zip(request.POST.getlist('company_name[]'), request.POST.getlist('job_title[]'), request.POST.getlist('start_date[]'), request.POST.getlist('end_date[]'), request.POST.getlist('skills[]')):
            professional_history.append({
                'company_name': company_name,
                'job_title': job_title,
                'start_date': start_date,
                'end_date': end_date,
                'skills': skills,
            })

        social_media = []
        for platform, username in zip(request.POST.getlist('platform[]'), request.POST.getlist('username[]')):
            social_media.append({
                'platform': platform,
                'username': username,
            })

        new_entry = {
            'alumni_info': alumni_info,
            'alumni_phone': alumni_phone,
            'academic_history': academic_history,
            'achievements': achievements,
            'professional_history': professional_history,
            'social_media': social_media,
        }

        data.append(new_entry)

        with open('alumni_data.json', 'a') as f:
            json.dump(new_entry, f)
            f.write('\n')

        return redirect('alumni_form')

    return render(request, 'alumni_form.html', {'data': json.dumps(data)})

def custom_query(request):
    # Implement your custom query logic here
    return render(request, 'custom_query.html')
