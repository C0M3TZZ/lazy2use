from django.db import models
# from django.db import models
# Create your models here.
class urldb(models.Model):
    lurl = models.TextField(max_length=200)
    surl = models.TextField(max_length=3)
