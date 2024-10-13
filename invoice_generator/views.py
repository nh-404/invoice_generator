from django.shortcuts import render,redirect
from invoice_generator.models import Invoice,InvoiceItem,CustmerInvoiceInfo

# Create your views here.


def index(request):

    itemList = Invoice.objects.all()    
    customers = CustmerInvoiceInfo.objects.all()
    products = InvoiceItem.objects.all()
    context = {
        'customers': customers,
        'itemList': itemList,
        'prosucts': products
        #'total_amount': sum(item.amount for item in itemList)  # Assuming you want total calculation
    }

    return render(request, 'invoice.html', context)


def add_product(request):

    if request.method == "POST":

        product_name = request.POST.get('product')
        quantity = request.POST.get('quantity')
        unit_price = request.POST.get('unit_price')

        # Ensure data is being passed correctly
        if product_name and quantity and unit_price:
            
            quantity = int(quantity)
            unit_price = float(unit_price)
            amount = quantity * unit_price

            # Create a new product and save to database
            new_product = InvoiceItem(
                product=product_name,
                quantity=quantity,
                unit_price=unit_price,
                amount=amount
            )
            new_product.save()
        return redirect('index')  # Replace with the name of your success page

    return render(request, 'invoice.html')



# def itemList(request):
    
#     if request.method == 'POST':
#         total_amount = 0
#         itemList = []

#         # Assuming you have a way to determine how many items were submitted
#         item_count = request.POST.get('item_count', 0)

#         for i in range(1, int(item_count) + 1):
#             description = request.POST.get(f'description_{i}')
#             quantity = int(request.POST.get(f'quantity_{i}', 0))
#             unit_price = float(request.POST.get(f'unit_price_{i}', 0))

#             # Calculate the amount
#             amount = quantity * unit_price
#             total_amount += amount

#             # Create an InvoiceItem instance (if needed)
#             itemList.append({
#                 'description': description,
#                 'quantity': quantity,
#                 'unit_price': unit_price,
#                 'amount': amount
#             })

#         return render(request, 'invoice.html', {'itemList': itemList, 'total_amount': total_amount})

#     # Render the invoice form initially
#     itemList = []  # Initial empty item list
#     return render(request, 'invoice.html', {'itemList': itemList, 'total_amount': 0})