from django.db import models


class Menu(models.Model):
    image = models.FileField(upload_to='img/')
