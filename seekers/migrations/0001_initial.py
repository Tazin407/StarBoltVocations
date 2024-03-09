# Generated by Django 4.2.7 on 2024-03-02 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SeekerPersonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=40)),
                ('district', models.CharField(max_length=40)),
                ('thana', models.CharField(max_length=40)),
                ('address', models.TextField()),
                ('postal_code', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=20)),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.CharField(max_length=12)),
                ('education_level', models.CharField(choices=[('PSC', 'PSC'), ('JSC', 'JSC'), ('SSC/Equivalent', 'SSC/Equivalent'), ('HSC/Equivalent', 'HSC/Equivalent'), ('Diploma', 'Diploma'), ('Undergrad', 'Undergrad'), ('Postgrad', 'Postgrad')], max_length=20)),
                ('board', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chattogram', 'Chattogram'), ('Cumilla', 'Cumilla'), ('Rangpur', 'Rangpur'), ('Rajshahi', 'Rajshahi'), ('Khulna', 'Khulna'), ('Syllhet', 'Syllhet'), ('Barisal', 'Barisal')], max_length=20)),
                ('passing_year', models.IntegerField()),
                ('result', models.CharField(max_length=3)),
                ('group', models.CharField(max_length=20)),
                ('skillset', models.TextField()),
                ('experience', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]