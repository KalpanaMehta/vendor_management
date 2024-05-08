from django.db import models

# Create your models here.
class Purchase_Order (models.Model):
     
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )  
    po_number = models.CharField(max_length= 255,unique=True)
    vendor_code = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE, to_field='vendor_code')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null = True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"PO Number: {self.po_number} - Vendor: {self.vendor_code.name}"
