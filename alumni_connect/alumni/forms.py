from django import forms
from .models import AlumniInfo, AcademicHistory, Achievement, ProfessionalHistory, SocialMedia, AlumniPhone

class AlumniInfoForm(forms.ModelForm):
    class Meta:
        model = AlumniInfo
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'grad_year', 'current_city', 'date_of_birth']


class AcademicHistoryForm(forms.ModelForm):
    class Meta:
        model = AcademicHistory
        fields = ['alumni', 'degree_name', 'cgpa', 'start_year', 'end_year']


class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['alumni', 'award_title', 'description', 'date_awarded']


class ProfessionalHistoryForm(forms.ModelForm):
    class Meta:
        model = ProfessionalHistory
        fields = ['alumni', 'company_name', 'job_title', 'start_date', 'end_date', 'skills']


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = ['alumni', 'platform', 'username', 'profile_link']


class AlumniPhoneForm(forms.ModelForm):
    class Meta:
        model = AlumniPhone
        fields = ['alumni', 'country_code', 'mobile_number']
