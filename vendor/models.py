from django.db import models

# Create your models here.
class Vendor (models.Model):
    name = models.CharField(max_length= 255)
    contact_details = models.CharField(max_length= 255)
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique = True)
    on_time_delivery_rate = models.FloatField(null = True, blank = True)
    quality_rating_avg = models.FloatField(null = True, blank = True)
    average_response_time = models.FloatField(null = True, blank = True)
    fulfillment_rate = models.FloatField(null = True, blank = True)


    def __str__(self):
        return self.name

"""
● name: CharField - Vendor's name.
● contact_details: TextField - Contact information of the vendor.
● address: TextField - Physical address of the vendor.
● vendor_code: CharField - A unique identifier for the vendor.
● on_time_delivery_rate: FloatField - Tracks the percentage of on-time deliveries.
● quality_rating_avg: FloatField - Average rating of quality based on purchase
orders.
● average_response_time: FloatField - Average time taken to acknowledge
purchase orders.
● fulfillment_rate: FloatField - Percentage of purchase orders fulfilled successfully
"""