from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=150, unique=True)
    capital = models.CharField(max_length=150, unique=True)
    continent = models.CharField(max_length=50)
    population = models.IntegerField()
    area = models.FloatField()
    gdp = models.FloatField()
    official_language = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
    
    def __str__(self):
        return self.name