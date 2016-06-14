from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from .models import Students

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from students.forms import *
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from manage_classes.models import *

# Create your views here.
@login_required
def index(request):
    current_user  = request.user
    uid = current_user.id
    student_list = Students.objects.filter(user_id=uid).order_by('-id')
    paginator = Paginator(student_list, 30)
    page = request.GET.get('page')


    try:
        students = paginator.page(page)
    except PageNotAnInteger:

        students = paginator.page(1)
    except EmptyPage:

        students = paginator.page(paginator.num_pages)
    return render(request, 'students/index.html', {'students':students})




	

def delete(request,student_id):
	student = get_object_or_404(Students, id=student_id)
	student.delete()

	return HttpResponseRedirect(reverse('students:students'))
def edit(request,student_id):
    classes = Classes.objects.filter().order_by('-id')

    student = get_object_or_404(Students, id=student_id)
    return render(request, 'students/editstudent.html', {'student': student,'classes':classes})
def update(request,student_id):
	student = get_object_or_404(Students, id=student_id)
	student.name = request.POST['sname']
	student.classs= request.POST['classs']
	student.save()

	return HttpResponseRedirect(reverse('students:students'))

@csrf_protect
def add(request):
    classes = Classes.objects.filter().order_by('-id')
	
    if request.method =='POST':
        form = addstudentform(request.POST)
        if form.is_valid():
            current_user = request.user
            user = User.objects.get(id=current_user.id)
            student = Students.objects.create(
            name = form.cleaned_data['name'],
            classs  =form.cleaned_data['classs'],
			user_id = user.id,
            add_date =timezone.now(),
            )

            return HttpResponseRedirect(reverse('students:students'))
    else:
        form = addstudentform()
        variables = RequestContext(request,{'form':form,'classes':classes})
    return render_to_response('students/addstudentform.html',variables)