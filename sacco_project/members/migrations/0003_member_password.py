# Generated by Django 5.1.2 on 2024-10-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(default='Welcome@123', max_length=128),
        ),
    ]
