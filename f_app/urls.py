from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='home'), # means, for the main domain, show viev with name 'index', which can be finded in views.index
    path('about',views.about, name='about'),
    path('new_income',views.new_income, name='new_income'),
    path('new_expence',views.new_expence, name='new_expence'),
]

