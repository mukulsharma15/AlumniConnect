# Generated by Django 5.1.3 on 2024-11-14 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='academichistory',
            table='Academic_History',
        ),
        migrations.AlterModelTable(
            name='achievement',
            table='Achievements',
        ),
        migrations.AlterModelTable(
            name='alumniinfo',
            table='Alumni_Info',
        ),
        migrations.AlterModelTable(
            name='alumniphone',
            table='Alumni_Phone',
        ),
        migrations.AlterModelTable(
            name='professionalhistory',
            table='Professional_History',
        ),
        migrations.AlterModelTable(
            name='socialmedia',
            table='Social_Media',
        ),
    ]
