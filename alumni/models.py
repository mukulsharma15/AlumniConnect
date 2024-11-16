from django.db import models

class AlumniInfo(models.Model):
    alumni_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=150, editable=False)
    email = models.EmailField(unique=True)
    grad_year = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    current_city = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.middle_name or ''} {self.last_name}".strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'Alumni_Info'


class AlumniPhone(models.Model):
    alumni = models.ForeignKey(AlumniInfo, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=5)
    mobile_number = models.CharField(max_length=10)

    class Meta:
        db_table = 'Alumni_Phone'
        unique_together = ('alumni', 'mobile_number')


class AcademicHistory(models.Model):
    alumni = models.ForeignKey(AlumniInfo, on_delete=models.CASCADE)
    degree_name = models.CharField(max_length=100)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Academic_History'
        unique_together = ('alumni', 'degree_name')


class Achievement(models.Model):
    alumni = models.ForeignKey(AlumniInfo, on_delete=models.CASCADE)
    award_title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_awarded = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'Achievements'


class ProfessionalHistory(models.Model):
    alumni = models.ForeignKey(AlumniInfo, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Professional_History'


class SocialMedia(models.Model):
    alumni = models.ForeignKey(AlumniInfo, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'Social_Media'