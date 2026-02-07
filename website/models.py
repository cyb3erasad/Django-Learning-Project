from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'Masala'),
        ('MK', 'Milk'),
        ('EL', 'Elaichi'),
        ('GR', 'Ginger'),
        ('PL', 'Plain')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai_image/')
    date_add = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default='')
    price = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name

