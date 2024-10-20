from django.db import models

class CustmerInvoiceInfo(models.Model):
    
    custmer_name = models.CharField(max_length=2500)
    custmer_address = models.CharField(max_length=2500)
    custmer_phone = models.CharField(max_length=2500)
    custmer_email = models.EmailField(max_length=254)
  
    def __str__(self):
        return self.custmer_name


class Invoice(models.Model):

    invoice_number = models.CharField(max_length=20)
    issue_date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.issue_date}"


# class InvoiceItem(models.Model):
#     invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
#     product = models.CharField(max_length=255)
#     quantity = models.PositiveIntegerField(default=1)
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     def save(self, *args, **kwargs):
#         # Calculate the amount when saving the item
#         self.amount = self.quantity * self.unit_price
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.description} - {self.quantity} @ {self.unit_price}"

class InvoiceItem(models.Model):

    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.product
    