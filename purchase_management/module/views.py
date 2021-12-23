from django.shortcuts import render,redirect
from module.models import purchase,project,purchase_request
from module.forms import ProjectForm,PurchaseForm,RequestForm
from datetime import date
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def main(request):
    if request.method == "POST":  
        utype = request.POST['utype']
        if 'Employee' in utype:
            return redirect('/index')
        elif 'Project_Manager' in utype:
            return redirect('/pr_index')
        else:
            return redirect('/pu_index')
    else:
        return render(request,'main.html')


def index(request):  
    purchase_req = purchase_request.objects.values() 
    project_mgr = project.objects.values() 
    purchase_mgr = purchase.objects.values()  
    return render(request,'index.html',{'pur_req':purchase_req,'pj_mgr':project_mgr,'pu_mgr':purchase_mgr})
    

def add(request):
    if request.method == "POST":  
        name = request.POST['name']
        team = request.POST['team']
        req_pro = request.POST['req_pro']
        purpose = request.POST['purpose']
        link = request.POST['link']
        price = request.POST['price']
        mgr = request.POST['mgr']
        insert = purchase_request.objects.create(emp_name=name,team=team,req_product=req_pro,purpose=purpose,product_link=link,
        price=price,project_manager=str(mgr),purchase_manager='Not Assigned',status='Pending for Approval',request_date=date.today())
        messages.success(request,'Request added successfully')
        return redirect('/index')
    else:
        project_mgr = project.objects.all() 
        form = RequestForm()
    return render(request,'add_req.html',{'form':form,'manager':project_mgr}) 


def project_index(request):  
    purchase_req = purchase_request.objects.values() 
    project_mgr = project.objects.values() 
    purchase_mgr = purchase.objects.values()    
    return render(request,'project_index.html',{'pur_req':purchase_req,'pj_mgr':project_mgr,'pu_mgr':purchase_mgr})


def purchase_index(request):  
    purchase_req = purchase_request.objects.values() 
    project_mgr = project.objects.values() 
    purchase_mgr = purchase.objects.values() 
    return render(request,'purchase_index.html',{'pur_req':purchase_req,'pj_mgr':project_mgr,'pu_mgr':purchase_mgr})


def change_status(request):
    req_id = request.GET.get('id')
    status = request.GET.get('status')
    utype = request.GET.get('utype')
    if 'project' in utype:
        if '1' in status:
            status = 'Approved by project manager'
            purchase_manager = purchase.objects.values('name').filter(id=1) 
            approve_date = date.today() 
            update = purchase_request.objects.filter(id=req_id).update(status=status,approved_date=approve_date,purchase_manager=list(purchase_manager)[0]['name'])
        elif '2' in status:
            status = 'Rejected by project manager'
            purchase_manager = purchase.objects.values('name').filter(id=0)
            update = purchase_request.objects.filter(id=req_id).update(status=status)
    elif 'purchase' in utype:
        if '1' in status:
            status = 'Order placed'
            purchase_manager = purchase.objects.values('name').filter(id=1)
            purchase_date = date.today() 
            update = purchase_request.objects.filter(id=req_id).update(status=status,purchase_date=purchase_date,purchase_manager=list(purchase_manager)[0]['name'])  
        elif '2' in status:
            status = 'Rejected by purchase manager'
            update = purchase_request.objects.filter(id=req_id).update(status=status)  
        elif '3' in status:
            status = 'Closed'
            del_date = date.today() 
            update = purchase_request.objects.filter(id=req_id).update(status=status,delivery_date=del_date)
     
    return HttpResponse('success')
