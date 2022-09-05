# Generated by Django 4.0.6 on 2022-09-05 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page1', '0006_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.AddField(
            model_name='employee',
            name='token',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='job',
            name='token',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='job',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
