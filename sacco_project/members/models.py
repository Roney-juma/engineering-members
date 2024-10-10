from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.hashers import make_password

class Member(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    membership_number = models.CharField(max_length=50, unique=True)
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=128)  # No default for security

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.pk is None:  
            self.password = make_password(self.password)
        
        # Automatically set the username to be the email if not provided
        if not self.username:
            self.username = self.email
        
        # Validate uniqueness of username
        if Member.objects.filter(username=self.username).exists() and self.pk is None:
            raise ValidationError("A member with this username already exists.")
        
        super().save(*args, **kwargs)

