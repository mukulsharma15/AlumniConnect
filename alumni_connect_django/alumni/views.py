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


# Additional views for AcademicHistory, Achievement, ProfessionalHistory, SocialMedia, AlumniPhone 
# (following the same create, list, and update structure)
