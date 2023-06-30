# Generated by Django 4.2.2 on 2023-06-30 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_staff', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('specialty', models.CharField(choices=[('PED', 'Pediatrician'), ('OBGYN', 'Gynecologist'), ('FAM', 'Family Physician'), ('DERM', 'Dermatologist'), ('RAD', 'Radiologist'), ('PSY', 'Psychiatrist'), ('CAD', 'Cardiologist')], max_length=250)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
