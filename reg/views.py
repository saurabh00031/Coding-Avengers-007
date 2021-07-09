from django.shortcuts import render, redirect
from .models import hspinfo, usrinfo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .forms import HospitalReg, UserReg
from django.views.generic import CreateView
from .decorators import user_required, hospital_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .models import User as my_usr

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def c19_info(request):
    return render(request, 'c19_info.html')

def sgin_user(request):
    if request.method == "POST":
        # check if user has entered correct credientials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            if user.is_user == True:
                login(request, user)
                return redirect("sginpg_user")
            else:
                messages.error(request, 'You are not authorized to access this page!')
        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid username or password!')    
            return render(request, 'sgin_user.html')

    return render(request, 'sgin_user.html')

@login_required
@user_required
def sginpg_user(request):
    hos_data = hspinfo.objects.all()
    hosp = {
        "hosp_info" : hos_data
    }
    return render(request, 'sginpg_user.html', hosp)

@login_required
@user_required
def search(request):
    qur = request.GET.get('search')
    ct = hspinfo.objects.filter(city__contains = qur)
    return render(request, 'search.html', {'ct': ct})

@login_required
@user_required
def update_usr_data(request):
    this_usr = usrinfo.objects.get(user = request.user.id)
    usr_inf = my_usr.objects.get(id = request.user.id)
    if request.method == "POST":
        fname = request.POST.get('fname')
        phnum = request.POST.get('phnum')
        email = request.POST.get('email')
        city = request.POST.get('city')
        addres = request.POST.get('addres')

        this_usr.full_Name = fname
        this_usr.phone = phnum
        this_usr.email = email
        this_usr.city = city
        this_usr.address = addres
        this_usr.save()
        
        usr_inf.email = email
        usr_inf.save()
        messages.success(request, 'Data Updated Successfully!')    

        
    usr_dat = {
        "usr_info" : this_usr,
        "my_usr_inf" : usr_inf
    }
    return render(request, 'usr_edit.html', usr_dat)

@login_required
@user_required
def change_pass_usr(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Password changed successfully!')    
            update_session_auth_hash(request, fm.user)
            return redirect("sginpg_user")
    else:
        fm = PasswordChangeForm(user = request.user)
            
    return render(request, 'change_pass.html', {'form':fm})

def sgin_hsp(request):
    if request.method == "POST":
        # check if user has entered correct credientials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            if user.is_hospital == True:
                login(request, user)
                return redirect("sginpg_hsp")
            else:
                messages.error(request, 'You are not authorized to access this page!')    

        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid username or password!')    
            return render(request, 'sgin_hsp.html')

    return render(request, 'sgin_hsp.html')

@login_required
@hospital_required
def sginpg_hsp(request):
    hos_data = hspinfo.objects.filter(user = request.user.id)
    hosp = {
        "hosp_info" : hos_data
    }
    return render(request, 'sginpg_hsp.html', hosp)

@login_required
@hospital_required
def update_data(request):
    this_hsp = hspinfo.objects.get(user = request.user.id)
    usr_inf = my_usr.objects.get(email = request.user.email)
    if request.method == "POST":
        hosname = request.POST.get('hosname')
        phnum = request.POST.get('phnum')
        email = request.POST.get('email')
        city = request.POST.get('city')
        addres = request.POST.get('addres')
        nbd = request.POST.get('nbd')
        nvnt = request.POST.get('nvnt')
        nvc = request.POST.get('nvc')

        this_hsp.hospital_Name = hosname
        this_hsp.phone = phnum
        this_hsp.email = email
        this_hsp.city = city
        this_hsp.address = addres
        this_hsp.no_of_beds = nbd
        this_hsp.no_of_ventilators = nvnt
        this_hsp.no_of_vaccines = nvc
        this_hsp.save()

        usr_inf.email = email
        usr_inf.save()
        messages.success(request, 'Data Updated Successfully!') 
        
    hosp = {
        "hosp_info" : this_hsp,
        "my_usr_inf" : usr_inf
    }
    return render(request, 'hsp_edit.html', hosp)

@login_required
@hospital_required
def change_pass_hsp(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Password changed successfully!')    
            update_session_auth_hash(request, fm.user)
            return redirect("sginpg_hsp")
    else:
        fm = PasswordChangeForm(user = request.user)
            
    return render(request, 'change_pass.html', {'form':fm})

def sout(request):
    logout(request)
    return render(request, 'index.html')

class HspView(CreateView):
    model = User
    form_class = HospitalReg
    template_name = 'register_hsp.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'hospital'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'User Created successfully!')    
        login(self.request, user)
        return redirect("sgin_hsp")

class UsrView(CreateView):
    model = User
    form_class = UserReg
    template_name = 'register_user.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'User Created successfully!')    
        login(self.request, user)
        return redirect("sgin_user")
