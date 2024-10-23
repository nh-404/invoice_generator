from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from invoice_generator.models import *
from django.db.models import Sum  
from django.template.loader import get_template
from weasyprint import HTML
import tempfile


@login_required(login_url='login')
def index(request):
 

        # Fetch all customers, invoices, and products
        customers = CustomerInfo.objects.all()
        itemList = Invoice.objects.all()
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




@login_required(login_url='login')
def customer_info(request):

    if request.method == "POST":

       customer_name    = request.POST.get('customer_name')
       customer_address  = request.POST.get('address')
       customer_phone   = request.POST.get('phone')
       customer_email   = request.POST.get('email')

       info_save = CustomerInfo( 

        customer_name   = customer_name    ,
        customer_address = customer_address ,
        customer_phone  = customer_phone   ,
        customer_email  = customer_email   

       )
       info_save.save()

       return redirect('index')
       
    return render(request, 'customer_info.html', )


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