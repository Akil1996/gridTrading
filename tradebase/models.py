from django.db import models

# Create your models here.
class BrokerDetails(models.Model):
    userName = models.CharField(max_length=100)
    passWord = models.CharField(max_length=100)
    accessToken = models.CharField(max_length=100)

    def __str__(self):
        return self.userName
