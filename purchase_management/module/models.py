from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class project(models.Model):  
    project_manager_id = models.AutoField(primary_key=True, null=False),  
    name = models.CharField(max_length=100)
    
    class Meta:  
        db_table = "project_manager"


class purchase(models.Model):  
    purchase_manager_id = models.AutoField(primary_key=True, null=False),  
    name = models.CharField(max_length=100)
    
    class Meta:  
        db_table = "purchase_manager"


class purchase_request(models.Model):  
    id = models.AutoField(primary_key=True, null=False)  
    emp_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    req_product = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    product_link = models.TextField(blank=True)
    price = models.CharField(max_length=100)
    #project_manager = models.ForeignKey(project,on_delete=CASCADE,db_column='project_manager_id')
    project_manager = models.CharField(max_length=100,blank=True)
    purchase_manager = models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=200)
    request_date = models.DateTimeField(blank=True)
    approved_date = models.DateTimeField(blank=True)
    purchase_date = models.DateTimeField(blank=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:  
        db_table = "purchase_request"