from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=300)
    Pub_date = models.DateTimeField(auto_now=False)


    def __str__(self):
        return self.title
    
