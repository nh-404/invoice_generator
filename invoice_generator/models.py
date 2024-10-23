from django.db import models
from django.contrib.auth.models import User

class CustomerInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensure this is required for linking to a user
    customer_name = models.CharField(max_length=250)
    customer_address = models.CharField(max_length=250)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.customer_name

class Invoice(models.Model):
    customer = models.ForeignKey(CustomerInfo, related_name='invoices', on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=20, unique=True)  # Ensure invoice numbers are unique
    issue_date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.issue_date}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        # Calculate the amount when saving the item
        self.amount = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} - {self.quantity} @ {self.unit_price}"
