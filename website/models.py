from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

## One to Many
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"

## Many to Many

class ChaiStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name='store')    

    def __str__(self):
        return self.name
    
## One to One

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)     
    valid_date = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.name.chai}"