from django.shortcuts import render,render_to_response,get_object_or_404

from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.models import User

# Create your views here.
@csrf_protect
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        variables = RequestContext(request,{'form':form})

        if form.is_valid():
            user = User.objects.create_user(
            username = form.cleaned_data['username'],
            password  =form.cleaned_data['password1'],
            email = form.cleaned_data['email'],
            )
            return HttpResponseRedirect('/home');
        else:
            print form.errors

    else:
        form = RegistrationForm()
        variables = RequestContext(request,{'form':form})
    return render_to_response('registration/register.html',variables)
	
def changepassword(request):
    if request.method =='POST':
        form = ChangePasswordForm(request.POST)
        variables = RequestContext(request,{'form':form})

        if form.is_valid():
            current_user = request.user
            uid = current_user.id
            user = get_object_or_404(User, id=uid)
            user.set_password(request.POST['password1'])
            user.save()
            return HttpResponseRedirect('/home');



    else:
        form = ChangePasswordForm()
        variables = RequestContext(request,{'form':form})
    return render_to_response('registration/changepassword.html',variables)
def changeprofile(request):
    current_user = request.user
	
    if request.method =='POST':
        form = ChangeProfileForm(request.POST)
        variables = RequestContext(request,{'form':form,'user':current_user})

        if form.is_valid():
            current_user = request.user
            uid = current_user.id
            user = get_object_or_404(User, id=uid)
            user.first_name = request.POST['fname']
            user.last_name = request.POST['lname']
            user.email = request.POST['email']
            user.save()
            return HttpResponseRedirect('/home');



    else:
        form = ChangeProfileForm()
        variables = RequestContext(request,{'form':form,'user':current_user})
    return render_to_response('registration/changeprofile.html',variables)
def register_success(request):
    return render_to_response('registration/success.html')
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
@login_required
def home(request):
    return render_to_response(
    'home.html',
    {'user': request.user}
    )

