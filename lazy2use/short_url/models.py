from django.db import models
# from django.db import models
# Create your models here.
<<<<<<< HEAD
class urldb(models.Model):
    lurl = models.TextField(max_length=200)
    surl = models.TextField(max_length=3)
=======
class url_db(models.Model):
    long_url = models.TextField(max_length=200)
    short_url = models.TextField(max_length=3)
>>>>>>> main
