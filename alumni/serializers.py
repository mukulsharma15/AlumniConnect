from rest_framework import serializers
from .models import AlumniInfo, AlumniPhone, AcademicHistory, Achievement, ProfessionalHistory, SocialMedia

class AlumniInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlumniInfo
        fields = '__all__'


class AlumniPhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlumniPhone
        fields = '__all__'


class AcademicHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcademicHistory
        fields = '__all__'


class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class ProfessionalHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProfessionalHistory
        fields = '__all__'


class SocialMediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'