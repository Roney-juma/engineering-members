from django.db import models


class Member(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    membership_number = models.CharField(max_length=50, unique=True)
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name

