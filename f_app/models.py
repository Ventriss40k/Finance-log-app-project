from django.db import models
# Each class, inherited from models.Model will be transfered to DB as table
# Create your models here.
CATEGORY_INCOME = (('Main work', 'Main work'), ('Business', 'Business'), ('Odd job','Odd job'))
CATEGORY_EXPENCE = (('Food', 'Food'),('Appartment rent', 'Appartment rent'), ('Clothes', 'Clothes'), ('Other','Other'), ('Education','Education'))



class Income(models.Model):
    # This is set of tupples for income category choice. First in tupple represent record in DB, second - how user will see it on site.
    CATEGORY = CATEGORY_INCOME
    amount = models.IntegerField()
    date = models.DateField()
    category = models.CharField(max_length=40, choices=CATEGORY) # max lenght should be as big as max lengt of first record in category tupples
    def __str__(self) -> str:
        return f"{self.category}, {self.amount}, {self.date}"
    # class Meta:
    #     verbose_name = "Доход"
    #     verbose_name_plural ="Доходы"
    #  In this way we can easily change the name of class, represented in admin table




class Expense(models.Model):
    CATEGORY = CATEGORY_EXPENCE
    amount = models.IntegerField()
    date = models.DateField()
    category = models.CharField(max_length= 40, choices=CATEGORY)
    def __str__(self) -> str:
        return f"{self.category}, {self.amount}, {self.date}"
    # class Meta:
    #     verbose_name = "Расход"
    #     verbose_name_plural ="Расходы"