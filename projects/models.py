from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1200)
    image = models.ImageField(upload_to="pics")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
