from django.db import models

class ShortUrl(models.Model):
    short_name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return '{} : {}'.format(self.short_name, self.url)
# Create your models here.
