from django.db import models

# Create your models here.
class regexPattern(models.Model):
    file=models.FileField(upload_to='temporaryFiles/', max_length=250, blank=True, default=None, verbose_name='',)
        