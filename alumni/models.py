from django.db import models

# Create your models here.
class socials(models.Model):
    name=models.CharField(max_length=100,help_text="Your full name")
    linkdin_url=models.URLField(help_text="Lindkin profile url")
    Company_name=models.CharField(max_length=100,help_text="Company your are at")
    Company_post=models.CharField(max_length=100,help_text="postion you are at")
    pass_out_year=models.IntegerField(help_text="Your passout year")


