from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=850)
    image = models.CharField(max_length=3000)
    film_id = models.CharField(max_length=12)

    def __str__(self):
        return self.title
