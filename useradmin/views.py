from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse

def signin(request):
    if request.method=="POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        try:
            result = VendorLog.objects.get(Q(password=password)&(Q(userName=name)|Q(email=name)))
            if result:
                request.session['user_id'] = result.pk
                return redirect(home)
            else:
                messages.warning(request,'user doesnt exist!')
                return render(request,"signin.html")
        except:
            messages.warning(request,'user doesnt exist!')
            return render(request,"signin.html")
    return render(request,'signin.html')

def logout_view(request):
    logout(request)
    # del request.session['user_id']
    return redirect(signin)

def home(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect(signin)
    moduleList = []
    for user in VendorLog.objects.filter(id=user_id):
        for singleModule in user.module.all():
            moduleList.append(singleModule.pk)
        for group in user.groups.all():
            for groupModule in group.group_modules.all():
                moduleList.append(groupModule.pk)
                # print(moduleList)
    # print(moduleList)
    return render(request, 'admin-lte/index.html',{'moduleList':moduleList})


# from joblib import load
# ml = load('/home/vishal/Desktop/vishal/customAdmin/mlmodels/.model.joblib')
import pandas as pd
def dfmodule(request):
    df=pd.DataFrame(list(VendorLog.objects.all().values()))
    print(df)
    print(df['email'])
    return HttpResponse(df)