from django.urls import path
from . import views

app_name = 'loan_calculator'

urlpatterns = [
    path('loan_calculator/', views.loan_calculator, name='loan_calculator'),
]
