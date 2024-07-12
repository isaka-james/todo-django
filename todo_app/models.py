from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    ROLE_ADMIN = 'admin'
    ROLE_USER = 'user'
    

    ROLE_CHOICES=(
        ('admin','Admin'),
        ('user','User')
    )
    role=models.CharField(max_length=5,choices=ROLE_CHOICES)

    class Meta:
        permissions = [
            ('can_manage_all', 'Can manage all tasks'),
            ('can_view', 'Can view tasks'),
        ]

class Todo(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    expires_at=models.DateTimeField()
    owner=models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def is_expired(self):
        return timezone.now()>self.expires_at

    def __str__(self):
        return self.title