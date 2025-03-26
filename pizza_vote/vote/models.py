from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pizzas/')
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
