from django.db import models

# Create your models here.
class FutureData(models.Model):
    instrument = models.CharField(max_length=20)
    date = models.DateField()
    avg_price = models.FloatField()
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.instrument} - {self.date}"