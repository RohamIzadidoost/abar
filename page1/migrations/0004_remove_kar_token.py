# Generated by Django 4.0.6 on 2022-09-09 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0003_karfarma_master_karmand_master'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kar',
            name='token',
        ),
    ]