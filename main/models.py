from django.db import models


# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=100, unique=True)
    numbers = models.PositiveIntegerField(default=0)
    distance = models.PositiveIntegerField(default=0)
    data = models.DateTimeField()

    def __str__(self):
        return self.name + str(self.numbers) + str(self.distance) + str(self.data)

