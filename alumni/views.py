from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlumniInfoForm, AcademicHistoryForm, AchievementForm, ProfessionalHistoryForm, SocialMediaForm, AlumniPhoneForm
from .models import AlumniInfo, AcademicHistory, Achievement, ProfessionalHistory, SocialMedia, AlumniPhone

# View for the alumni info form
def alumni_info_create(request):
    if request.method == 'POST':
        form = AlumniInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumni_info_list')
    else:
        form = AlumniInfoForm()
    return render(request, 'alumni/form.html', {'form': form})


# View to list all alumni
def alumni_info_list(request):
    alumni_list = AlumniInfo.objects.all()
    return render(request, 'alumni/admin.html', {'alumni_list': alumni_list})


# View to edit an alumni record
def alumni_info_update(request, pk):
    alumni = get_object_or_404(AlumniInfo, pk=pk)
    if request.method == 'POST':
        form = AlumniInfoForm(request.POST, instance=alumni)
        if form.is_valid():
            form.save()
            return redirect('alumni_info_list')
    else:
        form = AlumniInfoForm(instance=alumni)
    return render(request, 'alumni/form.html', {'form': form})

# alumni/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def alumni_form(request):
    if request.method == "POST":
        # Handle form submission here
        pass
    return render(request, 'alumni_form.html')

def custom_query(request):
    schema = "Display database schema here"
    result = None
    if request.method == "POST":
        sql_query = request.POST.get('sqlQuery')
        # Execute custom SQL query (ensure SQL injection safety)
        pass
    return render(request, 'custom_query.html', {'schema': schema, 'result': result})

from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

def alumni_form(request):
    if request.method == 'POST':
        data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'graduation_year': request.POST.get('graduation_year'),
            'degree': request.POST.get('degree'),
            'major': request.POST.get('major'),
        }
        with open('alumni_data.json', 'a') as f:
            json.dump(data, f)
            f.write('\n')
        return redirect('home')
    return render(request, 'alumni_form.html')
# Additional views for AcademicHistory, Achievement, ProfessionalHistory, SocialMedia, AlumniPhone 
# (following the same create, list, and update structure)
