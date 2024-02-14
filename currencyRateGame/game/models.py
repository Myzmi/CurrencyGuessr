from django.db import models

# Create your models here.
class CurrencyRate(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    rate = models.FloatField()

    def __str__(self):
        return f"{self.month}.{self.year}: {self.rate} TRY"