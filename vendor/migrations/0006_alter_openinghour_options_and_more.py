# Generated by Django 4.1.7 on 2023-06-01 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_openinghour'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openinghour',
            options={'ordering': ('day', '-from_hour')},
        ),
        migrations.AlterUniqueTogether(
            name='openinghour',
            unique_together={('vendor', 'day', 'from_hour', 'to_hour')},
        ),
    ]
