from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.hashers import make_password
from django.db import models
from ckeditor.fields import RichTextField
import cloudinary
import cloudinary.uploader
import cloudinary.models

class Member(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    membership_number = models.CharField(max_length=50, unique=True)
    profile_picture = cloudinary.models.CloudinaryField('image', null=True, blank=True)
    certificate = cloudinary.models.CloudinaryField('file', null=True, blank=True)  
    join_date = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    CLOUDINARY_BASE_URL = "https://res.cloudinary.com/diwhoj80y/"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if self.pk is None:  
            self.password = make_password(self.password)
        
        # Automatically set the username to be the email if not provided
        if not self.username:
            self.username = self.email
        
        # Validate uniqueness of username
        if Member.objects.filter(username=self.username).exists() and self.pk is None:
            raise ValidationError("A member with this username already exists.")
        
        if not self.membership_number:
            member_count = Member.objects.count() + 1
            self.membership_number = f"MESK-{member_count}"
        
        super().save(*args, **kwargs)

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = cloudinary.models.CloudinaryField('image')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255)
    image = cloudinary.models.CloudinaryField('image', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title