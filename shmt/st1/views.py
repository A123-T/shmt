from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from .forms import signupForm
from django.contrib import messages
# Create your views here.
def st1(request): 
    if request.method =="POST":
        fm = signupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully!!!')
            fm.save()
    else:
        fm = signupForm()  
    return render(request, 'reg/singup.html',{'form':fm})
                                            
def user_login(request):
    if not request.user.is_authenticated: 
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)                
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'reg/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
      
def profile(request):
    if request.user.is_authenticated:
        messages.success(request,"Login Successfully!!")
        return render(request,'reg/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')
        
def user_logout(request):

    logout(request)
    return HttpResponseRedirect('/login/')
# using with old password 
def user_pwd(request):

   if request.user.is_authenticated: 
    if request.method == "POST":    
        fm = PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,"Password sucessfully changed !!!")
            return HttpResponseRedirect('/changepwd/',)
            
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request,'reg/changepwd.html',{'form': fm})
   else:
       return HttpResponseRedirect('/login/',)

#using without old password
def user_pwd1(request):

   if request.user.is_authenticated: 
    if request.method == "POST":    
        fm = SetPasswordForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,"Password sucessfully changed !!!")
            return HttpResponseRedirect('/changepwd1/',)
    else:
        fm = SetPasswordForm(user=request.user)
    return render(request,'reg/changepwd1.html',{'form': fm})
   else:
       return HttpResponseRedirect('/login/',)

