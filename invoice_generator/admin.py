from django.contrib import admin
from invoice_generator.models import Invoice, InvoiceItem

admin.site.register(Invoice)
admin.site.register(InvoiceItem)

