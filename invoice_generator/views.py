from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == 'POST':
        descriptions = request.POST.getlist('description[]')
        quantities = request.POST.getlist('quantity[]')
        unit_prices = request.POST.getlist('unit_price[]')

        # Calculate amounts and total
        amounts = []
        total_amount = 0
        for qty, price in zip(quantities, unit_prices):
            amount = float(qty) * float(price)
            amounts.append(f'{amount:.2f}')
            total_amount += amount
        
        return render(request, 'invoice.html', {
            'descriptions': descriptions,
            'quantities': quantities,
            'unit_prices': unit_prices,
            'amounts': amounts,
            'total_amount': f'{total_amount:.2f}'
        })
    
    # For GET request
    return render(request, 'invoice.html', {
        'descriptions': [],
        'quantities': [],
        'unit_prices': [],
        'amounts': [],
        'total_amount': '0.00'
    })
