from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from invoice_generator.models import Invoice,InvoiceItem,CustmerInvoiceInfo
from django.db.models import Sum  
from django.template.loader import get_template
from weasyprint import HTML
import tempfile






@login_required(login_url='login')
def index(request):
 
        # Fetch all customers, invoices, and products
        itemList = Invoice.objects.all()    
        customers = CustmerInvoiceInfo.objects.all()
        Products = InvoiceItem.objects.all()  # Fetch all products

        # Calculate the total amount by summing the 'amount' field of all products
        total_amount = Products.aggregate(Sum('amount'))['amount__sum'] or 0.0

        context = {
            'customers': customers,
            'itemList': itemList,
            'Products': Products,  # Use the correct variable name
            'total_amount': total_amount  # Pass the total amount to the template
        }

        return render(request, 'invoice.html', context)

        with tempfile.NamedTemporaryFile(delete=True) as tmpfile:
            HTML(string=html).write_pdf(target=tmpfile.name)
            with open(tmpfile.name, 'rb') as pdf_file:
                response.write(pdf_file.read())

        return response







@login_required(login_url='login')
def add_product(request):

    if request.method == "POST":
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        unit_price = request.POST.get('unit_price')

        if product and quantity and unit_price:
            quantity = int(quantity)
            unit_price = float(unit_price)
            amount = quantity * unit_price

            # Create a new product and save it to the database
            new_product = InvoiceItem(
                product     = product,
                quantity    = quantity,
                unit_price  = unit_price,
                amount      = amount 
            )
            new_product.save()

        return redirect('index')

    return render(request, 'invoice.html')





@login_required(login_url='login')
def remove_product(request, id):

    rm = InvoiceItem.objects.get(id=id)
    rm.delete()

    return redirect('index')