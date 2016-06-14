from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from .models import Teachers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from teachers.forms import *
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    current_user  = request.user
    uid = current_user.id
    teacher_list = Teachers.objects.filter(user_id=uid).order_by('-id')
    paginator = Paginator(teacher_list, 30)
    page = request.GET.get('page')


    try:
        teachers = paginator.page(page)
    except PageNotAnInteger:

        teachers = paginator.page(1)
    except EmptyPage:

        students = paginator.page(paginator.num_pages)
    return render(request, 'teachers/index.html', {'teachers':teachers})
def edit(request,teacher_id):
    teacher= get_object_or_404(Teachers, id=teacher_id)
    return render(request, 'teachers/editteacher.html', {'teacher': teacher})
def update(request,teacher_id):
	teacher = get_object_or_404(Teachers, id=teacher_id)
	teacher.name = request.POST['tname']
	teacher.qualification= request.POST['qualification']
	teacher.city= request.POST['city']
	teacher.state= request.POST['state']
	teacher.address= request.POST['address']
	teacher.phone_number= request.POST['phone_number']
	teacher.experience= request.POST['experience']
	teacher.save()

	return HttpResponseRedirect(reverse('teachers:teachers'))
@csrf_protect
def add(request):

    if request.method =='POST':
        form = addteacherform(request.POST)
        variables = RequestContext(request, {'form': form})
        if form.is_valid():


            current_user = request.user
            user = User.objects.get(id=current_user.id)
            teacher = Teachers.objects.create(
            name = form.cleaned_data['name'],
            qualification  =form.cleaned_data['qualification'],
            address  =form.cleaned_data['address'],
            city  =form.cleaned_data['city'],
            state  =form.cleaned_data['state'],
            phone_number  =form.cleaned_data['phone_number'],
            experience  =form.cleaned_data['expeirience'],
			user_id = user.id,
            add_date =timezone.now(),
            )

            return HttpResponseRedirect(reverse('teachers:teachers'))
    else:
        form = addteacherform()
        variables = RequestContext(request,{'form':form})
    return render_to_response('teachers/addteacherform.html',variables)
def delete(request,teacher_id):
	teacher = get_object_or_404(Teachers, id=teacher_id)
	teacher.delete()

	return HttpResponseRedirect(reverse('teachers:teachers'))







