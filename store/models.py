from django.db import models

# Create your models here.
class Store(models.Model):
    title=models.TextField(max_length=50,help_text="Name of the product")
    para=models.TextField(max_length=100,help_text="enter detail of product")
    image=models.ImageField(null=True,upload_to='store_pics')
    email=models.EmailField()