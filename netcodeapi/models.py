from django.db import models

# Create your models here.

class Code(models.Model):
    topic = models.CharField(max_length=200)
    code = models.TextField()
    url = models.URLField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.topic