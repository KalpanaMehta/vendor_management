from django.db import models

# Create your models here.
class Vendor_Performance (models.Model):
    vendor_code = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE, to_field='vendor_code')
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()


    def __str__(self):
        return self.name
