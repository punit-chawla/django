from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from .models import Classes,Sections
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from manage_classes.forms import *
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
	current_user = request.user
	uid = current_user.id
	class_list = Classes.objects.filter(user_id=uid).order_by('-id')
	paginator = Paginator(class_list, 30)
	page = request.GET.get('page')


	try:
		classes = paginator.page(page)
	except PageNotAnInteger:

		classes = paginator.page(1)
	except EmptyPage:

		classes = paginator.page(paginator.num_pages)
	return render(request, 'classes/index.html', {'classes':classes})
def edit(request,class_id):
    classs= get_object_or_404(Classes, id=class_id)
    return render(request, 'classes/editclass.html', {'classs': classs})
def update(request,class_id):
	classs = get_object_or_404(Classes, id=class_id)
	classs.class_name = request.POST['cname']
	classs.save()

	return HttpResponseRedirect(reverse('manage_classes:classes'))
@csrf_protect
def add(request):

    if request.method =='POST':
        form = addclassform(request.POST)
        variables = RequestContext(request, {'form': form})
        if form.is_valid():


            current_user = request.user
            user = User.objects.get(id=current_user.id)
            classs = Classes.objects.create(
            class_name = form.cleaned_data['name'],
            
			user_id = user.id,
            add_date =timezone.now(),
            )

            return HttpResponseRedirect(reverse('manage_classes:classes'))
    else:
        form = addclassform()
        variables = RequestContext(request,{'form':form})
    return render_to_response('classes/addclassform.html',variables)
def delete(request,class_id):
	classs = get_object_or_404(Classes, id=class_id)
	classs.delete()

	return HttpResponseRedirect(reverse('manage_classes:classes'))