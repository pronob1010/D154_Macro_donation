from django.db import models

class donation(models.Model):
    name = models.CharField(max_length=25)
    about = models.TextField(max_length=50, null=True, blank=True)
    amount = models.PositiveBigIntegerField()
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)