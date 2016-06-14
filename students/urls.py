from django.conf.urls import url
from . import views
app_name = 'students'
urlpatterns = [
    url(r'^$',views.index,name='students'),
    #url(r'^(?s<student_id>[0-9]+)/$',views.detail,name="viewstudent"),
    url(r'^(?P<student_id>[0-9]+)/edit/$',views.edit,name="editstudent"),
	url(r'^(?P<student_id>[0-9]+)/update/$',views.update,name="updatestudent"),
	url(r'^(?P<student_id>[0-9]+)/delete/$',views.delete,name="deletestudent"),
    url(r'^add',views.add,name="addstudent"),
     
]