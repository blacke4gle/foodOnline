# Generated by Django 4.1.7 on 2023-06-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_vendors_alter_order_tax_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]