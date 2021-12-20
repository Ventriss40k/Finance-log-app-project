from django.contrib import admin
from .models import Income
from .models import Expense
# Register your models here.
# Tablas which must be acessed in admin panel should be registred here
admin.site.register(Income)
admin.site.register(Expense)