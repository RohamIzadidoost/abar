# Generated by Django 4.0.6 on 2022-09-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0002_alter_kar_token_alter_karmand_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='karfarma',
            name='master',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='karmand',
            name='master',
            field=models.IntegerField(default=0),
        ),
    ]
