from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class News(models.Model):
    company = models.CharField(max_length=50)
    subject = models.CharField(max_length=500)
    body = RichTextField()
    datetime= models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.company + '-' + self.subject