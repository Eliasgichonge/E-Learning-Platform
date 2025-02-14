from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
      title = models.CharField(max_length=200)
      slug = models.SlugField(max_length=200, unique=True)

      class Meta:
            ordering = ['title']


