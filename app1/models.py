from django.db import models

class HtmlContact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
