from django.shortcuts import render
from .forms import LoanCalculatorForm

def loan_calculator(request):
    monthly_payment = None

    if request.method == 'POST':
        form = LoanCalculatorForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data['principal']
            r = form.cleaned_data['rate'] / 100 / 12
            n = form.cleaned_data['years'] * 12
            
            # Monthly payment calculation using the formula
            monthly_payment = p * r * (1 + r) ** n / ((1 + r) ** n - 1)
    else:
        form = LoanCalculatorForm()

    return render(request, 'loan_calculator/loan_calculator.html', {
        'form': form,
        'monthly_payment': monthly_payment
    })

