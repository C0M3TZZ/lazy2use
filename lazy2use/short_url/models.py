from django.db import models
# from django.db import models
# Create your models here.
class url_db(models.Model):
    long_url = models.TextField(max_length=200)
    short_url = models.TextField(max_length=3)