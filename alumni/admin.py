from django.contrib import admin
from .models import AlumniInfo, AlumniPhone, AcademicHistory, Achievement, ProfessionalHistory, SocialMedia

admin.site.register(AlumniInfo)
admin.site.register(AlumniPhone)
admin.site.register(AcademicHistory)
admin.site.register(Achievement)
admin.site.register(ProfessionalHistory)
admin.site.register(SocialMedia)