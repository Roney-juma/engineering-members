# Generated by Django 5.1.2 on 2024-10-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to='certificates/'),
        ),
    ]
