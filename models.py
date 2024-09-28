from django.db import models

class IPO(models.Model):
    company_name = models.CharField(max_length=255)
    price_band = models.DecimalField(max_digits=10, decimal_places=2)
    open_date = models.DateField()
    close_date = models.DateField()
    issue_size = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name
