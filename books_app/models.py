from django.conf import settings
from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=40)
    text = models.CharField(max_length=100, default='')
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(default='', null=False, db_index=True)

    def __str__(self):
        return f'{self.name}'