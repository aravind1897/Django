# Generated by Django 4.0 on 2021-12-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0002_purchase_purchase_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_request',
            name='deivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
