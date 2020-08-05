from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class User(AbstractUser):
    resume = models.FileField(null = True, blank= True)
    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

class Contact(models.Model):
    name = models.CharField(max_length=100, help_text = 'Enter your name')
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length = 100)
    message = models.TextField(null = True, blank = True)
    image = models.ImageField(null=True, blank = True, upload_to= 'media')
    def __str__(self):
        return f'{self.name}, {self.subject}'
