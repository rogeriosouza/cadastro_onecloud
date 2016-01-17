
from django.db import models
from django.utils import timezone

# Create your models here.

class cadastro(models.Model):
    codigo = models.ForeignKey('auth.User')
    cpu = models.IntegerField()
    memoria = models.IntegerField()
    disco = models.IntegerField()
    sistemaoperacional= models.CharField(max_length=7)

    created_date = models.DateTimeField(default = timezone.now )
    published_date = models.DateTimeField(blank=True, null=True)

   
    def publish(self): 
     self.published_date = timezone.now()
     self.save()
    
    
    # created_date = models.DateTimeField(
    #         default=timezone.now)
    # published_date = models.DateTimeField(
    #         blank=True, null=True)
