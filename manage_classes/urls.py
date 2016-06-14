from django.conf.urls import url
from . import views
app_name = 'manage_classes'
urlpatterns = [
    url(r'^$',views.index,name='classes'),
    #url(r'^(?s<student_id>[0-9]+)/$',views.detail,name="viewstudent"),
    url(r'^(?P<class_id>[0-9]+)/edit/$',views.edit,name="editclass"),
	url(r'^(?P<class_id>[0-9]+)/update/$',views.update,name="updateclass"),
	url(r'^(?P<class_id>[0-9]+)/delete/$',views.delete,name="deleteclass"),
    url(r'^add',views.add,name="addclass"),

]