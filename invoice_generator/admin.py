from django.contrib import admin
from invoice_generator.models import Invoice, InvoiceItem, CustmerInvoiceInfo

admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(CustmerInvoiceInfo)

