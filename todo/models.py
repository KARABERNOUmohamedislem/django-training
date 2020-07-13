from django.db import models


# Create your models h

class Task(models.Model):
    
    title = models.CharField( max_length=50)
    description = models.CharField( max_length=250)

    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")



