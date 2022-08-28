# Generated by Django 4.0.6 on 2022-08-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0005_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('value', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
                ('owner', models.CharField(max_length=100)),
                ('explanations', models.CharField(max_length=500)),
            ],
        ),
    ]
