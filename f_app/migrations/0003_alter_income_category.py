# Generated by Django 3.2.9 on 2021-12-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_app', '0002_alter_expense_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.CharField(choices=[('Main work', 'Main work'), ('Business', 'Business'), ('Odd job', 'Odd job')], max_length=40),
        ),
    ]
