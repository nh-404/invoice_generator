from django.shortcuts import render,redirect
from invoice_generator.models import Invoice,InvoiceItem

# Create your views here.


def index(request):

    itemList= Invoice.objects.all()

    return render(request, 'invoice.html', {'itemList' : itemList})


def itemList(request):
    
    if request.method == 'POST':
        total_amount = 0
        itemList = []

        # Assuming you have a way to determine how many items were submitted
        item_count = request.POST.get('item_count', 0)

        for i in range(1, int(item_count) + 1):
            description = request.POST.get(f'description_{i}')
            quantity = int(request.POST.get(f'quantity_{i}', 0))
            unit_price = float(request.POST.get(f'unit_price_{i}', 0))

            # Calculate the amount
            amount = quantity * unit_price
            total_amount += amount

            # Create an InvoiceItem instance (if needed)
            itemList.append({
                'description': description,
                'quantity': quantity,
                'unit_price': unit_price,
                'amount': amount
            })

        return render(request, 'invoice.html', {'itemList': itemList, 'total_amount': total_amount})

    # Render the invoice form initially
    itemList = []  # Initial empty item list
    return render(request, 'invoice.html', {'itemList': itemList, 'total_amount': 0})