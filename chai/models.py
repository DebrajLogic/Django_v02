from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('OL', 'OOLONG'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    price = models.CharField(max_length=10, default='$4.99')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
