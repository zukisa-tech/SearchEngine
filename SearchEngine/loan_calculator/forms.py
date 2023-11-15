from django import forms

class LoanCalculatorForm(forms.Form):
    principal = forms.DecimalField(label='Principal Amount', decimal_places=2, min_value=0.01)
    rate = forms.DecimalField(label='Annual Interest Rate (%)', decimal_places=2, min_value=0.01)
    years = forms.IntegerField(label='Loan Duration (Years)', min_value=1)
