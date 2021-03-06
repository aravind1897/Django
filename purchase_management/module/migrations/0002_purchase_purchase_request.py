# Generated by Django 4.0 on 2021-12-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'purchase_manager',
            },
        ),
        migrations.CreateModel(
            name='purchase_request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('team', models.CharField(max_length=100)),
                ('req_product', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('product_link', models.TextField(blank=True)),
                ('price', models.CharField(max_length=100)),
                ('project_manager', models.CharField(blank=True, max_length=100)),
                ('purchase_manager', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(max_length=200)),
                ('request_date', models.DateTimeField(blank=True)),
                ('approved_date', models.DateTimeField(blank=True)),
                ('purchase_date', models.DateTimeField(blank=True)),
            ],
            options={
                'db_table': 'purchase_request',
            },
        ),
    ]
